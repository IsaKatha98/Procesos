from threading import *
import random;
class NumeroOculto (Thread):
    #este será el número a adivinar
    num= random.randint(0,100)
    numAcertado=False #booleano que controla si el número se ha acertado o no
    bloqueo=Lock()#definimos un objeto de tipo Lock.
     #esto es como un constructor de la clase
    def __init__(self, nombre):
      Thread.__init__(self, name=nombre)

    def run(self):

         #mientras no se haya acertado, dejamos que pasen de uno en uno.
        NumeroOculto.bloqueo.acquire()
        #comprobamos si ya se ha acertado el numero.
        while not NumeroOculto.numAcertado:
           
            numRandom=random.randint(0,100)
            print("Hilo", self.name,"num:",numRandom)
             
            if numRandom==NumeroOculto.num:
                print("El hilo", self.name,"ha acertado el número. Es", NumeroOculto.num)
                NumeroOculto.numAcertado=True
                #aquí hacemos un release del bloqueo.
                NumeroOculto.bloqueo.release()
              
                break
                 
            
          
       