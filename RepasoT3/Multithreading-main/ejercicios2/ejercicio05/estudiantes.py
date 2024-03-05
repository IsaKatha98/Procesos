from threading import Thread, Condition
import time
import random

class Libro(Thread):
    libros = []
    leyendo = Condition()

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        librosElegidos = random.sample(range(9), 2)
        libro1 = librosElegidos[0]
        libro2 = librosElegidos[1]
        print("El estudiante", self.name, "quiere leer los libros", libro1 + 1, "y", libro2 + 1)

        #Conseguir libros
        Libro.leyendo.acquire()
        while Libro.libros[libro1] or Libro.libros[libro2]:
            Libro.leyendo.wait()

        print("El estudiante", self.name, "ha cogido los libros", libro1 + 1, "y", libro2 + 1)
        Libro.libros[libro1] = True
        Libro.libros[libro2] = True
        Libro.leyendo.release()

        #Leer libros
        time.sleep(random.randint(3, 5))
        print("El estudiante", self.name, "ha leído los libros", libro1 + 1, "y", libro2 + 1)

        #Devolver libros
        Libro.leyendo.acquire()
        Libro.libros[libro1] = False
        Libro.libros[libro2] = False
        Libro.leyendo.notifyAll()
        Libro.leyendo.release()
        print("El estudiante", self.name, "ha devuelto los libros", libro1 + 1, "y", libro2 + 1)
