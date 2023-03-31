# DECORATOR: A DECORATOR TAKES A FUNCTION AND ADD SOME FUNCTIONALITY AND RETURNS IT.....

def func1(n):
    def func2():
        a=n()
        return  250+ a
    return func2
@func1
def func3():
        return 250
@func1
def func4():
    return 1000
# x=func1(func3)
# print(x())
print(func3())
print(func4())


