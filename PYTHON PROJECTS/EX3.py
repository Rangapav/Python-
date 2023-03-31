# TO FIND PRIME NUMBER
# n=int(input("ENTER ANY NUMBER="))
# for i in range(2,n):
#     if (n%i)==0:
#         print(n,"is NOT a primenumber")
#         break
# else:
#         print(n,"IS A PRIME NUMBERS")

# f=int(input("ENTER STARTING VALUE="))
# e=int(input("ENTER THE ENDING VALUE="))
# for i in range(f,e):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#      print(i,end=" ")

for i in range(0,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)