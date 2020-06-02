from flask import Flask, render_template, request, session, url_for,redirect, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import session
from form import valid
from flask_googlemaps import GoogleMaps
from map1 import map
from ordering import *
from sqlalchemy import ForeignKey, func
from datetime import date
from email.mime.text import MIMEText
import smtplib
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/foodmaza'
#engine=create_engine('postgresql://postgres:postgres123@localhost/login')
app.secret_key='dont tell anyone'
db=SQLAlchemy(app)
#x=Flask(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    user_name=db.Column(db.String(100), unique=True)
    user_pwd=db.Column(db.String(8))

    def __init__(self, user_name, user_pwd):
        self.user_name=user_name
        self.user_pwd=user_pwd

@app.route("/index", methods=['GET','POST'])
def foodmaza():
    return render_template("index.html")
@app.route("/log", methods=['GET','POST'])
def log():

    return render_template("login.html")


@app.route("/login", methods=['GET','POST'])
def submission():
    #error=None
    if request.method=='POST':
          global user
          user=request.form.get("uname")
          pwd=request.form.get("psw")
          session.user = user
          #app.session['user']=user
          result=db.session.query(Data).filter(Data.user_name.in_([user]), Data.user_pwd.in_([pwd])).first()
          db.session.commit()
          print(result)
          if not result:
               flash("INVALID INPUT")
               return redirect(url_for('log') )
          else:
               return render_template("submission.html", name=session.user)
    else:
           return render_template("submission.html", name=session.user)




class Sign(db.Model):
    __tablename__="sign"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    number=db.Column(db.String(100))
    db.UniqueConstraint(number)
    address=db.Column(db.String(100))
    mail=db.Column(db.String(100))
    user_name=db.Column(db.String(100),unique=True)
    #db.UniqueConstraint(user_name)
    user_pwd=db.Column(db.String(8))
    #test=db.relationship('Order', backref='sign')
    #test1=db.relationship('Customer' , backref='sign')


    def __init__(self,name,number,address,mail, user_name, user_pwd):
        self.name=name
        self.number=number
        self.address=address
        self.mail=mail
        self.user_name=user_name
        self.user_pwd=user_pwd




@app.route("/sign", methods=['GET','POST'])
def sign():
    #register=signupform()
    return render_template("submit.html")
@app.route("/signup", methods=['GET','POST'])
def sub():
    if request.method=='POST':
      sign=request.form.get("signup")
      nam=request.form.get("name")
      num=request.form.get("contact")
      addr=request.form.get("add")
      mal=request.form.get("email")
      use=request.form.get("u_name")
      pw=request.form.get("psw")
      rep=request.form.get("psw-repeat")
      print(sign)
      email_=valid(mal)
      #form=signupform()
      if db.session.query(Sign).filter(Sign.number==num).count():
           flash("This number is already registered")
           return redirect(url_for('sign'))
      elif db.session.query(Sign).filter(Sign.user_name==use).count():
           flash("Sorry try again with some other username")
           return redirect(url_for('sign'))
      elif db.session.query(Sign).filter(Sign.mail==mal).count():
         flash("This E-mail is already registered")
         return redirect(url_for('sign'))
      elif len(num) < 10 or len(num)>10:
          flash("It seems you have entered a invalid number")
          return render_template("submit.html")
      elif email_==False:
          flash("Invalid Email")
          return redirect(url_for('sign'))
      elif pw!=rep:
          flash("Password did not match")
          return redirect(url_for('sign'))
      else:
        current=Data(user_name=use,user_pwd=pw)
        data=Sign(name=nam,number=num,address=addr,mail=mal,user_name=use,user_pwd=pw)
        #cust=Customer(c_name=nam,c_number=num,c_address=addr,c_mail=mal,c_uname=use)
        print(data)
        db.session.add(data)
        db.session.add(current)
        #db.session.add(cust)
        db.session.commit()
        flash("Congratulations! Welcome to the Food kingdom.. Please login ")
        return redirect(url_for('log'))
class Cart(db.Model):
    __tablename__="cart"
    id=db.Column(db.Integer, primary_key=True)
    order_id=db.Column(db.Integer, ForeignKey('order.order_id'))
    food_item=db.Column(db.String(100))
    price=db.Column(db.Integer)
    tprice=db.Column(db.Integer)
    quantity= db.Column(db.String(100))
    def __init__(self,order_id, food_item, price, tprice,quantity):
        self.order_id=order_id
        self.food_item=food_item
        self.price=price
        self.tprice=tprice
        self.quantity=quantity
