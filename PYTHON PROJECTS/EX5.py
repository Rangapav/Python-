# AMSTRONG NUMBER IS SAID TO BE THAT IS EQUAL TO SUM OF CUBES OF ITS DIGITS
# FOR EX: 153=(1*1*1)+(5*5*5)+(3*3*3)
#         1*1*1=1
#         5*5*5=125
#         3*3*3=27
#      1+125+27=153
n=int(input("ENTER ANY NUMBER="))
x=len(str(n))
temp=n
sum=0
while temp!=0:
    k=temp%10
    sum+=k**x
    temp=temp//10
if sum==n:
    print(n,"is a armstong number")
else:
    print(n, "is not a armstong number")
