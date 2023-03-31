import functools
l=[1,2,3,4,5,6,7,8,9,10]
print(functools.reduce (lambda x,y:x+y,l))

print(list(map(lambda x:x**2 if x%2==0 else x**3, range(0,200))))

# lambda function=a lambda function is anonymus function
# A lambda can take no of arguments in only one function


