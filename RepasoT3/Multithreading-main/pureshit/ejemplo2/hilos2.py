from threading import Thread

def imprimirMensaje(num):
    print("Soy el hilo", num)

if __name__ == "__main__":
    print("Soy el hilo principal")
    for i in range(0,10):
        hilo = Thread(target=imprimirMensaje, args=(i,))
        hilo.start()