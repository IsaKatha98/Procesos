from threading import Thread
import random

class NumeroOculto (Thread):
    #este será el número a adivinar
    num= random.randint(0,100)
    numAcertado=False #booleano que controla si el número se ha acertado o no
     #esto es como un constructor de la clase
    def __init__(self, nombre):
      Thread.__init__(self, name=nombre)

    def run(self):
        #comprobamos si ya se ha acertado el numero.
        while not NumeroOculto.numAcertado:
            numRandom=random.randint(0,100)
            print("Hilo", self.name,"num:",numRandom)
            if numRandom==NumeroOculto.num:
                print("El hilo", self.name,"ha acertado el número. Es", NumeroOculto.num)
                NumeroOculto.numAcertado=True
                break
            
          

           