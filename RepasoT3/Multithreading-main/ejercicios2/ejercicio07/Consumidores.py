from threading import Thread
from multiprocessing import Queue
import time
import random

class Consumismo(Thread):
    def __init__(self, nombre, cond, cola:Queue):
        Thread.__init__(self, name=nombre)
        self.cond = cond
        self.cola = cola

    def run(self):
        while True:
            self.cond.acquire()
            while self.cola.qsize() <= 0 : #Si la cadena está vacía, esperamos a que se llene
                self.cond.wait()
            print("Consumidor", self.name, "está comprando un producto")
            self.cola.get() #Una vez consigamos acceder, tomamos el primer elemento disponible

            time.sleep(random.randint(3,5))
            print("Consumidor", self.name, "ya ha cogido el producto")
            self.cond.notifyAll()
            self.cond.release()
