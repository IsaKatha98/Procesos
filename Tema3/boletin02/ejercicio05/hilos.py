import random
from threading import *
import time

class Libro(Thread):

    libros=[]
    for i in range(9):
        libros.append(False)
    cond= Condition()

    def __init__(self, nombre):
      Thread.__init__(self, name=nombre)

    def run(self):
       seleccionados= random.sample(range(9), 2) #nos genera una lista de dos elementos en un rango de 9, porque son 9 libros.

       libro1=seleccionados[0]
       libro2=seleccionados[1]
       Libro.cond.acquire()
       while Libro.libros[libro1] or Libro.libros[libro2]:
          print("El estudiante", self.name, "está esperando los libros: ",libro1," y ", libro2)
          Libro.cond.wait()

       Libro.libros[libro1]=True
       Libro.libros[libro2]=True
       Libro.cond.release()
       print("El estudiante", self.name, "está usando los libros: ",libro1," y ", libro2)
       time.sleep(random.randint(3,5))
       Libro.cond.notifyAll()
       Libro.cond.release()
       print("El estudiante", self.name, "ha devuelto los libros.")
