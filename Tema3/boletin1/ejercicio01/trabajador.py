from threading import Thread
import time
import random

class Trabajador(Thread):
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run (self):
        while True:
            print("Soy", self.name, "y estoy trabajando.")
            num= random.randint(0, 10)
            time.sleep(num)
            print ("Soy", self.name, "y he terminado de trabajar. He trabajado", num, "horas")