def f1(n):
    def func2():
        a=n()
        for i in range(1,11):
            yield a*i,'=',a,'*',i
    return func2()
@f1
def f3():
    return x
x=int(input("enter any number="))
# print(f3)
# for x in f3:
#     print(x)



