from threading import *
import time
import random

#variables globales
#estas hay que vlver a devlararlas dentro de la función
total=0
cond=Condition()

class Voluntarios(Thread):

    #definimos el constructor
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run (self):

        #definimos las variables
        global total
        global cond

        cantMax=2000

        print ("El voluntario", self.name, "sale a buscar dinero")

        while True:
            #definimos la cantidad y el tiempo que tardan en recaudar
            cantRecogida=random.randint(4,26)
          
            print ("El voluntario", self.name, "ha recogido", cantRecogida, "€")

            #cogemos la condicion
            with cond:
            
                #mientras que la cantidadRecogida sea mayor que la cantMax
                #tendrá que esperar para poder añadirla al bote.
                while (cantRecogida+total)>cantMax:
                    print("El voluntario", self.name, "tiene que esperar")
                    cond.wait()

                else:
                    #se suma al bote
                    print("El voluntario", self.name, "está añadiendo", cantRecogida, "€")
                    time.sleep(random.randint(1,4))
                    total+=cantRecogida
                    print("Total:", total)

                    #notificamos al resto de hilos.
                    cond.notifyAll()



class Gestores(Thread):

    #definimos el constructor
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run (self):

        #definimos las variables
        global total
        global cond

        print ("El gestor", self.name, "llega a la oficina")

        while True:
            #definimos la cantidad y el tiempo que tardan en recaudar
            cantParaRetirar=random.randint(10,41)
            print ("El gestor", self.name, "quiere retirar", cantParaRetirar, "€")

            #cogemos la condicion
            with cond:
            
                #mientras que la cantidadRecogida sea mayor que la cantMax
                #tendrá que esperar para poder añadirla al bote.
                while cantParaRetirar>total:
                    print("El gestor", self.name, "tiene que esperar")
                    cond.wait()

                else:
                    #se suma al bote
                    print("El gestor", self.name, "está retiranod", cantParaRetirar)
                    total-=cantParaRetirar
                    time.sleep(random.randint(2,6))
                    print("Total:", total)

                    #notificamos al resto de hilos.
                    cond.notifyAll()





