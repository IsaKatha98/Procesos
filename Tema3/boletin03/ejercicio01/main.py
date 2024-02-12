from carrera import *
from threading import Barrier
if __name__=="__main__":

    #definimos una barrera que es la que hará que todos los hilos
    #se esperen en la línea de salida.
    #ponemos 10 porque es la cantidad total de hilos.
    barrera=Barrier(10)

    for i in range (0,10):
        hilo = Carrera(str(i), barrera)

        hilo.start()