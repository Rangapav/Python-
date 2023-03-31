from abc import ABC,abstractmethod

class laptop(ABC):
    @abstractmethod
    def name(self):
        pass                     #abstract class work as blue print for another classes
    @abstractmethod
    def generation(self):
        pass
    def conc(self):    #~~~~this is concrete method
        print("this is good computer")

class lenovo(laptop):
    def name(self):
        print("company name=lenovo")
    def generation(self):
        print("5th generation")
class apple(laptop):
    def name(self):
        print("company name=apple")

    def generation(self):
        print("6th generation")

ob=lenovo()
ob.name()
ob.generation()
ob.conc()
ob1=apple()
ob1.name()
ob1.generation()
ob1.conc()

