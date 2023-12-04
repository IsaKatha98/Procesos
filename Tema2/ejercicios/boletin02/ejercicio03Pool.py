from multiprocessing import*
import time
import random

#función que genera 6 números aleatorios.
def random6 (rutaFichero):
    #abrimos el fichero de destino.
    with open (rutaFichero, "w") as file:
        #Hacemos el bucle for.
        for _ in range(6):
            #generamos seis números aleatorios con decimales y los vamos guardando en el fichero.
            num=round(random.uniform(0,10),2)
            #guardamos num en el archivo y le ponemos un salto de línea.
            file.write(f"{num}\n")

#Función que calculará la media de cada alumno.
def calculaMedias (fichero, nombreAlumno):
    totalNotas=0
    #leemos el fichero que nos pasan
    with open (fichero, 'r') as file:
        lineas=file.readlines()

        #recorremos lineas y vamos sumando a una variable
        for i in lineas:
            totalNotas+=float(i)

        #Hacemos la media.
        else:
            mediaNotas=totalNotas/int(i)
        #abrimos otro fichero nuevo donde escribiremos las medias.
        #lo abrimos con "a" para que escriba concatenando
            with open ("medias.txt", "a") as newFile:
                newFile.write(f"{mediaNotas} {nombreAlumno}\n")

            newFile.close()

def calculaNotaMax ():
    #inicializamos una variable notaMax
    #necesitamos que sea una tupla para poder compararla con la que nos viene.
    notaMax=[0,0]
    #abrimos el fichero de medias.
    with open ("medias.txt", "r") as file:
       #recorremos el archivo.
       for linea in file:
            #Guardamos cada linea como una tupla.
            linea=linea.split(" ")

            #comparamos si el primer valor de la tupla es mayor que notaMaxima.
            #si lo es, lo seteamos como la nueva notaMax.
            if linea[0]>notaMax[0]:
                notaMax=linea
       else:
        #Pasamos notaMax a string.
        notaMax=" ".join(notaMax)
        print(notaMax)

        #cerramos el archivo.
        file.close()

if __name__=="__main__":

    #iniciamos el tiempo.
    inicio=time.time()

    #con pool
    with Pool(processes=10) as pool1:
        ficheros=[]
        for i in range(10):
            ficheros.append(f"Alumno{i+1}.txt")
        pool1.map(random6,ficheros)
    #hacemos un join pa que se espere a que el pool1 termine.
    pool1.join()

    with Pool(processes=10) as pool2:
        ficheros=[]
        for i in range(10):
            #creamos una tupla con los dos argumentos que necesitamos
            args=(f"Alumno{i+1}.txt",f"Alumno{i+1}")
            #añadimos los argumentos a la lista
            ficheros.append(args)
        pool2.starmap(calculaMedias,ficheros)


    

    
   


    fin=time.time()

    print("Tiempo", fin-inicio)

            

       