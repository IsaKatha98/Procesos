import random
from threading import *

class Consumidor(Thread):

    def __init__(self, nombre, cola, cond):
      Thread.__init__(self, name=nombre)
      self.cola=cola
      self.cond=cond

    def run(self):
       while True:
        cadena="objeto"
        with self.cond:
            while self.cola.empty():
                print("Cola vacía")
                self.cond.wait()
            cadena= self.cola.get() #lo quitamos de la cola
        print(self.name,"está recogiendo el objeto...")
        with self.cond:
            self.cond.notifyAll()
            print (self.name, "ya ha recogido todo")
