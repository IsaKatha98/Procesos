from multiprocessing import*
import time

#función que cuenta las vocales
def cuentaVocales (vocal):
    res=0
    #abrimos el fichero a leer, en modo lectura
    rutaFichero="Tema2/ejercicios/boletin02/ficheros/vocales.txt"

    with open (rutaFichero, "r") as file:
        #recorremos el fichero y contamos las veces que se repite la vocal.
        for letra in file:
            res=letra.count(vocal)

        #cuando terminamos, imprimimos el resultado.
        print("La vocal", vocal, "se repite", res, "veces")

#main
if __name__=="__main__":
    #declaramos el principio del tiempo.
    inicio=time.time()

    #declaramos el Pool con las vocales.
    with Pool(processes=5) as pool:
        vocal=["a", "e", "i","o","u"]
    
        #pedimos los resultados.
        results=pool.map(cuentaVocales, vocal)

    #imprimimos el tiempo
    fin=time.time()

    print ("Tiempo de ejecución:", fin-inicio)