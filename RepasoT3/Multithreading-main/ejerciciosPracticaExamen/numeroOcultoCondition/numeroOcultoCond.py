from threading import *
import random
import time

class numeroOculto(Thread):
    acertado = False
    numerosIntentados = []
    intentando = False

    def __init__(self, nombre, numero, cond:Condition):
        Thread.__init__(self, name=nombre)
        self.numero = numero
        self.cond = cond

    def run(self): 
        while True:
            self.cond.acquire()
            while numeroOculto.intentando:
                self.cond.wait()

            numeroOculto.intentando = True
            intento = random.randint(0, 1000)

            while intento in numeroOculto.numerosIntentados:
                intento = random.randint(0, 1000)
            print("El hilo", self.name, "prueba con el número", intento)
            numeroOculto.numerosIntentados.append(intento)

            if intento == self.numero:
                print("El hilo", self.name, "ha acertado. Era el", intento)
                numeroOculto.acertado = True
            self.cond.release()
            
            self.cond.acquire()
            numeroOculto.intentando = False
            self.cond.notify_all()
            self.cond.release()
            