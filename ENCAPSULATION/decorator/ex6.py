def func1(n):
    def func2():
        a=n()
        return  250+ a
    return func2
@func1
def func3():
        return 250
# p=func1(func3)
# print(p())
print(func3())


