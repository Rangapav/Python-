#2)PROTECTED DATA,PROTECTED ACCESS SPECIFIER
# IT IS CASE SENSITIVE
# IT IS USED BY PUTTING['_']IN FRONT OF ATTRIBUTE

class Laptop:
    _price=100000
    _generation="5th"
    def f1(self):
        print("PRICE=",self._price,'\n'"GENERATION=",self._generation)
class Lenovo(Laptop):
    def f2(self):
        print("PRICE=", self._price, '\n'"GENERATION=", self._generation)

ob=Lenovo()
ob.f1()
ob.f2()

