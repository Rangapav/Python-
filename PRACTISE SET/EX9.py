n = int(input("Enter any number= "))
for i in range(n):
    for j in range(i+1):
        print(n-j, end=' ')
    print('\r')



# def f1(n):
#     num = 65
#     for i in range(0,n):
#        for j in range(0,i+1):
#           ch=chr(num)
#           print(ch, end='')
#           num=num+1
#        print('\r')
#
#
# n = (input("Enter any number= "))
# f1(n)