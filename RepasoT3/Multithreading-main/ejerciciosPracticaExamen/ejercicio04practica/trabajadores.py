#Implementa un simulador de procesamiento de pedidos en un almacén. Varios hilos representan a los trabajadores que preparan pedidos. 
#Utiliza una barrera para asegurar que todos los trabajadores comiencen a trabajar al mismo tiempo, 
#y un evento que vaya indicando si hay pedido a preparar. Una vez se empieza a preparar el pedido el evento se marca como “no seteado”. 
#Tras un tiempo, se vuelve a generar un pedido poniendo de nuevo el evento a “seteado”.
from threading import *

class Trabajadores(Thread):
    
    def __init__(self, nombre, evento:Event, barrera:Barrier):
        Thread.__init__(self, name=nombre)
        self.evento = evento
        self.barrera = barrera

    def run(self):
        while True:
            while not self.evento.is_set():
                self.evento.wait()
            
            self.barrera.wait()
            print("El hilo", self.name, "está preparando el pedido")
            self.evento.clear()
