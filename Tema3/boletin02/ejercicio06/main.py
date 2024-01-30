from hilos import *
if __name__=="__main__":
    for i in range (0,5):
        hilo = Filosofos(f"filósofo {i}")
        hilo.start()