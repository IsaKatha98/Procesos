import random
from threading import *
import time
from main import cond, cola

class Consumidor(Thread):

    def __init__(self, nombre):
      Thread.__init__(self, name=nombre)

    def run(self):
       while True:
        cadena="objeto"
        with cond:
            while cola.empty():
                print("Cola vacía")
                cond.wait()
            cadena= cola.get() #lo quitamos de la cola
        print(self.name,"está recogiendo el objeto...")
        cond.notifyAll()
        print (self.name, "ya ha recogido todo")
