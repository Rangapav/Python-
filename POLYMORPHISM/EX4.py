class Parent:
    def m1(self,x,y):
        print(x+y)
class child(Parent):
    def m1(self,x,y,z):
        print(x+y+z)
    def m2(self):
        super().m1(10,30)
ob=child()
ob.m1(10,20,70)
ob.m2()