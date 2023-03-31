def func(n):
    l=[]
    for i in range(1,11):
        l.append(f'{n}*{i}={n*i}')
    yield l
n=int(input("enter any number="))
p=func(n)
import sys
s=sys.getsizeof(p)
print("size taken=",s)
for i in p:
    print(i)