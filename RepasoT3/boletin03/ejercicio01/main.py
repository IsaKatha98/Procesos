from carrera import*

#definimos el main
if __name__=="__main__":

    hilos=[]
    for i in range (1,11):
        hilo= Carrera(f"hilo {i}")
        hilo.start()
        hilos.append(hilo)

    for x in hilos:
        x.join()