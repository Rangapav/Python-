def func():
    for i in range(1,20):
        if i%2==1:
            yield i**2
        else:
             yield i**3
p=func()
for x in p:
   print(x)