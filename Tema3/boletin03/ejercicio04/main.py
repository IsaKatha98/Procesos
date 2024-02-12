from trabajadores import *
from threading import Barrier, Event, Timer
if __name__=="__main__":

    #definimos la barrera y el evento.
    barrera=Barrier(5)
    evento=Event()

    hilos = []
    
    print("Empieza la jornada laboral.")
    for i in range (1,6):
        
        hilo = Almacen(str(i), barrera, evento)

        hilo.start()

        hilos.append(hilo)


    for x in hilos:
        x.join()    
   
    