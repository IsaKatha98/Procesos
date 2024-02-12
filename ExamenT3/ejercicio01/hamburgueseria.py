import time
import random
from threading import *

class Hamburgueseria (Thread):

    #he elegido un semáforo porque hasta cinco clientes pueden ser atendidos a la vez
    #por los dependientes.
    #con esta cantidad de dependientes nunca llega a colapsarse el mostrador.
    #he probado a hacerlo con dos dependientes y sí se produce un colapso.
    dependientes=Semaphore(5) 

    def __init__(self, nombre, maquina1:Event, maquina2:Event):
        Thread.__init__(self, name=nombre)
        self.maquina1=maquina1
        self.maquina2=maquina2

    def run (self):
        enMostrador=True
        siendoAtendido=False
        print("Llega el cliente", self.name)
        
        #comprobamos si alguna de las máquinas está libre.
        if not self.maquina1.is_set():

            #seteamos la máquina.
            self.maquina1.set()
            time.sleep(random.randint (1,5))
            print("El cliente", self.name,"saca un ticket en la máquina 1")
            self.maquina1.clear()
        
        elif not self.maquina2.is_set():

             #seteamos la máquina.
            self.maquina2.set()
            time.sleep(random.randint(1,5))
            print("El cliente", self.name,"saca un ticket en la máquina 2")
            self.maquina2.clear()
        
        else:
            #los clientes tendrán que esperar a que la máquina se libere.
            self.maquina1.wait()
            self.maquina2.wait()
            print("El cliente", self.name,"está esperando a recoger un ticket")

       

   
        while enMostrador:
            print("El cliente", self.name,"está en el mostrador")
            if Hamburgueseria.dependientes._value>0 and not siendoAtendido:
                Hamburgueseria.dependientes.acquire()
                siendoAtendido=True
                print("El cliente", self.name,"está siendo atendido")
                #simulamos un tiempo distinto para cada cliente.
                time.sleep(random.randint(3,8))
                print("El cliente", self.name,"recoge su comida y se va")
                Hamburgueseria.dependientes.release()
                break
            else:
                print("El cliente",self.name, "está esperando a que lo atiendan en el mostrador")




    



    
