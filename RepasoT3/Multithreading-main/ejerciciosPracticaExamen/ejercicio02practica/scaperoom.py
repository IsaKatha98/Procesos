#Simula una sala de Escape Room en la que hay 5 personas encerradas. 
#Para poder salir deben adivinar la clave que abre la puerta que es un código de 4 cifras. 
#Una vez adivinado, deben juntarse los 5 para poder salir juntos y así no dejar a ninguno atrás.
from collections.abc import Callable
from threading import *
import random

class ScapeRoom(Thread):
    acertado = False
    candado = Lock()

    def __init__(self, nombre, codigo, barrera:Barrier):
        Thread.__init__(self, name=nombre)
        self.codigo = codigo
        self.barrera = barrera
    
    def run(self):
        while not ScapeRoom.acertado:
            intento = random.randint(1000, 9999)
            print("El hilo", self.name, "prueba con el numero", intento)
            ScapeRoom.candado.acquire()
            if intento == self.codigo:
                ScapeRoom.acertado = True
                print("El hilo", self.name, "ha acertado")
            ScapeRoom.candado.release()

        if ScapeRoom.acertado: 
            print("Los hilos han conseguido salir y se están reuniendo")
            self.barrera.wait()
            print("Los hilos han escapado todos juntos")

