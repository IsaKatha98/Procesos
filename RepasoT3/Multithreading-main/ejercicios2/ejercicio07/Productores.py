from threading import Thread
import time
import random

class Capitalismo(Thread):

    def __init__(self, nombre, cond, cola):
        Thread.__init__(self, name=nombre)
        self.cond = cond
        self.cola = cola
    
    def run(self):
        while True:
            cadena = "objeto"
            self.cond.acquire()
            while self.cola.full(): #Si la cola está llena, esperamos
                self.cond.wait()
            print("Productor", self.name, "produciendo")
            self.cola.put(cadena) #Una vez se libere y accedamos a ella, insertamos un elemento
            #release automaticamente
                
            time.sleep(random.randint(3,5))
            print("Productor", self.name, "ya ha producido")
            self.cond.notifyAll() #Notificamos que ya se acabó de producir el temario
            self.cond.release() #Soltamos el hilo