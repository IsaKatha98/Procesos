from filosofos import *

#Como tiene que ser un bucle para una lista 'circular', es decir, que el palillo de la derecha del último elemento es el palillo de la izquierda
#del primer elemento, he jugado con la longitud y las condiciones para que no pete el programa
if __name__ == "__main__":
    palillos = 5
    lista = []

    for _ in range(palillos):
        Palillos.palillos.append(False)
    
    for i in range(5):
        hilo = Palillos(str(i))
        hilo.start()
        lista.append(hilo)
    
    for j in lista:
        j.join()
    
    print("Fin del programa")