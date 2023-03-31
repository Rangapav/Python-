#BY USING MULTIPLE DISPATCH-WE CAN EXECUTE BOTH METHODS

# import multipledispatch as multipledispatch
# import multipledispatch as dispatch

class Parent:
    # @multipledispatch.dispatch(int,int)
    def m1(self,x,y):
        print(x+y)
class child(Parent):
    # @multipledispatch.dispatch(int,int,int)
    def m1(self,x,y,z):
        print(x+y+z)
ob=child()
# ob.m1(11,22)
ob.m1(11,29,60)

# polymorphism doesn't support method overloading