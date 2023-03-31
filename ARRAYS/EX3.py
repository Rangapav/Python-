from numpy import *

x=matrix('1,2,3;1,2,3;1,2,3')
y=matrix('1,2,3;1,2,3;1,2,3')
z=matrix('0,0,0;0,0,0;0,0,0')
# print(x)
# print(y)
# print("addition=",x+y)
# print("subtraction=",x-y)
# print("product=",x*y)
# print("division=",x/y)

for i in range(len(x)):
    for j in range(len(y[0])):
     z[i][j]=x[i][j]+y[i][j]
# for z in r:
print(z)