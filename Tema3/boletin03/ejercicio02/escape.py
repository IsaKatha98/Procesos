from threading import *
import random;
class Escape(Thread):

    #este será la clave a adivinar
    clave= random.randint(0,8)
    claveAcertada=False #booleano que controla si el número se ha acertado o no
    bloqueo=Lock()#definimos un objeto de tipo Lock.
    
    #esto es como un constructor de la clase
    def __init__(self, nombre, barrera:Barrier):
      Thread.__init__(self, name=nombre)
      self.barrera=barrera

    def run(self):

        #hay que esperar a que todos las personas estén en la habitación.
        print ("La persona",self.name, "está en la habitación")
        #ponemos la barrera.
        #comprobamos que todos los hilos están.
        if self.barrera.wait()==4:
            print("Se cierra la habitación.")
        while True:
            with Escape.bloqueo:
                #comprobamos si ya se ha acertado el numero.
                if not Escape.claveAcertada:
                    
                    intentoClave=random.randint(0,8)
                    print("La persona", self.name,"intenta la clave:",intentoClave)
                    
                    if intentoClave==Escape.clave:
                        
                        Escape.claveAcertada=True
                        print("La persona", self.name,"ha acertado la clave. Es", Escape.clave)
                            
                        break
            Escape.bloqueo.release()   
               

                        
        
        print("La persona", self.name, "está esperando en la puerta.")
        #ahora tenemos que esperar a todos los hilos.
        if self.barrera.wait()==4:
            print("Todas las personas salen juntas.")
                        
                
                        
                    