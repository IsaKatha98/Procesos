from clientes import Carniceria

if __name__ == "__main__":
    lista = []
    for i in range(10):
        hilo = Carniceria(str(i))
        hilo.start()
        lista.append(hilo)
    
    for j in lista:
        j.join()

    print("Fin del main")