from threading import Condition, Thread
import random
import time

class Filosofos (Thread):
    cond=Condition()
    palillos=[False, False, False, False, False]


    def __init__(self, nombre):
      Thread.__init__(self, name=nombre)

    def run(self):
        while True:
            print("El ", self.name," está pensado.")
            time.sleep(random.randint(1,5))
            with Filosofos.palillos[int(self.name)]:
                Filosofos.cond.wait()
            Filosofos.palillos[int(self.name)]=True

            while Filosofos.palillos[(int(self.name)+1)%5]:
                Filosofos.cond.wait()
            Filosofos.palillos[(int(self.name)+1)%5]=True

            print ("Filósofo", self.name, "está comiendo")
            time.sleep(random.randint(1,3))
            print ("Filósofo", self.name, "termina de comer")

            with Filosofos.cond:
                Filosofos.palillos[int(self.name)]=False
                Filosofos.palillos[(int(self.name)+1)%5]=False

                Filosofos.cond.notifyAll()

            



