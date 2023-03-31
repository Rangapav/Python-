#Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user.
from abc import ABC,abstractmethod
class Mobile(ABC):
    @abstractmethod
    def camera(self):
        print("this is iphone camera")

OB=Mobile()
OB.camera()

# TypeError: Can't instantiate abstract class Mobile with abstract method camera

