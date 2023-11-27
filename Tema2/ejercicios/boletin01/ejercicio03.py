from multiprocessing import*

def suma (queue):
    res=0
    while True:
        num=queue.get()
        if num is None:
            break
        for n in range (num+1):
            res+=n
        print ("suma igual a ",res)
        res=0

#Función que lee el fichero.
def producer (ficheroRuta, queue):
    with open(ficheroRuta, "r") as fichero:
        for linea in fichero:
            queue.put(int(linea))
    queue.put(None)
        #Ponemos un None al final de la cola.
      

if __name__=="__main__":

    #Definimos la ruta del fichero de lectura.
    ficheroRuta="ejercicios/boletin01/ficheros/ejercicio03Fichero.txt"
    queue=Queue()

    p1=Process(target=producer, args=(ficheroRuta,queue))
    p2=Process(target=suma, args=(queue,))

    p1.start()
    p2.start()

    p1.join()

    p2.join()

    print("Se han terminado todos los procesos.")

   