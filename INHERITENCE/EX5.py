#HYBRID INHERITENCE

class grandparent():
    def p1(self):
        print("pavan")
class parent1(grandparent):
    def p2(self):
        print("kalyan")
class parent2:
    def p3(self):
        print("yadav")
class child(parent1,parent2):
    def p4(self):
        print("pavan")

ob=child()
ob.p1()
ob.p2()
ob.p3()
ob.p4()