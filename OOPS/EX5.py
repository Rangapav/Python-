#USING TWO METHODS IN INIT

class car:
    def __init__(self,price,color,roofavailable,mailage,speed,brand,seatings):
        self.mrp=price
        self.color=color
        self.roofavail=roofavailable
        self.mail=mailage
        self.sp=speed
        self.br=brand
        self.seat=seatings
    def display(self):
        print("car price=", self.mrp, '\n'"CAR COLOR=", self.color, '\n'"ROOF AVAIALBLE=", self.roofavail, '\n'"MAILAGE=",
              self.mail, '\n'"CAR SPEED=", self.sp, '\n'"CAR BRAND=", self.br, '\n'"SEATS=", self.seat, '\n')
        

ob=car("200k","blue","available","50km","200km/hr","tata",4)
ob.display()
