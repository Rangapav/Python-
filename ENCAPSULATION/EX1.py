#ENCAPSULATON IS SAID TO BE BINDING OF CLASSES ,ATTRIBUTES,METHODS AT ONE PLACE
# THERE ARE 3 TYPES OF ENCAPSULATION
# 1)PUBLIC,2)PROTECTED AND 3)PRIVATE

# 1) PUBLIC SPECIFIER-IT CAN ACCESS ANY WHERE IN THE PROGRAM

class Laptop:
    price=100000
    def f1(self):
        print(self.price)

ob=Laptop()
ob.f1()
print(ob.price)