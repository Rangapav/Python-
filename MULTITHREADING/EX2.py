from time import *
from threading import*

# class threading

class Whatsapp(Thread):
    def run(self):
        for i in range(10):
            print("WHATSAPP")
            sleep(1)


class instagram(Thread):
    def run(self):
        for i in range(10):
            print("INSTAGRAM")
            sleep(1)

t1=Whatsapp()
t2=instagram()

t1.start()
sleep(0.1)
t2.start()
