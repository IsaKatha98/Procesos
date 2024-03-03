from threading import *
import random
import time

#definimos la clase
class PanaderiaC(Thread):

    #definimos una variable dependiente.
    #cuando esta variable sea falsa, estará libre
    #si es True, está ocupada.
    dependiente=False 

    #definimos una condición.
    cond=Condition()
    
    #definimos el constructor
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    #definimos la función que gestiona los hilos
    def run(self):
        print("El cliente", self.name, "llega a la panadería")

        #cogemos el candado
        with PanaderiaC.cond:
            #si el dependiente está libre
            if not PanaderiaC.dependiente:
               
                PanaderiaC.dependiente=True
                print("El cliente", self.name, "está siendo atendido por el dependiente")

                #generamos un número de segundos aleatorios
                num=random.randint(1,6)
                time.sleep(num)

                #soltamos la caja
                PanaderiaC.dependiente=False
                print ("El cliente", self.name, "se va")
        
           

       
            
               
           


