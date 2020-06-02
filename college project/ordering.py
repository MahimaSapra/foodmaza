from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, url_for,redirect, flash
from sqlalchemy.orm import session
import itertools

ordering=Flask(__name__)
ordering.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/foodmaza'
ordering.secret_key='dont tell anyone'
db=SQLAlchemy(ordering)
class Menu(db.Model):
    __tablename__= 'foodmaza_menu'
    id=db.Column(db.Integer, primary_key=True)
    food_item=db.Column(db.String(100))
    price=db.Column(db.Integer)
    def __init__(self, food_item, price):
        self.food_item=food_item
        self.price=price
class Order(db.Model):
    __tablename__="order_table"
    id=db.Column(db.Integer, primary_key=True)
    food_item=db.Column(db.String(100))
    price=db.Column(db.Integer)
    tprice=db.Column(db.Integer)
    quantity= db.Column(db.String(100))
    def __init__(self, food_item, price, tprice,quantity):
        self.food_item=food_item
        self.price=price
        self.tprice=tprice
        self.quantity=quantity

def get_data():
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
              # number[i] = int(number[i])

     #number=list(map(int,number))
     print(type(number))
     print(number)


     item_name=["Regular Bite","Premium Bites Pizza", "Veggie Delight Pizza","Exotic Veggie Bite","Turkey club Salad","Taco Salad" ,"Spinach Berry Salad","Pineapple Boat Salad","Mojito",
           "Martini", "Manhattan", "Gin tonic", "Key lime pie","Lemon Cake","Cheese Cake","Texas Choclate Cake","Chilly Paneer","Veg Manchurian","Honey Chilly Potato",
           "Vegetable Spring Roll","Cheese and Garlc Bread","Paneer Tikka Tandoori","Paneer Malai Tikka","Soya Malai Chaap","Stuffed Mushroom Tikka","Mushroom Malai Tikka",
           "Veg. Noodles","Egg Soft Noodles","Chicken Soft Noodles","Prawns Noodles","Szechwan Noodles"]

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
            order=Order(food_item=j, price=price1,tprice=total,quantity=i)
            db.session.add(order)
            db.session.commit()
            flash("Item added successfully,proceed to checkout to confirm your order.")
         elif i=='none'or i=='0':
            continue
         else:
            continue
