from threading import *
import random
import time

class Panadería(Thread):
    lock=Lock()
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run (self):
        
        print ("El ", self.name, "está esperando.")
        Panadería.lock.acquire()
        print("El",self.name, "está siendo atendido.")
        time.sleep(random.randint(1,5))
        #soltamos la caja.
        Panadería.lock.release()
        print("El ",self.name, "recoge la compra y se va.")
       
        

        