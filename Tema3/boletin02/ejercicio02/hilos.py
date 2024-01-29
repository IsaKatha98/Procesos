from threading import *
import random
import time

class Panadería(Thread):
    semaforo= Semaphore()
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run (self):
        
        print ("El hilo", self.name, "está esperando.")
        Panadería.semaforo.acquire()
        print("Hilo",self.name, "está siendo atendido.")
        time.sleep(random.randint(1,5))
        #soltamos la caja.
        print("El hilo",self.name, "recoge la compra y se va.")
        Panadería.semaforo.release
        

        