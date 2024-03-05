
from hilos import *

#Lo mejor que he podido hacer
if __name__ == "__main__":
    
    # Recorremos la lista de nombres
    for nombre in range(0,10):             
            hilo = Hilo(str(nombre)) # Creamos un hilo con el nombre correspondiente
            hilo.start()    