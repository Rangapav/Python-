l=[int(input("ENTER ANY NUMBER="))]
def func(n):
    for i in range (1,100):
       yield i**n

p=map(func,l)
for x in p:
    print(list(x))

