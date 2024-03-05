from threading import *
import random
import time

class numeroOculto(Thread):
    acertado = False
    numerosIntentados = []

    def __init__(self, nombre, numero, lock:Lock):
        Thread.__init__(self, name=nombre)
        self.numero = numero
        self.lock = lock
        
    def run(self): 
        while True:
            self.lock.acquire()
            if numeroOculto.acertado == False:
                intento = random.randint(0, 1000)
                while intento in numeroOculto.numerosIntentados:
                    intento = random.randint(0, 1000)
                print("El hilo", self.name, "prueba con el número", intento)
                self.lock.release()
                self.lock.acquire()
                if intento == self.numero:
                    print("El hilo", self.name, "ha acertado. Era el", intento)
                    break
                numeroOculto.numerosIntentados.append(intento)
                self.lock.release()
            else:
                print("Otro número ya ha acertado")
                self.lock.release()
            time.sleep(0.0001)
            