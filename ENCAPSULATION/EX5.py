#NAMES MANGLING:-IT IS SAID TO BE ATLEAST TWO UNDERSCORES BEFOTE ATTRIBUTE AND ALMOST TRAILING BY ONE undersocre

class Parent:
    _a=100
    __b=200
    ___c_=300
    ____d=500
    __e__=600
    ____f__=700
    _____g=1000

print(dir(Parent))

ob=Parent()
print(ob._a)
print(ob._Parent__b)
print(ob._Parent___c_)
print(ob._Parent____d)
print(ob.__e__)
print(ob.____f__)
print(ob._Parent_____g)