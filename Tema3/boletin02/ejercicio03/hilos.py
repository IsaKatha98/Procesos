from threading import *
import random
import time;
class Carniceria (Thread):
    #declaramos un semáforo
    semaforo=Semaphore(4)
    
    def __init__(self, nombre):
      Thread.__init__(self, name=nombre)

    def run(self):

       print("Llega el cliente", self.name)
       Carniceria.semaforo.acquire()
       print("El ", self.name," está siendo atendido.")
       time.sleep(random.randint(1,10))
       Carniceria.semaforo.release()
       print("El", self.name, "se va.")
                 
            
          