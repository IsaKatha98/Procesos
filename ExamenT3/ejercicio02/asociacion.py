from threading import *
import random
import time

cant=0
cantMax=2000

class Gestor(Thread):

    
    def __init__(self, nombre, cond):
        Thread.__init__(self, name=nombre)
        self
        self.cond=cond
        

    def run (self):
        global cant
        while True:
            #generamos la cantidad a retirar por cada gestor
            cantidadRetirar=random.randint(10,41)
            print ("El gestor", self.name, "quiere retirar", cantidadRetirar, "euros")
            with self.cond:
                #comprobamos que la cantidad a retirar es menor que la que hay.
                while cantidadRetirar< cant:

                    #retiramos la cantidad
                    time.sleep(random.randint(2,5))
                    cant-=cantidadRetirar
                    print("El gestor", self.name, "retira", cantidadRetirar, "euros")
                    print("Hay", cant, "euros")
                    self.cond.notifyAll()
                    break
                else:
                    print("El gestor", self.name, "todavía no puede retirar", cantidadRetirar, "euros")
                    self.cond.wait()

class Voluntario (Thread):
   
    def __init__(self, nombre, cond):
        Thread.__init__(self, name=nombre)
        self
        self.cond=cond
        

    def run (self):
        global cant
        while True:
            #generamos la cantidad a ingresar por cada voluntario
            cantidadIngresar=random.randint(4,26)
            print ("El voluntario", self.name, "recauda", cantidadIngresar, "euros")
            with self.cond:
                #simulamos la cantidad a ingresar
                simulCant=cant
                simulCant+=cantidadIngresar
                
                #comprobamos que la cantidad simulada a ingresar no supera los 2000
                while simulCant<cantMax:

                    #ingresamos la cantidad
                    time.sleep(random.randint(1,4))
                    cant+=cantidadIngresar
                    print("El voluntario", self.name, "ingresa", cantidadIngresar, "euros")
                    print("Hay", cant, "euros")
                    self.cond.notifyAll()
                    break
                else:
                    print("El voluntario", self.name, "todavía no puede ingresar", cantidadIngresar, "euros")
                    self.cond.wait()











