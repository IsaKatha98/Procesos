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

    procesos1=[]
    procesos2=[]

    for i in range(10):
        p1=Process(target=random6, args=(f"Alumno{i+1}.txt",))
        p1.start()
        procesos1.append(p1)
    
    for p in procesos1:
        p.join()

    for i in range(10):
        p2=Process(target=calculaMedias,args=(f"Alumno{i+1}.txt",f"Alumno{i+1}"))
        p2.start()
        procesos2.append(p2)
        
    for p in procesos2:
        p.join()

    p3=Process(target=calculaNotaMax)
    p3.start()




    

    
   


    fin=time.time()

    print("Tiempo", fin-inicio)

            

       