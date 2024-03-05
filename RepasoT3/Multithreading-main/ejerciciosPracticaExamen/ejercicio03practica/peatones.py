#Crea un simulador de paso de peatones. Varios hilos representan a los peatones que esperan en una barrera para cruzar la calle. 
#Un temporizador simula el cambio de luz del semáforo, liberando periódicamente la barrera para permitir el cruce de los peatones.
from threading import *

class Peatones(Thread):

    def __init__(self, nombre, evento:Event):
        Thread.__init__(self, name=nombre)
        self.evento = evento

    def run(self):
        while not self.evento.is_set():
            self.evento.wait()
        
        print("El peaton", self.name, "ha cruzado el paso de peatones.")
