def func():
    l=['apple ','grapes ','mango ','banana ',1 ,2 ,3 ,4 ,5]
    for x in l:
        yield l
p=func()
import sys
s=sys.getsizeof(p)
print("size taken by list=",s)
for y in p:
   print(y)