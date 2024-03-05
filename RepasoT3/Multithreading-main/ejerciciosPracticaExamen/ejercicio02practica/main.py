from scaperoom import ScapeRoom
from threading import *
import random

if __name__ == "__main__":
    jugadores = 5
    barrera = Barrier(5)
    codigo = random.randint(1000, 9999)

    for i in range(jugadores):
        hilo = ScapeRoom(str(i), codigo, barrera)
        hilo.start()
