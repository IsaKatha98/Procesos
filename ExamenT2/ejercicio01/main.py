from multiprocessing import *
import random

#función que genera las temperaturas. Este proceso recibirá un fichero
def proceso1(fichero):
    #abrimos el fichero en modo escritura cpon "a" para ir concatenando
    with open (fichero, "a") as file:
        #hacemos un bucle for que genere 24 temperaturas
        for _ in range (24):
            tempRandom=random.uniform(0,20)
            temperatura= round(tempRandom,2)
            
            #añadimos la temperatura al fichero.
            file.write(f"{temperatura}\n")

#función que escribe las temperaturas máximas
#recibe los ficheros que tiene que leer 
def proceso2(fichero):
    temperaturaMaxima=0.00
    #abrimos el fichero a leer.
    with open (fichero,"r") as file:
        #recorremos cada línea del fichero y clasificamos.
        for linea in file:
            temp=linea.strip()
            if float(temp)>float(temperaturaMaxima):
                temperaturaMaxima=temp
        #cuando termine creamos el fichero maximas y escribimos la temperatura.
        else:
            with open ("ejercicio01/ficheros/maximas.txt", "a") as fileWrite:
                #renombramos fichero.
                ficheroNombre=fichero.split("/")
                fichero=ficheroNombre[2].split(".")

                #escrtibimos la fecha y la temperatura.
                fileWrite.write(f"{fichero[0]}:{temperaturaMaxima}\n")

#función que escribe las temperaturas mínimas
#recibe los ficheros que tiene que leer 
def proceso3(fichero):
    #inicializamos la temperatura minima a 20, porque es la temperatura máxima que se puede tener
    temperaturaMinima=20.00
    #abrimos el fichero a leer.
    with open (fichero,"r") as file:
        #recorremos cada línea del fichero y clasificamos.
        for linea in file:
            temp=linea.strip()
            if float(temp)<float(temperaturaMinima):
                temperaturaMinima=temp
        #cuando termine creamos el fichero minimas y escribimos la temperatura.
        else:
            with open ("ejercicio01/ficheros/minimas.txt", "a") as fileWrite:
                 #renombramos fichero.
                ficheroNombre=fichero.split("/")
                fichero=ficheroNombre[2].split(".")

                #escrtibimos la fecha y la temperatura.
                fileWrite.write(f"{fichero[0]}:{temperaturaMinima}\n")



if __name__=="__main__":

    #creamos los ficheros y los añadimos a una lista.
    ficheros=[]
    for i in range(31):
        if i<9:
            ficheros.append(f"ejercicio01/ficheros/0{i+1}-12.txt")
        else:
            ficheros.append(f"ejercicio01/ficheros/{i+1}-12.txt")

    #Utilizamos un Pool ya que nos permite lanzar los procesos de forma
    #simúltanea
    with Pool(processes=31) as pool1:

        pool1.map(proceso1, ficheros)

    #Lanzamos los dos procesos. 
    with Pool (processes=31) as pool2:
        pool2.map(proceso2, ficheros)

    with Pool (processes=31) as pool3:
        pool3.map(proceso3, ficheros)

    #hacemos un join pa que se espere a que el pool1 termine.
    pool1.join()

    print("Termina Pool1")

    print("Todos los procesos han finalizado")


    
            
            

       