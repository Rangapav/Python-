import mysql.connector


x = mysql.connector.connect(host='localhost', user='root', password='Pavan@123',database='laptops')

db=x.cursor()
data="Insert into models(no, companyname, generation,ram,rom) values (%s, %s,%s,%s,%s)"
stu =[(1,'lenovo','5thgeneration','4gb','6gb'),(2,'dell','4thgeneration','8gb','264gb'),(3,'apple','6thgeneration','12gb','568gb')]
db.executemany(data,stu)
print(db)

x.commit()

