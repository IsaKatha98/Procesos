from numeroOculto import numeroOculto
import random
from threading import Lock

if __name__ == "__main__":
    numeroHilos = 10
    numero = random.randint(0,1000)
    lock = Lock()

    for i in range(numeroHilos):
        hilo = numeroOculto(str(i), numero, lock)
        hilo.start()