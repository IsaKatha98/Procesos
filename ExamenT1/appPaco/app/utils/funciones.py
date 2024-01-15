import json

#Función que lee los datos de un fichero pasado por parámetros y los devuelve
def leeFichero(nombreFichero):
    fichero = open(nombreFichero, 'r') #Guardamos el fichero abierto en modo lectura en una variable
    datos = json.load(fichero) #Cargamos los datos del fichero en una variable
    fichero.close() #Cerramos el fichero
    return datos #Devolvemos los datos

#Método que escribe en un fichero pasado por parámetros los datos pasados por parámetros
def escribeFichero(nombreFichero, datos): #Abrimos el fichero en modo escritura y lo guardamos en una variable
    fichero = open(nombreFichero, "w")#Escribimos los datos que nos han pasado por parámetros
    json.dump(datos, fichero)#Cerramos el fichero
    fichero.close()

#Función para encontrar el primer id disponible en el fichero que mandemos por parámetros
#Asignaremos este id al elemento que vayamos a crear
def find_next_id(nombreFichero):
    elementos = leeFichero(nombreFichero) #Guardamos los datos del fichero
    longitud = len(elementos) #Guardamos la longitud de la lista de elementos del fichero
    ultimoElem = elementos[longitud-1]
    idDispo = ultimoElem["Id"] + 1 #Guardamos en una variable el primerid disponible después del último gurdado en la lista
    return idDispo #Devolvemos el id encontrado