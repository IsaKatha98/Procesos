
from threading import *
from typing import Any

class Contador (Thread):
    #atributo
    contador=0
    l= Lock()

    #esto es como un constructor de la clase
    def __init__(self, nombre):
      Thread.__init__(self, name=nombre)

    def run(self):
        print ("Ejecutando: ", self.name)
        Contador.l.acquire()
        while Contador.contador<1000:
            Contador.contador=Contador.contador+1
            print(Contador.contador)
        Contador.l.release()
       
          