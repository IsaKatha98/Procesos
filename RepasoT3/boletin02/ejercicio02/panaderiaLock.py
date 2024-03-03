from threading import *
import random
import time

#definimos la clase
class PanaderiaL(Thread):

    #definimos una variable dependiente.
    #cuando esta variable sea falsa, estará libre
    #si es True, está ocupada.
    dependiente=False 

    #definimos un candado.
    block=Lock()
    
    #definimos el constructor
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    #definimos la función que gestiona los hilos
    def run(self):
        print("El cliente", self.name, "llega a la panadería")

        #cogemos el candado
        with PanaderiaL.block:
            #si el dependiente está libre
            if not PanaderiaL.dependiente:
               
                PanaderiaL.dependiente=True
                print("El cliente", self.name, "está siendo atendido por el dependiente")

                #generamos un número de segundos aleatorios
                num=random.randint(1,6)
                time.sleep(num)

                #soltamos la caja
                PanaderiaL.dependiente=False
                print ("El cliente", self.name, "se va")
        
           

       
            
               
           


