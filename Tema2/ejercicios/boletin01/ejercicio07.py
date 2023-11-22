from multiprocessing import*

#Función que lee el fichero.
def leeFichero (ficheroRuta, queue):
    with open(ficheroRuta, "r") as fichero:
        for linea in fichero:
            num=linea.strip().split(" ")
            num1,num2=map(int,num)
            numeros=(num1,num2)
            queue.put(numeros)
    queue.put(None)
       
#Método con dos números por parámetro
#En caso de que num1 sea mayor que num2, hay que intercambiarlos.
def suma (queue):

    while True:
        num=queue.get()
       
        if (num==None):
            break
        if (num[0]>num[1]):
        #Intercambiamos los valores de las variables.
            num=num[1],num[0]
    
        res=0
    
        #Recorremos el rango sumando los números.
        for n in range (num[0], num[1]+1):
            res=res+n
    
        print ("suma igual a ",res)

if __name__=="__main__":

    #Definimos la ruta del fichero de lectura.
    ficheroRuta="Tema2/ejercicios/boletin01/ficheros/fichero07.txt"
    queue=Queue()
    
    p1=Process(target=leeFichero, args=(ficheroRuta,queue))
    p2=Process(target=suma, args=(queue,))

    p1.start()
    p2.start()

    p1.join()

    p2.join()

    print("Se han terminado todos los procesos.")

            