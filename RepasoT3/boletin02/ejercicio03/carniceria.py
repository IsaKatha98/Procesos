from threading import *
import random
import time

#definimos la clase
class Carniceria(Thread):

    #definimos una variable dependiente.
    #cuando esta variable sea falsa, estará libre
    #si es True, está ocupada.
    dependiente1=False 
    dependiente2=False
    dependiente3=False
    dependiente4=False

    #definimos un semáforo
    semaf=Semaphore(4)
    
    #definimos el constructor
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    #definimos la función que gestiona los hilos
    def run(self):
        print("El cliente", self.name, "llega a la carniceria")

        #cogemos el semáforo
        with Carniceria.semaf:
            #si el dependiente está libre
            if not Carniceria.dependiente1:
               
                Carniceria.dependiente1=True
                print("El cliente", self.name, "está siendo atendido por el dependiente1")

                #generamos un número de segundos aleatorios
                num=random.randint(1,6)
                time.sleep(num)

                #soltamos la caja
                Carniceria.dependiente1=False
                print ("El cliente", self.name, "se va")
            
            elif not Carniceria.dependiente2:
                Carniceria.dependiente2=True
                print("El cliente", self.name, "está siendo atendido por el dependiente2")

                #generamos un número de segundos aleatorios
                num=random.randint(1,6)
                time.sleep(num)

                #soltamos la caja
                Carniceria.dependiente2=False
                print ("El cliente", self.name, "se va")

            elif not Carniceria.dependiente3:
                Carniceria.dependiente3=True
                print("El cliente", self.name, "está siendo atendido por el dependiente3")

                #generamos un número de segundos aleatorios
                num=random.randint(1,6)
                time.sleep(num)

                #soltamos la caja
                Carniceria.dependiente3=False
                print ("El cliente", self.name, "se va")

            elif not Carniceria.dependiente4:
                Carniceria.dependiente2=True
                print("El cliente", self.name, "está siendo atendido por el dependiente4")

                #generamos un número de segundos aleatorios
                num=random.randint(1,6)
                time.sleep(num)

                #soltamos la caja
                Carniceria.dependiente4=False
                print ("El cliente", self.name, "se va")

            
        
           

       
            
               
           


