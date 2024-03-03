from almacen import *

#definimos el main
if __name__=="__main__":

    #empezamos los hilos
    hilos=[]

    for i in range (1,11):
        hilo=Almacen(str(i))
        hilo.start()
        hilos.append(hilo)

    for x in hilos:
        x.join()