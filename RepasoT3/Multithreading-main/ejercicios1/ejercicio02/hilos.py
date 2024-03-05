from threading import Thread
import time

class Hilo(Thread):
    contador_compartido = 0

    def __init__(self, nombre):
        Thread.__init__(self)
        self.name = nombre
    
    def run(self):
        while Hilo.contador_compartido < 1000: #Mientras la variable compartida sea menor a 1000 
            Hilo.contador_compartido+=1 #Sumamos +1 a dicha variable
            print(f"Contador: {Hilo.contador_compartido}, Hilo: {self.name}") #Mostramos el hilo y el progreso del contador
            time.sleep(0.05)  #Cada hilo se activa cada 0.05 secs