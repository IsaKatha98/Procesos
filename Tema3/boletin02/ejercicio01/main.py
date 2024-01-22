from hilos import NumeroOculto
if __name__=="__main__":
    for i in range (0,10):
        hilo = NumeroOculto(f"hilo{i}")
        hilo.start()