#HIERARICAL INHERITERNCE

class grandparent():
    def p1(self):
        print("pavan")
class parent1(grandparent):
    def p2(self):
        print("kalyan")
class parent2(grandparent):
    def p3(self):
        print("yadav")
ob=parent1()
ob.p1()
ob.p2()
ob1=parent2()
ob1.p1()
ob1.p3()