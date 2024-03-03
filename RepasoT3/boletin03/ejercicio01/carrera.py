from threading import *
import time
import random


#declaramos la clase
class Carrera(Thread):

    #declaramos la barrera
    barrera=Barrier(10)

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run (self):

        print ("Se coloca el corredor", self.name)
        #ponemos la barrera.
        #comprobamos que todos los hilos están.
        if Carrera.barrera.wait()==9:
            print("Todos los corredores están en la línea de salida.")

                #simulamos el tiempo que va a tardar cada hilo en llegar a la meta.
        duracionCarrera=random.uniform(5,15)
        time.sleep(duracionCarrera)

        print("El corredor", self.name, "ha terminado la carrera. Ha tardado:", round(duracionCarrera,2), "segundos.")
        
        

        


