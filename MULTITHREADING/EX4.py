import time
def double(num):
    print('Double numbers:')
    for i in num:
        time.sleep(0.2)
        print('square of i:',i**2)

def triple(num):
    print('Triple numbers:')
    for i in num:
        time.sleep(0.2)
        print('cube values:',i**3)

Time=time.time()
l=[1,2,3,4,5,6]

double(l)
triple(l)

# print('time taken:',time.time()-Time)