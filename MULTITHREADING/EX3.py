import time

def square(n):
    for n in range(10):
        time.sleep(1)
        print("square root values:", n**2)

def cube(n):
    for n in range(10):
        time.sleep(1)
        print("cube root values:", n**3)

initial=time.time()

l=[1,2,3,4,5,6,7,8,9,10]
print("time taken=",time.time()-initial)

square(l)
cube(l)
print("time taken=",time.time()-initial)


