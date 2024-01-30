import random
from threading import *
import time
from main import cond, cola

class Productor(Thread):

    def __init__(self, nombre):
      Thread.__init__(self, name=nombre)

    def run(self):
       
       while True:
        cadena="objeto"
        with cond:
            #tenemos que saber si la cola está vacía antes de poder añadir algo.
            while cola.full():
               print("Cola llena")
               cond.wait()#hacemos que la cola espere.
            cola.put(cadena) #si la cola está vacía pues llenamos la cola.
            
        print("Hilo", self.name, "produciendo...")
        time.sleep(random.randint(1,5))
        print ("Hilo", self.name, "ha terminado de producir")
        cond.notifyAll()