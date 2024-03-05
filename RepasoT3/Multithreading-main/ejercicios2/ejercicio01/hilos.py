from threading import Thread, Lock
import random

class Hilo(Thread):
    numero = random.randint(0,100)
    acertado = False
    bloqueo = Lock()

    def __init__(self, nombre):
        Thread.__init__(self)
        self.name = nombre
        
        #Función run
    def run(self):
        while True:
            if not Hilo.acertado:
                intento = random.randint(0,99)
                Hilo.bloqueo.acquire()
                if intento == Hilo.numero:
                    print(f"El hilo {self.name} ha acertado. Era el número {Hilo.numero}") 
                    Hilo.bloqueo.acquire()
                    Hilo.acertado = True #Cambiamos la variable global de hilos
                    Hilo.bloqueo.release()
                    break
                else:
                    print(f"El hilo {self.name} prueba con el número {intento}") #Mostramos el hilo que ha intentado adivinarlo
                    Hilo.bloqueo.release()
