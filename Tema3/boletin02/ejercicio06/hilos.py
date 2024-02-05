from threading import Condition, Thread
import random
import time

class Filosofos (Thread):
    
    def __init__(self, nombre):
      Thread.__init__(self, name=nombre)

    def run(self):
       palillosDerecha= False
       palillosIzquierda=False
       cond=Condition()
       while True: 
          print("El ", self.name," está pensado.")
          #hacemos un acquire:
          with cond:
             #si ninguno de los palillos están cogidos.
             while palillosDerecha and palillosIzquierda:
               
                palillosIzquierda=True
                cond.wait()
            
              #coge el palillo a su izquierda.
             print ("El", self.name, "coge los palillos a su izquierda.")
             palillosIzquierda=True
             time.sleep(random.randint(1,5))
             palillosIzquierda=False
             print ("El", self.name, "suelta los palillos a su izquierda.")
             cond.notifyAll()
          with cond:
             while palillosDerecha:
               
                cond.wait()
                
             print("El", self.name, "coge los palillos de su derecha.")
             palillosDerecha=True
             time.sleep(random.randint(1,5))
             palillosDerecha=False
             print ("El", self.name, "suelta los palillos de su derecha.")
             cond.notifyAll()
          print("El", self.name, "ha terminado de comer.")
          break







          

             

