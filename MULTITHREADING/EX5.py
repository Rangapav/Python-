import time
import threading

def square(n):
    for n in range(10):
        time.sleep(1)
        print("square root values:", n**2)

def cube(n):
    for n in range(10):
        time.sleep(3)
        print("cube root values:", n**3)

initial=time.time()
l=[1,2,3,4,5,6,7,8,9,10]


t1 = threading.Thread(target=square, args=(l,))
ob=threading.Thread(target=cube, args=(l,))

ob.start()
time.sleep(1)
t1.start()

print("Time taken=",time.time()-initial)
