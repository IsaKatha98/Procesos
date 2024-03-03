from trabajador import*

#definimos el main
if __name__=="__main__":

    for i in range (1,6):
        hilo= Trabajador(f"hilo {i}")
        hilo.start()