#2)METHOD OVER-RIDDING
# DIFFRERENT CLASSES WITH SAME METHOD,WITH DIFFERENT SIGNATURES/PARAMETERS
# IT IS A EXAMPLE OF RUNTIME ERROR IN POLYMORPHISM

class Parent:
    def m1(self):
        print("pavan kalyan")
class Child(Parent):
    def m1(self):
        print("this is child class")
    def m2(self):
        super().m1()

ob=Child()
ob.m1()
ob.m2()

