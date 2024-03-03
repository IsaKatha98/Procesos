from threading import Condition, Thread, Barrier
import random
import time
from typing import Mapping
class Carrera(Thread):

    cond=Condition()

    def __init__ (self, nombre, barrera:Barrier):
        Thread.__init__(self, name=nombre)
        self.barrera=barrera

    def run (self):
        #hay que esperar a que todos los corredores estén en la línea de salida.
        print ("El corredor", self.name,"está en la línea de salida.")
        #ponemos la barrera.
        #comprobamos que todos los hilos están.
        if self.barrera.wait()==9:
            print("Todos los corredores están en la línea de salida.")

        #simulamos el tiempo que va a tardar cada hilo en llegar a la meta.
        duracionCarrera=random.uniform(5,15)
        time.sleep(duracionCarrera)

        print("El corredor", self.name, "ha terminado la carrera. Ha tardado:", round(duracionCarrera,2), "segundos.")
                                                                                      
                                                                                        



