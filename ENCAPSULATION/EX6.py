class Car:
    carname="Mahindra"
    _price=1000000
    __series="10th series"
    x="THIS CAR IS BEAUTIFUL"
    def f1(self):
        print("carname=",self.carname,'\n'"price=",self._price,'\n'"series=",self.__series)
class Mahindra(Car):
    def f2(self):
        print("carname=",self.carname,'\n'"price=",self._price,'\n'"series=",self._Car__series)

ob=Mahindra()
ob.f1()
print(ob.x,'\n')
ob.f2()
print(ob.x)
