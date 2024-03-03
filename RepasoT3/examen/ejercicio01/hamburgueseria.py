from threading import *
import time
import random
from typing import Mapping

#definimos la clase
class Hamburgueseria(Thread):
    
    #definimos los semáforos
    semaforoMaquinas=Semaphore(2) 
    semaforoMostrador=Semaphore(5)

    #definimos el constructor
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run (self):

        #definimos las variables que vamos a necesitar
        tieneTicket=False
        tieneComida=False

        print("Llega el cliente", self.name)

        #cogemos el semaforo de las máquinas
        with Hamburgueseria.semaforoMaquinas:

            #mientras no tenga el ticket.
            while not tieneTicket:
                print("El cliente", self.name, "está pidiendo en un máquina")
                time.sleep(random.randint(1,5))
                print ("El cliente", self.name, "ya tiene ticket")
                tieneTicket=True

            
        #cogemos el semaforo del mostrador.
        with Hamburgueseria.semaforoMostrador:

            #esperará en el mostrador mientras no tenga comida
            while not tieneComida:
                print("El cliente", self.name, "está siendo atendido")
                time.sleep(random.randint(3,8))
                print("El cliente", self.name," ya tiene su comida")
                tieneComida=True