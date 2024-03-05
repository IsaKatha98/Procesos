from peatones import Peatones
from threading import Timer, Event
import time
import random

if __name__ == "__main__":
    evento = Event()
    contador = 0
    tiempoEnRojo = 10
    tiempoEnVerde = 8
    esperandoARojo = False
    esperandoAVerde = False

    def semaforoARojo():
        evento.clear()
        print("SEMÁFORO EN ROJO")

    def semaforoAVerde():
        evento.set()
        print("SEMÁFORO EN VERDE")


    while True:
        if not esperandoAVerde and not evento.is_set():
            semaforo = Timer(tiempoEnRojo, semaforoAVerde).start()
            esperandoAVerde = True
            esperandoARojo = False

        time.sleep(random.randint(1,4)) #Espera entre 1 y 4 segundos
        print("Llega un peatón al cruce")
        peaton = Peatones(str(contador), evento)
        peaton.start()
        contador += 1
        
        if evento.is_set() and not esperandoARojo:
            Timer(tiempoEnVerde, semaforoARojo).start()
            esperandoARojo = True
            esperandoAVerde = False

            

    