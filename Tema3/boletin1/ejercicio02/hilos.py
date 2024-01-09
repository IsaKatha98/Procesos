
import threading
from typing import Any

class Contador (threading.Thread):
    #atributo
    contador=0

    #esto es como un constructor de la clase
    def __init__(self, nombre):
      threading.Thread.__init__(self, name=nombre)

    def run(self):
        while Contador.contador<1000:
            Contador.contador=Contador.contador+1
            print(Contador.contador)
       
          