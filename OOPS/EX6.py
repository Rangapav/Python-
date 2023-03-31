#STATIC VARIABLE IS DEFINED AS THE VARIABLE INSIDE THE CLASS AND OUTSIDE THE METHOD CALLED CLASS VARIABLE/STATIC VARIABLE

class car:
    price = "200"
    COLOR = "blue"
    ROOFAVAILABLE = "available"
    MAILAGE = "50 km"
    SPEED = "200km / hr"
    BRAND = "tata"
    def m1(self):
        print("THIS CAR IS IN GOOD CONDITION",'\n')
ob=car()
print("car price=",ob.price,'\n'"CAR COLOR=",ob.COLOR,'\n'"ROOF AVAIALBLE=",ob.ROOFAVAILABLE,'\n'"MAILAGE=",ob.MAILAGE,'\n'"CAR SPEED=",ob.SPEED,'\n'"CAR BRAND=",ob.BRAND,'\n')
ob.m1()
ob1=car()
print("car price=",ob1.price,'\n'"CAR COLOR=",ob1.COLOR,'\n'"ROOF AVAIALBLE=",ob1.ROOFAVAILABLE,'\n'"MAILAGE=",ob1.MAILAGE,'\n'"CAR SPEED=",ob1.SPEED,'\n'"CAR BRAND=",ob1.BRAND,'\n')
ob1.m1()