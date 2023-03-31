n=int(input("ENTER ANY NUMBER="))
x = 0
count=0
for i in range(1000):
    if i%n==0:
        # print(x)
        x=+i
        count+=1
print("SUM OF THE VALUES DIVIDED BY",n,"IS =",x)
print("NO OF DIGITS THAT ARE DIVIDED BY",n,"IS =",count)
print("AVERAGE OF THE VALUES DIVIDED BY=",x/count)
