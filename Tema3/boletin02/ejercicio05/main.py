from hilos import *
if __name__=="__main__":

   hilos=[]
   for i in range (4):
        hilo = Libro(f"hilo{i}")
        hilo.start()
        hilos.append(hilo)
   for h in hilos:
       h.join()