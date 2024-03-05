from threading import Thread, Semaphore
import time
import random

class Mostrador(Thread):
    semaforo = Semaphore(4)

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
    
    def run(self):
        print("El cliente", self.name, "ha entrado en la panadería")
        Mostrador.semaforo.acquire()
        print("El cliente", self.name, "está en el mostrador")
        time.sleep(random.randint(1,5))
        print("El cliente", self.name, "ya ha comprado su pan y se va")
        Mostrador.semaforo.release()  