from escape import *
from threading import Barrier
if __name__=="__main__":

    #definimos una barrera que es la que hará que todos los hilos
    #se esperen en la línea de salida.
    #ponemos 5 porque es la cantidad total de hilos.
    barrera=Barrier(5)

    for i in range (1,6):
        hilo = Escape(str(i), barrera)

        hilo.start()