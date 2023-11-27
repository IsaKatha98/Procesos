from multiprocessing import *

#Función que lee el fichero.
def leeFichero(rutaFichero, conn): 
    with open(rutaFichero, "r") as fichero:
        for linea in fichero:
            num=linea.strip().split(" ")
            num1,num2=map(int,num)
            numeros=(num1,num2)
            conn.send(numeros)
            
    #Ponemos None y cerramos.
    conn.send(None)
    conn.close()

def suma (conn):
    res=0
    while True:
        num=conn.recv()
        if num is None:
            break
        if (num[0]>num[1]):
        #Intercambiamos los valores de las variables.
            num=num[1],num[0]

        for n in range (num[0],num[1]+1):
            res+=n
        print ("suma igual a ",res)
        res=0

if __name__=="__main__":
    funcion_leer,funcion_sumar=Pipe()
    rutaFichero="ejercicios/boletin01/ficheros/fichero07.txt"
    
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