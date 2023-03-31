#MULTIPLE INHERITENCE

class parent1():
    def p1(self):
        print("pavan")
class parent2:
    def p2(self):
        print("kalyan")
class child(parent1,parent2):
    def p3(self):
        print("yadav")

ob=child()
ob.p1()
ob.p2()
ob.p3()