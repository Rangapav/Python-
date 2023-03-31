# decarator is said to be wrap another function in order to extend the behaviour of wrapped function
# decarator are used to modify the behaviour of function or class
# In decarators, functions are taken as the argument in to another function and then called inside the wraper function
def func1(n):
    def func2():
        x=n()
        return x+"  kalyan"
    return func2
@func1
def func3():
    return  "pavan"
# p=func1(func3)
# print(p())
print(func3())