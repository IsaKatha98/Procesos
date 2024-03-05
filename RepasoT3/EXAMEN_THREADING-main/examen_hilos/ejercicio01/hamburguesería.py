#Este ejercicio lo voy a hacer mediante el método de sincronización Semaphore. Éste método permite que una cierta cantidad de hilos entre a la vez en la sección crítica.
#En este ejercicio, hay dos secciones críticas, las máquinas y el mostrador. Sólo pueden acceder a las máquinas dos clientes a la vez, y 5 a la vez al mostrador.
#Estas limitaciones se las especifico a cada Semaphore para que ellos gestionen la cantidad de clientes en cada sección

from threading import Semaphore, Thread
import random
import time

class Hamburguesería(Thread):
    cantidadMaquinas = 2 #cantidad de máquinas en el local
    cantidadDependientes = 5 #cantidad de dependientes en el local
    semaforoMaquinas = Semaphore(cantidadMaquinas)
    semaforoDependientes = Semaphore(cantidadDependientes)

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        self.ticket = False #Se pondrá a true cuando el cliente pida en la maquina
        self.atendido = False #Se pondrá a true cuando el cliente haya sido atendido por un dependiente
    
    def run(self):
        while not self.atendido: #Mientras el cliente no haya sido atendido por un dependiente
            print("El cliente", self.name, "entra en la hamburguesería")

            #Bloqueamos el código
            Hamburguesería.semaforoMaquinas.acquire()
            
            while not self.ticket: #Mientras el cliente no consiga un ticket con su pedido
                print("El cliente", self.name, "está pidiendo en la máquina") 
                time.sleep(random.randint(1, 4)) #Tiempo de tardanza en pedir su hamburguesa
                self.ticket = True #Consigue el ticket
            Hamburguesería.semaforoMaquinas.release() #Liberamos el espacio en la maquina
            
            #Bloqueamos el código
            Hamburguesería.semaforoDependientes.acquire()
            print("El cliente", self.name, "está siendo atendido en el mostrador por el dependiente")
            time.sleep(random.randint(3, 7)) #tiempo de espera en lo que es atendido cada cliente
            print("El cliente", self.name, "ya tiene su comida.")
            self.atendido = True #Cliente atendido
            Hamburguesería.semaforoDependientes.release() #Liberamos el espacio en el mostrador
        
        print("El cliente", self.name, "sale de la hamburguesería.")

