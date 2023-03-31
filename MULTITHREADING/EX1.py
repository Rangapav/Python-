#MULTITHREADING IS SAID TO BE IT PERFORM MULTIPLE TASKS SIMULTANEOUSLY

import threading


t1=threading.currentThread().getName()
print(t1)
# <_MainThread(MainThread, started 9404)>
# MainThread
t2=threading.main_thread().getName()
print(t2)