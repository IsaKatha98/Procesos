from queue import Queue
from threading import *
from Productores import *
from Consumidores import *

#Si ponemos un elemento como máximo de la cola, los hilos productores y consumidores se intercalan sin problemas,
    #ya que cuando haya un producto, los productores no pueden producir, y cuando no lo haya, los consumidores no pueden consumir.
    #Al aumentar el tamaño de la cola, es el primer hilo de cualquier tipo que acceda a la cola quien determina qué acción toma lugar.
    #Es decir, si en la cola de tamaño 5 hay 3 productos, pueden acceder tanto productores como consumidores, así que el primero que acceda
    #consumirá o producirá en función de la clase del hilo.
if __name__ == "__main__":
    max = 5
    cola = Queue(maxsize=max)
    cond = Condition()
    listaHilosProductores = []
    listaHilosConsumidores = []

    for i in range(3):
        hilo = Capitalismo(str(i), cond, cola)
        hilo.start()
        listaHilosProductores.append(hilo)

    for p in range(7):
        hilo = Consumismo(str(p), cond, cola)
        hilo.start()
        listaHilosConsumidores.append(hilo)
    
    for j in listaHilosProductores:
        j.join()
    
    for h in listaHilosConsumidores:
        h.join()
    
    print("Fin del main")