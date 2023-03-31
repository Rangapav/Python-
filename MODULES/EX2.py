from EX1 import addition,substraction
from EX3 import multiplication,division

a=int(input("Enter any number="))
b=int(input("Enter any number="))
n=int(input("Enter any number ="))

if n==1:
    print(addition(a,b))
elif n==2:
    print(substraction(a,b))
elif n==3:
    print(multiplication(a,b))
elif n==4:
    print(division(a,b))
else:
   print ("you have not given correct number")