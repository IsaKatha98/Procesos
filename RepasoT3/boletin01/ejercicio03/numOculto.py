from threading import *
import random

#definimos la clase
class NumOculto(Thread):

    #generamos un numAleatorio
    numO=random.randint(0,101)
    numAcertado=False
    block=Lock()
    
    #definimos el constructor
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    #definimos la función que gestiona los hilos
    def run(self):
        while True:
            NumOculto.block.acquire()
            #creamos un bucle que compruebe si numAcertado es falso
            if not NumOculto.numAcertado:
                #generamos un numAleatorio.
                numAdivina= random.randint(0,101)
                print("Soy el", self.name, "y el número que he adivinado es: ", numAdivina)
                NumOculto.block.release()

                
                #si adivina el número oculto
                if numAdivina==NumOculto.numO:
                    NumOculto.block.acquire()
                    print("Soy el", self.name,"y he adivinado el número oculto:", NumOculto.numO)
                    NumOculto.numAcertado=True
                    NumOculto.block.release()
                    break

                else: 
                    print("Soy el", self.name, "y no he adivinado el número oculto")
              

                        
                            
                            




