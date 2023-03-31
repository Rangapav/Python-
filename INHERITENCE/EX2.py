#MULTILEVEL INHERITENCE

class grandparent:
    def p1(self):
        print("ranga")
class parent(grandparent):
    def p2(self):
        print("pavan")
class child(parent):
    def p3(self):
        print("kalyan")

ob=child()
ob.p1()
ob.p2()
ob.p3()