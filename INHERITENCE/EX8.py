
class details:
    def __init__(self,firstname,lastname,email,id,address,phonenumber,datejoined):
        self.fname=firstname
        self.lname=lastname
        self.email=email
        self.id=id
        self.address=address
        self.phonenumber=phonenumber
        self.joined=datejoined
    def getfullname(self):
        print(self.fname+''+self.lname)

    def changeaddress(self,newaddress):
        self.address=newaddress
        print('address changed sucessfully')
    def changednumber(self,newnumber):
        self.phonenumber=newnumber

class Teacher(details):
    def __init__(self, firstname, lastname, email, id, address, phonenumber, subjectteaching, salry, datejoined):
        self.subjectteaching=subjectteaching
        self.salary=salry
        details.__init__(self,firstname,lastname,email,id,address,phonenumber,datejoined)

    def getsalry(self):
        print(self.salary)


class student(details):
    def __init__(self,firstname, lastname, email, id, address, phonenumber, subjectlearnrd, fees, datejoined):
        self.subjectlearned=subjectlearnrd
        self.fees=fees
        details.__init__(self, firstname, lastname, email, id, address, phonenumber,datejoined)

    def getfess(self):
        print('student fees:',self.fees)


# ob1=details('pavan','kumar','pavan@gmail',11,'hyd','123123123',10/12/2020)
#  print(ob1)
ob1=Teacher('PAVAN','KALYAN','mohan@',111,'chennai',123456,'maths',12000,12/10/2020)
ob1.getfullname()
ob1.changeaddress('hyd')
ob1.changednumber(12300000)
ob1.getsalry()
