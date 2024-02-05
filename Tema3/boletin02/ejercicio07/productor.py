import random
from threading import *
import time


class Productor(Thread):

    def __init__(self, nombre, cola, cond):
      Thread.__init__(self, name=nombre)
      self.cola=cola
      self.cond=cond

    def run(self):
       
       while True:
        cadena="objeto"
        with self.cond:
            #tenemos que saber si la cola está vacía antes de poder añadir algo.
            while self.cola.full():
               print("Cola llena")
               self.cond.wait()#hacemos que la cola espere.
            self.cola.put(cadena) #si la cola está vacía pues llenamos la cola.
            
        print("Hilo", self.name, "produciendo...")
        time.sleep(random.randint(1,5))
        print ("Hilo", self.name, "ha terminado de producir")
        with self.cond:
          self.cond.notifyAll()