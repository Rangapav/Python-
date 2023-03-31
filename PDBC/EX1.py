import mysql.connector


x = mysql.connector.connect(host='localhost', user='root', password='Pavan@123')
if x.is_connected():
    print("connected")
else:
    print("does not connected")

