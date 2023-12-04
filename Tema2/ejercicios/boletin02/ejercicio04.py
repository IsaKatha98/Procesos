from multiprocessing import *
import time
import sys

#Función que lee el fichero y busca según el año de las películas.
def buscaPelis(cola, fichero, year):
    #hacemos un boolean por si no encuentra el año.
    yearFound=False

    #abrimos el fichero en modo lectura.
    with open (fichero, "r") as file:
        #recorremos el fichero.
        for linea in file:
            #leemos
            linea=linea.split(";")
            #quitamos el salto de línea
            linea[1]=linea[1].strip()
            #comparamos los años
            if linea[1]==(str(year)):
                #enviamos la peli que sea
                cola.put(linea[0])
                yearFound=True
        #si llegamos al final del archivo y no se ha encontrado el año, ponemos mensajito.
        if yearFound is False:
            print("No hay películas de ese año")
            cola.put(None)
    
        #ponemos none.
        else:
            cola.put(None)

#Función que guarda las películas en un fichero.
def clasificaPelis(cola, year):
    #recibimos la peli
    peli=cola.get()
    #Comprobamos que peli no es None, pa que finalize el proceso
    if peli!=None:
        #hacmeos un fichero.
        archivo=f"peliculas{year}"
        #bucle while para que se repita mientras la cola no pase None.
        while peli!=None:
            #abrimos un fichero en modo"a" para concatenar
            with open(archivo,"a") as file:
                #añadimos las peliculas
                file.write(f"{peli}\n")

            #pedimos la siguiente peli.
            peli=cola.get()

        print("El fichero se ha generado con éxito")


if __name__=="__main__":

    #Pedimos al usuario que introduzca un año.
    year=input("Por favor, introduzca un año: ")
    
    #Declaramos tiempo de inicio
    inicio=time.time()

    #Guardamos la ruta del fichero.
    fichero="Tema2/ejercicios/boletin02/ficheros/pelis"
    
    cola=Queue()

    p1=Process(target=buscaPelis, args=(cola, fichero, year))
    p2=Process(target=clasificaPelis, args=(cola,year))

     #Iniciamos los procesos.
    p1.start()
    p2.start()
  
     #Esperamos a que terminen.
    p1.join()
    p2.join()

   
    fin=time.time()

    #esto me da raro
    #TODO:calcular tiempos, preguntar
    print("Tiempo", fin-inicio)
