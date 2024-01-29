import random
from threading import *
import time

class Carniceria (Thread):
    carniceria=Semaphore(4)
    charcuteria=Semaphore(2)
  

    def __init__(self, nombre):
      Thread.__init__(self, name=nombre)

    def run(self):
        pasaCarniceria=False
        pasaCharcuteria=False

        print("Llega el cliente", self.name)
        while not pasaCarniceria or not pasaCharcuteria:
            if Carniceria.carniceria._value>0 and not pasaCarniceria:
      
                Carniceria.carniceria.acquire()
                pasaCarniceria=True
                print("El cliente", self.name, "está siendo atendido en la carnicería.")
                time.sleep(random.randint(1,10))
                print("El cliente", self.name, "ha terminado en carnicería.")
                Carniceria.carniceria.release()

            if Carniceria.charcuteria._value>0:

                Carniceria.charcuteria.acquire()
                pasaCharcuteria=True
                print("El cliente", self.name, "está siendo atendido en la charcutería.")
                time.sleep(random.randint(1,5))
                print("El cliente", self.name, "ha terminado en charcutería.")
                Carniceria.charcuteria.release()
