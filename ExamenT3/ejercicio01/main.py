from hamburgueseria import *
from threading import Event
import time
import random

if __name__=="__main__":

    #Las máquinas serán eventos para poder controlar la forma en la que 
    #los clientes acceden a ellas.
    maquina1=Event()
    maquina2=Event()
    

    hilos = []
    
    for i in range (1,11):
        
        hilo = Hamburgueseria(str(i), maquina1, maquina2)
        #ponemos un time.sleep para simular que los clientes llegan de forma distinta.
        time.sleep(random.randint(1,6))

        hilo.start()

        hilos.append(hilo)


    for x in hilos:
        x.join()    
   
    