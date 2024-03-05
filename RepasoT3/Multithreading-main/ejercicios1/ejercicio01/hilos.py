from threading import Thread
import random
import time

class Hilo(Thread):
    def __init__(self, nombre):
        # Llamamos al constructor de la clase base
        Thread.__init__(self)
        self.name = nombre
    
    def run(self):
        while True: #Bucle infinito
            print(f"Soy {self.name} y estoy trabajando.") #Empieza a trabajar
            trabajo = random.randint(1, 10) #Guardamos el tiempo que trabaja cada uno
            time.sleep(trabajo)  # Detenemos la ejecución durante un tiempo entre 1 y 10 segundos
            print(f"Soy {self.name} y he terminado de trabajar. He trabajado{ trabajo}s") #Termina de trabajar
            
