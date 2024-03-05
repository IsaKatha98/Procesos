from hilos import *

if __name__ == "__main__":
    
    hilos = [] #Aquí guardaremos los hilos

    # Recorremos la lista de nombres
    for nombre in range(0,10):
        hilo = Hilo(nombre) # Creamos un hilo con el nombre correspondiente
        hilos.append(hilo)
        hilo.start()

    # Recorremos la lista de hilos  
    for hilo in hilos:
        hilo.join() 
