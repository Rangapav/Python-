# GENERATOR IS USED TO GENERATE SEQUENCE OF ARGUMENTS/NUMBERS
# YIELD IS A KEYWORD USED FOR GENERATOR
#YIELD TAKE LESS MEMORY SIZE COMPARE TO RETURN


def func(n):
    l=[]
    for i in range(1,11):
        l.append(f'{n}*{i}={n*i}')
    return l
n=int(input("enter any number="))
p=func(n)
import sys
s=sys.getsizeof(p)
print("size taken=",s)
for i in p:
    print(i)