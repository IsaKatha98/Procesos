
from threading import *

class ContadorB (Thread):
    #atributo
    contador=0
    l= Lock()

    #esto es como un constructor de la clase
    def __init__(self, nombre):
      Thread.__init__(self, name=nombre)

    def run(self):
        print ("Ejecutando: ", self.name)
        ContadorB.l.acquire()
        while ContadorB.contador<1000:
            ContadorB.contador=ContadorB.contador+1
            print("Soy el",self.name, "y he aumentado el contador:",ContadorB.contador)
        ContadorB.l.release()
       