class Order(db.Model):
    __tablename__= 'order'
    order_id=db.Column(db.Integer, primary_key=True)
    #db.UniqueConstraint(order_id)
    cust_name=db.Column(db.String(100))
    date=db.Column(db.Date)
    sign=db.relationship('Cart',backref='order')
    cust=db.relationship('Customer',backref='order')
    def __init__(self,cust_name,date):
        self.cust_name=cust_name
        self.date=date

class Customer(db.Model):
        __tablename__="customer_data"
        id=db.Column(db.Integer, primary_key=True)
        c_name=db.Column(db.String(100))
        c_number=db.Column(db.String(100))
        c_address=db.Column(db.String(100))
        c_mail=db.Column(db.String(100))
        c_uname=db.Column(db.String(100))
        datee=db.Column(db.Date)
        r_orderid=db.Column(db.Integer, ForeignKey('order.order_id'))

        def __init__(self,c_name,c_number,c_address,c_mail, c_uname,r_orderid,datee):
            self.c_name=c_name
            self.c_number=c_number
            self.c_address=c_address
            self.c_mail=c_mail
            self.c_uname=c_uname
            self.r_orderid=r_orderid
            self.datee=datee


@app.route("/outlets", methods=['GET','POST'])
def outlets():
    return render_template("feed.html")
@app.route("/map", methods=['GET','POST'])
def mapping():
    map()
    return render_template("map_one.html")
@app.route("/about", methods=['GET','POST'])
def about():
    return render_template("about.html")
@app.route("/menu", methods=['GET','POST'])
def menu():
    return render_template("menu.html")
@app.route("/order_food", methods=['GET','POST'])
def order():
    try:
      return render_template("order.html",name=session.user)
    except AttributeError:
      return redirect(url_for('foodmaza'))

@app.route("/aboutus", methods=['GET','POST'])
def aboutus():
    try:
       return render_template("aboutus.html",name=session.user)
    except AttributeError:
       return redirect(url_for('foodmaza'))
@app.route("/menus", methods=['GET','POST'])
def menus():
    try:
       return render_template("menus.html",name=session.user)
    except AttributeError:
       return redirect(url_for('foodmaza'))
@app.route("/outlet", methods=['GET','POST'])
def out():
    try:
      return render_template("outlet.html",name=session.user)
    except AttributeError:
      return redirect(url_for('foodmaza'))

@app.route("/order", methods=['GET','POST'])
def ordering():
    checkout()
    return redirect(url_for('order'))

@app.route("/checkout", methods=['GET','POST'])
def check():
    sum=0
    orderid=db.session.query(Customer.r_orderid).filter(Customer.c_uname==session.user).first()
    item=db.session.query(Cart).filter(Cart.order_id==orderid).all()
    #grand=db.session.query(func.sum(Cart.tprice)).filter(Cart.order_id==orderid)
    grand=db.session.query(func.sum(Cart.tprice)).filter(Cart.order_id==orderid).first()[0]
    #g=(int)grand
    db.session.commit()
    send_email()
    flash("ORDERED SUCCSSFULLY. YOU WILL RECIEVE EMAIL FOR THE SAME")
    return render_template("checkout.html",item=item,name=session.user,grand=grand)
class Menu(db.Model):
    __tablename__= 'foodmaza_menu'
    id=db.Column(db.Integer, primary_key=True)
    food_item=db.Column(db.String(100))
    price=db.Column(db.Integer)
    def __init__(self, food_item, price):
        self.food_item=food_item
        self.price=price

