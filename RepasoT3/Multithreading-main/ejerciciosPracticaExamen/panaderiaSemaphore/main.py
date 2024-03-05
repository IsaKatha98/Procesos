from panaderia import Panaderia
from threading import Semaphore

if __name__ == "__main__":
    numeroClientes = 10
    semaforo = Semaphore(2)
    clientes = []

    for i in range(numeroClientes):
        hilo = Panaderia(str(i), semaforo)
        hilo.start()
        clientes.append(hilo)

    for hilo in clientes:
        hilo.join()

    print("Fin de la jornada laboral")