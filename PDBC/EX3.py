import mysql.connector


x = mysql.connector.connect(host='localhost', user='root', password='Pavan@123',database='laptops')
db = x.cursor()

print(db)
# db.execute('create database laptops')
db.execute("create table models(sno int,companyname varchar(50),generation varchar(50),ram varchar(30),rom varchar(30))")