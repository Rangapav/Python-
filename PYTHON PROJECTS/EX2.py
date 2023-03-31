# FIBANOCI SERIES

# n=int(input("ENTER ANY NUMBER="))
# n1,n2=0 ,1
# sum=0
# if n<=0:
#     print("ENTER THE NUMBER GREATER THAN 0")
# else:
#     for i in range(n):
#         print(sum ,end=" ")
#         n1=n2
#         n2=sum
#         sum=n1+n2

n=int(input("ENTER ANY NUMBER="))
first=0
second=1
for i in range(n):
   print(first,end=" ")
   temp=first
   first=second
   second=temp+second