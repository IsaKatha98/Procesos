from multiprocessing import *
import time

#Función que lee el fichero y busca según el año de las películas.
def buscaPelis(cola, fichero, year):

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
        #ponemos none.
        else:
            cola.put(None)

#Función que guarda las películas en un fichero.
def clasificaPelis(cola, year):
    #recibimos la peli
    peli=cola.get()
    #bucle while para que se repita mientras la cola no pase None.
    while peli!=None:
        #abrimos un fichero en modo"a" para concatenar
        with open(f"peliculas{year}","a") as file:
            #añadimos las peliculas
            file.write(f"{peli}\n")

        #pedimos la siguiente peli.
        peli=cola.get()
    else:
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