def checkout():
    if request.method=='POST':
         num1= request.form.get('number1')
         num2= request.form.get('number2')
         num3= request.form.get('number3')
         num4= request.form.get('number4')
         num5=request.form.get('number5')
         num6= request.form.get('number6')
         num7= request.form.get('number7')
         num8= request.form.get('number8')
         num9= request.form.get('number9')
         num10= request.form.get('number10')
         num11= request.form.get('number11')
         num12= request.form.get('number12')
         num13= request.form.get('number13')
         num14= request.form.get('number14')
         num15= request.form.get('number15')
         num16= request.form.get('number16')
         num17= request.form.get('number17')
         num18= request.form.get('number18')
         num19= request.form.get('number19')
         num20= request.form.get('number20')
         num21= request.form.get('number21')
         num22= request.form.get('number22')
         num23= request.form.get('number23')
         num24= request.form.get('number24')
         num25= request.form.get('number25')
         num26= request.form.get('number26')
         num27= request.form.get('number27')
         num28= request.form.get('number28')
         num29= request.form.get('number29')
         num30= request.form.get('number30')
         num31= request.form.get('number31')


         number=[num1, num2, num3, num4, num5, num6, num7, num8, num9, num10,num11,num12,num13,num14,num15,num16,num17, num18, num19,num20,num21,num22,num23,num24,num25,num26,num27,
                num28,num29,num30,num31]
         #for i in range(0, len(number)):
                  # number[i0] = int(number[i])

         #number=list(map(int,number))
         print(type(number))
         print(number)
         item_name=["Regular Bite","Premium Bites Pizza", "Veggie Delight Pizza","Exotic Veggie Bite","Turkey club Salad","Taco Salad" ,"Spinach Berry Salad","Pineapple Boat Salad","Mojito",
               "Martini", "Manhattan", "Gin tonic", "Key lime pie","Lemon Cake","Cheese Cake","Texas Choclate Cake","Chilly Paneer","Veg Manchurian","Honey Chilly Potato",
               "Vegetable Spring Roll","Cheese and Garlc Bread","Paneer Tikka Tandoori","Paneer Malai Tikka","Soya Malai Chaap","Stuffed Mushroom Tikka","Mushroom Malai Tikka",
               "Veg. Noodles","Egg Soft Noodles","Chicken Soft Noodles","Prawns Noodles","Szechwan Noodles"]
         #submission()
         print(session.user)
         today=date.today()
         print(today)
         order=Order(cust_name=session.user,date=today)
         db.session.add(order)
         db.session.commit()
         results=db.session.query(Customer).filter(Customer.c_uname.in_([session.user])).first()
         db.session.commit()
         if not results:
            cname=db.session.query(Sign.name).filter(Sign.user_name==session.user).first()
            cnum=db.session.query(Sign.number).filter(Sign.user_name==session.user).first()
            cadd=db.session.query(Sign.address).filter(Sign.user_name==session.user).first()
            cmail=db.session.query(Sign.mail).filter(Sign.user_name==session.user).first()
            cuname=db.session.query(Sign.user_name).filter(Sign.user_name==session.user).first()
            db.session.commit()
            customer=Customer(c_name=cname,c_number=cnum,c_address=cadd,c_mail=cmail, c_uname=cuname,r_orderid=order.order_id, datee=order.date)
            db.session.add(customer)
            db.session.commit()
         else:
            x=db.session.query(Customer).filter(Customer.c_uname==session.user).first()
            x.r_orderid=order.order_id
            x.datee=order.date

         for i,j in zip(number,item_name):
             if i!=None and i!='0':
                print(i,j)
                print(type(i))
                price1=int(getattr(db.session.query(Menu.price).filter(Menu.food_item==j).first(),'price'))
                #price1._asdict()
                db.session.commit()
                print("Price 1 original",price1)
                print("Type of Price 1 original",type(price1))
                print("i value int type",int(i))
                price2=price1
                total=int(i)*int(price2)
                print(total)
                cart=Cart(order_id=order.order_id,food_item=j, price=price1,tprice=total,quantity=i)
                #db.session.query(Order, Cart).filter(Order.order_id == Cart.order_id)
                db.session.add(cart)
                db.session.commit()
                flash("Item added successfully,proceed to checkout to confirm your order.")
             elif i=='none'or i=='0':
                continue
             else:
                continue
@app.route("/acc_detail", methods=['GET','POST'])
def acc_detail():
    if request.method=='POST':
        add= request.form.get('ad')
        print(add)
        x=db.session.query(Customer).filter(Customer.c_uname==session.user).first()
        x.c_address=add
        flash("Successfully Updated")
    customern=db.session.query(Customer.c_name).filter(Customer.c_uname==session.user).first()[0]
    num=db.session.query(Customer.c_number).filter(Customer.c_uname==session.user).first()[0]
    email=db.session.query(Customer.c_mail).filter(Customer.c_uname==session.user).first()[0]
    address=db.session.query(Customer.c_address).filter(Customer.c_uname==session.user).first()[0]
    date=db.session.query(Customer.datee).filter(Customer.c_uname==session.user).first()[0]
    orderid=db.session.query(Customer.r_orderid).filter(Customer.c_uname==session.user).first()
    item=db.session.query(Cart).filter(Cart.order_id==orderid).all()
    #quantity=db.session.query(Cart.quantity).filter(Cart.order_id==orderid).all()
    db.session.commit()
    return render_template("account.html",cname=customern,number=num,mail=email,name=session.user,add=address,date=date,item=item )
def send_email():
    from_email="mahimasapra02@gmail.com"
    from_password="2061998@mahi"
    email=db.session.query(Customer.c_mail).filter(Customer.c_uname==session.user).first()[0]
    to_email=email
    subject="Foodmaza: Regarding your food order."
    message="Hello there, \n This is to inform you that this is a <strong>demo project</strong>.\n Hope you enjoyed visiting us. "
    msg=MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)




if __name__ == '__main__':
   app.run(debug = True)
