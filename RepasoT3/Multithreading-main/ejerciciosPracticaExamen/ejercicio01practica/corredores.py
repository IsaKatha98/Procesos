import random
import time
from threading import *

class Corredor(Thread):

    def __init__(self, nombre, evento:Event):
        Thread.__init__(self, name=nombre)
        self.evento = evento
    
    def run(self):
        
        self.evento.wait()

        print("El corredor", self.name ,"comienza a correr")
        tiempo = round(random.uniform(3,5), 2)
        time.sleep(tiempo)
        print("El corredor", self.name, "ha llegado a la meta. Ha tardado", tiempo,"segundos")
