print(list(map(lambda n:n**2 if n%2==0 else n**3, range(0,20))))
x=lambda n:n**2 if n%2==0 else n**3
n=int(input("ENTER ANY NUMBER="))
print(x(n))
