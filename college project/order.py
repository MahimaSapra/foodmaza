from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, url_for,redirect, flash
from sqlalchemy.orm import session, join,  relationship
from sqlalchemy import ForeignKey
from app import Sign
order=Flask(__name__)
order.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/foodmaza'
order.secret_key='dont tell anyone'
db=SQLAlchemy(order)
class Order(db.Model):
    __tablename__= 'order'
    order_id=db.Column(db.Integer, primary_key=True)
    cust_name=db.Column(db.String(100),ForeignKey('sign.name') )
    sign=db.relationship('Cart',backref='order')
    cust=db.relationship('Customer',backref='order')
    def __init__(self,cust_name):
        self.cust_name=Sign.name

class Cart(db.Model):
    __tablename__="cart"
    id=db.Column(db.Integer, primary_key=True)
    order_id=db.Column(db.Integer, ForeignKey('Order.order_id'))
    food_item=db.Column(db.String(100))
    price=db.Column(db.Integer)
    tprice=db.Column(db.Integer)
    quantity= db.Column(db.String(100))
    def __init__(self, food_item, price, tprice,quantity):
        self.food_item=food_item
        self.price=price
        self.tprice=tprice
        self.quantity=quantity
class Customer(db.Model):
        __tablename__="customer_data"
        id=db.Column(db.Integer, primary_key=True)
        c_name=db.Column(db.String(100), ForeignKey('Sign.name'))
        c_number=db.Column(db.String(100),ForeignKey('Sign.number'))
        c_address=db.Column(db.String(100),ForeignKey('Sign.address'))
        c_mail=db.Column(db.String(100),ForeignKey('Sign.mail'))
        c_uname=db.Column(db.String(100), ForeignKey('Sign.user_name'))
        r_orderid=db.Column(db.Integer, ForeignKey('Order.order_id'))

        def __init__(self,c_name,c_number,c_address,c_mail, c_uname, r_orderid):
            self.c_name=Sign.name
            self.c_number=Sign.number
            self.c_address=Sign.address
            self.c_mail=Sign.mail
            self.c_uname=Sign.user_name
            self.r_orderid=Order.order_id
