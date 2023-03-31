import mysql.connector


x = mysql.connector.connect(host='localhost', user='root', password='Pavan@123',database='laptops')

db=x.cursor()
# db1='update models set companyname="acer" where companyname="16gb"'
# db.execute('select * from models')
# p=db.fetchall()
# for i in p:
#     print(i)
m='delete from models where no=1'
db.execute(m)
print(db)
x.commit()