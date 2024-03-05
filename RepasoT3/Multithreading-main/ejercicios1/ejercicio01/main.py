from threading import Thread
from hilos import *

if __name__ == "__main__":

    nombres = ["Luisa Gameplays", "Migue Pelate", "Isabela Katharina", "Jordi Calba", "Fran García"] #nombres de los hilos
    hilos = [] #Aquí guardaremos los hilos

    # Recorremos la lista de nombres
    for nombre in nombres:
        hilo = Hilo(nombre) # Creamos un hilo con el nombre correspondiente
        hilos.append(hilo)
        hilo.start()

    # Recorremos la lista de hilos
    for hilo in hilos:
        hilo.join() 