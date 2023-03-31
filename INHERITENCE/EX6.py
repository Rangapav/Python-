class teacher:
    def __init__(self,fname,lname,salary,address,mobileno,pincode,dealingsubject,experience):
        self.fname=fname
        self.lname=lname
        self.sal=salary
        self.adr=address
        self.mno=mobileno
        self.pin=pincode
        self.dealsub=dealingsubject
        self.exp=experience
        print("TEACHER FIRST NMAE=",self.fname,'\n',"LAST NAME=",self.lname,'\n'"SALARY=",self.sal,'\n'"ADDRESS=",self.adr,'\n'"MOBILE NO=",self.mno,'\n'"PINCODE=",self.pin,'\n'"DEALING SUBJECT=",self.dealsub,'\n'"EXPERIENCE=",self.exp,'\n''\n')
class student(teacher):
    def f1(self,fname,lname,address,mobileno,pincode,idcard,fees,standard):
        self.id=idcard
        self.fee=fees
        self.std=standard
        print("STUDENT F NAME=",self.fname,'\n'"ADDRESS=",self.adr,'\n'"MOBILE-NO=",self.mno,'\n'"L NAME=",self.lname,'\n'"FEES=",self.fee,'\n'"ROLL-NO=",self.id,'\n'"STANDARD=",self.std)
# teacher("pavan","kalyan","500000","marthahalli","996978834","560037","maths","10+years")
obj1=student("pavan","kalyan","34500","marthahalli","996978834","560037","maths","10+years")
obj1.f1("pavan","kalyan","marthahalli","996978834","560037","34","560037","10th std")