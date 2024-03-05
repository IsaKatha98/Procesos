from threading import Thread
import random
import time

class Hilo(Thread):
    numero = random.randint(0,100)
    acertado = False

    def __init__(self, nombre):
        Thread.__init__(self)
        self.name = nombre
        
        #Función run
    def run(self):
        while Hilo.acertado is False: #Mientras no se haya acertado el número secreto
            intento = random.randint(0,100) #Creamos un nuevo número aleatorio
            print(f"El hilo {self.name} prueba con el número {intento}") #Mostramos el hilo que ha intentado adivinarlo
            if intento == Hilo.numero: #Si se adivina, lo comunicamos
                print(f"El hilo {self.name} ha acertado. Era el número {Hilo.numero}") 
                Hilo.acertado = True #Cambiamos la variable global de hilos
            time.sleep(1)  # Detenemos la ejecución durante un segundo