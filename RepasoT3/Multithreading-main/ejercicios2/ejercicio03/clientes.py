from threading import Thread, Semaphore
import time
import random

class Carniceria(Thread):
    semaforo = Semaphore(4)

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
    
    def run(self):
        print("El cliente", self.name, "ha entrado en la carnicería")
        Carniceria.semaforo.acquire()
        print("El cliente", self.name, "está siendo atentido")
        time.sleep(random.randint(1,10))
        print("El cliente", self.name, "ha terminado en la carnicería")
        Carniceria.semaforo.release()  