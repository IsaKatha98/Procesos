from hilos import Hilos1

print("Soy el hilo principal")

for i in range(0,10):
    hilo = Hilos1(i)
    hilo.start()

hilo.join()