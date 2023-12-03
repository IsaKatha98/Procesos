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
            num=round(random.uniform(1,6),2)
            #guardamos num en el archivo y le ponemos un salto de línea.
            file.write(f"{num}\n")

#Función que calculará la media de cada alumno.
def calculaMedias (rutaFichero, nombreAlumno):
    #leemos el fichero que nos pasan
    with open (rutaFichero, 'r') as file:
        lineas=file.readlines().strip()

        #cerramos el archivo.
        file.close()

        #recorremos lineas y vamos sumando a una variable
        for i in lineas:
            totalNotas+=i

        #Hacemos la media.
        else:
            mediaNotas=totalNotas/i
        #abrimos otro fichero nuevo donde escribiremos las medias.
            with open ("medias.txt", "w") as newFile:
                newFile.write(mediaNotas," ", nombreAlumno)

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

    #inicializamos una variable alumnos
    alumnos=[]
    
    #Hacemos un bucle for.
    for i in range(10):
         #creamos los ficheros.
        if i<10:
       
            nombreFichero=f"Alumno{i+1}.txt"
        with open(nombreFichero,"w"):
            pass #pass es para que el fichero se cree vacío.
        #lanzamos el proceso,
        p1=Process(target=random6, args=(nombreFichero,))
        p1.start()
        

        #guardamos el nombre de los archivos, ya que nos harán falta para el pool.
        alumnos.append(nombreFichero)
    else: 
        #esperamos a que termine p1.
        p1.join()
    #ahora hacemos el pool.
    #TODO: no funciona
        with Pool(processes=10) as pool:
            alumnos
        results=pool.map(calculaMedias, alumnos)
      
        #lanzamos el último proceso.

        p3=Process(target=calculaNotaMax)
        p3.start()

    fin=time.time()

    #esto me da raro
    #TODO:calcular tiempos, preguntar
    print("Tiempo", fin-inicio)

            