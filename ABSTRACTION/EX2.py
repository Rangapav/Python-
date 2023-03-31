from abc import ABC,abstractmethod
class Mobile(ABC):
    @abstractmethod
    def camera(self):
        pass

    @abstractmethod
    def ram(self):
        pass

class iphone(Mobile):
    def camera(self):
        print("this is iphone camera")

    def ram(self):
        print("ram=4gb")


class infinix(Mobile):
    def camera(self):
        print("this is inifinix camera")

    def ram(self):
        print("ram=6gb")


ob=iphone()
ob.camera()
ob.ram()
ob1=infinix()
ob1.camera()
ob1.ram()