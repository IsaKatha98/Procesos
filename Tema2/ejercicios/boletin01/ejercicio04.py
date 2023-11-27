from multiprocessing import *

#Función que lee el fichero.
def leeFichero(rutaFichero, conn): 
    with open(rutaFichero, "r") as fichero:
        for linea in fichero:
            conn.send(int(linea))
    #Ponemos None y cerramos.
    conn.send(None)
    conn.close()

def suma (conn):
    res=0
    while True:
        num=conn.recv()
        if num is None:
            break
        for n in range (num+1):
            res+=n
        print ("suma igual a ",res)
        res=0

if __name__=="__main__":
    funcion_leer,funcion_sumar=Pipe()
    rutaFichero="ejercicios/boletin01/ficheros/ejercicio03Fichero.txt"
    
    #Hacemos los procesos.
    p1=Process(target=leeFichero, args=(rutaFichero, funcion_leer))
    p2=Process(target=suma, args=(funcion_sumar,))

    #Iniciamos los procesos.
    p1.start()
    p2.start()

    #Esperamos a que terminen.
    p1.join()
    p2.join()

    print("All processes have finished.")