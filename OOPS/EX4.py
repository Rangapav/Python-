#DECLARING USING OBJECT CREATION in init method

class car:
    def __init__(self,price,color,roofavailable,mailage,speed,brand,seatings):
        self.mrp=price
        # init variable
        self.color=color
        self.roofavail=roofavailable
        self.mail=mailage
        self.sp=speed
        self.br=brand
        self.seat=seatings
ob=car("200k","blue","available","50km","200km/hr","tata",4)
print("car price=",ob.mrp,'\n'"CAR COLOR=",ob.color,'\n'"ROOF AVAIALBLE=",ob.roofavail,'\n'"MAILAGE=",ob.mail,'\n'"CAR SPEED=",ob.sp,'\n'"CAR BRAND=",ob.br,'\n'"SEATS=",ob.seat,'\n')
ob1=car("300k","white","available","40km","200km/hr","mahindra",5)
print("car price=",ob1.mrp,'\n'"CAR COLOR=",ob1.color,'\n'"ROOF AVAIALBLE=",ob1.roofavail,'\n'"MAILAGE=",ob1.mail,'\n'"CAR SPEED=",ob1.sp,'\n'"CAR BRAND=",ob1.br,'\n'"SEATS=",ob1.seat)