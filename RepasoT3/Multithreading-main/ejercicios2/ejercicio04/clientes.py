from threading import Thread, Semaphore
import time
import random

class Carniceria(Thread):
    semaforoCarniceria = Semaphore(4)
    semaforoCharcuteria = Semaphore(2)

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
    
    def run(self):
        attCarniceria = False
        attCharcuteria = False
        while not (attCarniceria and attCharcuteria): 

            if Carniceria.semaforoCarniceria._value > 0 and not attCarniceria:
                Carniceria.semaforoCarniceria.acquire()
                print("El cliente", self.name, "ha entrado en la carnicería")
                print("El cliente", self.name, "está siendo atentido en la carnicería")
                time.sleep(random.randint(1,10))
                print("El cliente", self.name, "ha terminado en la carnicería")
                attCarniceria = True
                Carniceria.semaforoCarniceria.release()  

            elif Carniceria.semaforoCharcuteria._value > 0 and not attCharcuteria: 
                Carniceria.semaforoCharcuteria.acquire()
                print("El cliente", self.name, "ha entrado en la charcutería")
                print("El cliente", self.name, "está siendo atentido en la charcutería")
                time.sleep(random.randint(1,10))
                print("El cliente", self.name, "ha terminado en la charcutería")
                attCharcuteria = True
                Carniceria.semaforoCharcuteria.release()

        print("El cliente", self.name, "se va a su casa")  
            
        