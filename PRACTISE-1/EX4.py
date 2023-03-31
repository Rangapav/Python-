# for row in range(6):
#     for col in range(7):
#         if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
#             print("ram",end=" ")
#         else:
#             print(end="    ")
#     print()
#

n=int(input("ENTER NO OF ROWS="))
x=ord('p')
for i in range(n):
    for j in range(i+1):
       print(chr(x),end=" ")
       x=x+1
    print()

