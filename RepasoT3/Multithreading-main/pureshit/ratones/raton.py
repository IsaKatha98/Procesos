from threading import *
import time

class Raton(Thread):
    def __init__(self, nombre, tiempoAlimentacion):
        Thread.__init__(self)
        self.nombre = nombre
        self.tiempoAlimentacion = tiempoAlimentacion

    def run(self):
        print("El raton ", self.nombre, " empieza a comer")
        time.sleep(self.tiempoAlimentacion)
        print("El ratón ", self.nombre, " termina de comer")