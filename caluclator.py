#simple clauclator
print("select an operator to work")
print("1. add")
print("2. subtract")
print("3.multiplication")
print("4.divide")
print("5.percent")

operation=str(input("ENTER ANY NUMBER="))
if operation=="1":
    num1=int(input("Enter the first value="))
    num2=int(input("enter second value="))
    print("sum is="+ str(int(num1) + int(num2)))
if operation=="2":
    num1=int(input("Enter the first value="))
    num2=int(input("enter second value="))
    print("difference is="+ str(int(num1) - int(num2)))
elif operation=="3":
    num1=int(input("Enter the first value="))
    num2=int(input("enter second value="))
    print("multiplication is="+ str(int(num1) * int(num2)))
elif operation == "4":
        num1 = int(input("Enter the first value="))
        num2 = int(input("enter second value="))
        print("division is="+ str(int(num1) / int(num2)))
elif operation=="5":
    num1=int(input("Enter the first value="))
    num2=int(input("enter second value="))
    print("Remainder is="+ str(int(num1) %  int(num2)))
else:
    print("invalid number")
