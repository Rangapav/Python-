
# def f1(n):
#     # num = 1
#     for i in range(0, n):
#         num = 1
#         for j in range(0, i + 1):
#             print(num, end="  ")
#             num = num + 1
#         print('\r')
#
#
# n = int(input("enter any number="))
# f1(n)

x=int(input("enter any character="))
for i in range(x):
    for j in range(i,-1,-1):
        print(j+1,end=" ")
    print('\r')