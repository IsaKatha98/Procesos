from clase import *

#declaramos el main
if __name__=="__main__":

    hilos=[]

    hilo1= Colores("Luisa", "rojo")
    hilo1.start()
    hilos.append(hilo1)

    hilo2=Colores("Carmen", "azul")
    hilo2.start()
    hilos.append(hilo2)

    hilo3=Colores("Isa","amarillo")
    hilo3.start()
    hilos.append(hilo3)

   

    for x in hilos:

        x.join()

   

   