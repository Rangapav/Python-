class school:
    def __init__(self,schoolname,address,mobile,pincode,schoolwebsite):
        self.sname=schoolname
        self.adr=address
        self.mno=mobile
        self.pin=pincode
        self.schoolweb=schoolwebsite
class teacher(school):
    def f1(self,schoolname,address,mobile,pincode,schoolwebsite,fname,lname,salary,dealingsubject,experience):
        self.fname = fname
        self.lname = lname
        self.sal = salary
        self.dealsub = dealingsubject
        self.exp = experience
        print("SCHOOL NAME=",self.sname,'\n'"MOBILE NO=", self.mno,'\n'"PINCODE=",self.pin,'\n'"SCHOOL WEBPAGE=",self.schoolweb,'\n'"TEACHER F NAME=",self.fname,'\n'"L NAME=",self.lname,'\n'"SALARY=",self.sal,'\n'"SUBJECT DEAL=",self.dealsub,'\n'"EXPERIENCE=",self.exp,'\n')

class student(teacher):
    def f2(self,schoolname,address,mobile,pincode,schoolwebsite,fname,lname,fees,idcard,standard):
        self.fee=fees
        self.id=idcard
        self.std=standard
        # def f4(self,fees,idcard,standard):
        print("SCHOOL NAME=",self.sname,'\n'"MOBILE NO=", self.mno,'\n'"PINCODE=",self.pin,'\n'"SCHOOL WEBPAGE=",self.schoolweb,'\n'"STUDENT F NAME=",self.fname,'\n'"L NAME=",self.lname,'\n'"FEES=",self.fee,'\n'"ROLL-NO=",self.id,'\n'"STANDARD=",self.std)
ob=student("schhol","marthahalli","980887969","67989079","www.schools.com")
ob.f1("vvr schol","marthahalli","980887969","67989079","www.schools.com","pavan","kalyan","2000","physics","10+years")
ob.f2("vvr schhol","marthahalli","980887969","67989079","www.schools.com","pavan","kalyan","500000","45","10th std")

