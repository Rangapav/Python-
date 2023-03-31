l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def func(l):
    if l%2==0:
        return l**2
def func2(l):
    if l%2==1:
        return l**3
p=map(func,l)
print(set(p))
s=map(func2,l)
print(set(s))