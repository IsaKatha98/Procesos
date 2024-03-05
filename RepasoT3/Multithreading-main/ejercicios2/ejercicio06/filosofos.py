from threading import Thread, Condition
import time
import random

class Palillos(Thread):
    palillos = []
    comiendo = Condition()

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
    
    def run(self):
        while True: #Si queremos que coman y piensen por siempre. No se produce interbloqueo, creo
            print("El filosofo", self.name, "está pensando")

            Palillos.comiendo.acquire()
            if int(self.name) != Palillos.palillos.__len__()-1:
                while Palillos.palillos[int(self.name)] or Palillos.palillos[int(self.name)+1]:
                    Palillos.comiendo.wait()
                Palillos.palillos[int(self.name)] = True
                Palillos.palillos[int(self.name)+1] = True
            else:
                while Palillos.palillos[int(self.name)] or Palillos.palillos[0]:
                    Palillos.comiendo.wait()
                Palillos.palillos[int(self.name)] = True
                Palillos.palillos[0] = True

            print("El filosofo", self.name, "ha conseguido los palillos")
            Palillos.comiendo.release()

            time.sleep(random.randint(2,5))
            print("El filosofo", self.name, "está comiendo")

            Palillos.comiendo.acquire()
            if int(self.name) != Palillos.palillos.__len__()-1:
                Palillos.palillos[int(self.name)] = False
                Palillos.palillos[int(self.name)+1] = False
            else: 
                Palillos.palillos[int(self.name)] = False
                Palillos.palillos[0] = False

            Palillos.comiendo.notifyAll()
            Palillos.comiendo.release()
            print("El filosofo",self.name, "ha dejado sus palillo")
