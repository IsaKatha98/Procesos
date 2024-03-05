from clientes import Mostrador

if __name__ == "__main__":
    lista = []
    for i in range(5):
        hilo = Mostrador(str(i))
        hilo.start()
        lista.append(hilo)
    
    for j in lista:
        j.join()

    print("Fin del main")