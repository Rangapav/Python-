#PRIVATE ACCESS MODIFIER/SPECIFIER
# PRIVATE DATA=IT IS SAID TO BE ['__']BEFORE ATTRIBUTE

class Car:
    __companyname="MAHINDRA"
    def f1(self):
        print(self.__companyname)

ob=Car()
ob.f1()
# print(ob.__companyname)
# AttributeError: 'Car' object has no attribute '__companyname'
