from corredores import *
from threading import Barrier
import time

if __name__ == "__main__":
    corredores = []
    numCorredores = 10
    evento = Event()

    for i in range(numCorredores):
        hilo = Corredor(str(i), evento)
        corredores.append(hilo)
    
    print("Los corredores se están dopando...")
    time.sleep(random.randint(1, 3))
    for h in corredores:
        h.start()

    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print("ADELANTE")
    evento.set()
    