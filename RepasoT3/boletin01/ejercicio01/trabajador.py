from threading import *
import time
import random

#definimos la clase
class Trabajador(Thread):
    
    #definimos el constructor
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    #definimos la función que gestiona los hilos
    def run(self):

        #creamos un bucle infinito
        while True:

            print("Soy el", self.name, "y empiezo a trabajar")
            
            #definimos un número aleatorio.
            num=random.randint(0,11)

            #descansamos ese número de segundos.
            time.sleep(num)

            print("Soy el", self.name,"y he estado trabajando", num, "segundos")