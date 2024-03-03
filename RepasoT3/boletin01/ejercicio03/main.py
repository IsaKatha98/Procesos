from numOculto import*

#definimos el main
if __name__=="__main__":

    for i in range (1, 6):
        hilo= NumOculto(f"hilo {i}")
        hilo.start()