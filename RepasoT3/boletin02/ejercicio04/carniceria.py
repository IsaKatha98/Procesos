from threading import *
import random
import time

#definimos la clase
class Carniceria(Thread):
    #definimos un semáforo
    semafCarniceria=Semaphore(4)
    semafCharcuteria=Semaphore(2)

    #definimos el constructor
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    #definimos la función que gestiona los hilos
    def run(self):

         #variables booleanas para comprobar si ha pasado por ambas secciones
        pasaCharcuteria=False
        pasaCarniceria=False

        print("El cliente", self.name, "llega a la carniceria")

        #mientras el cliente no haya pasado por ninguna de las secciones
        while not pasaCharcuteria or not pasaCarniceria:

            #si hay dependientes disponibles
            if Carniceria.semafCarniceria._value>0 and not pasaCarniceria:

                #cogemos el semaforo
                with Carniceria.semafCarniceria:
                    pasaCarniceria=True
                    print("El cliente", self.name, "está siendo atendido en la carnicería.")
                    time.sleep(random.randint(1,10))
                    print("El cliente", self.name, "ha terminado en carnicería.")
                
            if Carniceria.semafCharcuteria._value>0:
                #cogemos el semaforo
                with Carniceria.semafCharcuteria:
                    pasaCharcuteria=True
                    print("El cliente", self.name, "está siendo atendido en la charcutería.")
                    time.sleep(random.randint(1,5))
                    print("El cliente", self.name, "ha terminado en charcutería.")
        
        else:
            if pasaCarniceria and pasaCharcuteria:
                print("El cliente", self.name, "ha pasado tanto por la charcutería como por carnicería")

