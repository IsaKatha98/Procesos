from threading import Semaphore, Thread
import time
import random

class Panaderia(Thread):

    def __init__(self, nombre, semaforo:Semaphore):
        Thread.__init__(self, name=nombre)
        self.semaforo = semaforo

    def run(self):
        print("Entra un muerto de hambre llamado", self.name, "en la panadería")
        self.semaforo.acquire()
        print("El muerto de hambre", self.name, "está siendo atendido")
        time.sleep(random.randint(1,3))
        print("El muerto de hambre", self.name, "ha comprado pan y se va")
        self.semaforo.release()