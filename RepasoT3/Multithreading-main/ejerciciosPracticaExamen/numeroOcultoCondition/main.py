from numeroOcultoCond import numeroOculto
import random
from threading import Condition

if __name__ == "__main__":
    numeroHilos = 10
    numero = random.randint(0,1000)
    cond = Condition()

    for i in range(numeroHilos):
        hilo = numeroOculto(str(i), numero, cond)
        hilo.start()