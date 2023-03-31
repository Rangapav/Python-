#INHERITENCE IAS SAID TO BE AQUIRINIG PROPERTIES FROM ONE CLASS TO ANOTHER CLASS
# PARENT CLASSS IS SUPERCLASS
# CHILD CLASS IS CALLED SUBCLASS
# 1>SINGLE INHERITENCE

class parent:
    def p1(self):
        print("pavan")
class child(parent):
    def p2(self):
        print("kalyan")
ob=child()
ob.p1()
ob.p2()