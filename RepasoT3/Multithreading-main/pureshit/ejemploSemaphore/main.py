from cajero import Cajero

if __name__ == "__main__":
    lista = []
    for i in range(20):
        hilo = Cajero(str(i))
        hilo.start()
        lista.append(hilo)
    
    for j in lista:
        j.join()

    print("Fin del main")