#POLYMORPHISM IS SAID TO BE IN DIFFERENT FORMS
# IT SAID TO BE SAME FUNCTIONS BUT DIFFERENT DIGNATURES
# THERE ARE TWO TYPES OF POLYMORPHISM
# 1)METHOD OVERLOADING
# 2)METHOD OVERRIDING

# 1)METHOD OVERLOADING:-IT IS SAID TO BE ONE CLASS WITH SAME METHOD BUT WITH DIFFERENT PARAMETERS/SIGNATURES
# IT IS SAID TO EXAMPLE OF COMPILE TIME ERROR
# TO EXECUTE BOTH METHODS WE USE MULTIPLE DISPATCH

class Parent:
    def m1(self,x,y):
        print(x+y)
class child(Parent):
    def m1(self,x,y,z):
        print(x+y+z)

ob=child()
ob.m1(10,20,70)
ob.m1(10,20,30)