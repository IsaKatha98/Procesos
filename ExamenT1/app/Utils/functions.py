import json
import random
import string

#Función que lee el fichero.
def leeFichero (nombreFichero):
    archivo=open(nombreFichero,"r")

    #Comprobamos si el fichero está vacío o no.
    try:

        data=json.load(archivo)
        archivo.close
        return data
    
    except json.JSONDecodeError:
        return []
    
def escribeFichero(nombreFichero, data):
    archivo=open(nombreFichero,"w")
    json.dump(data, archivo)
    archivo.close

#Función que genera una clave aleatoria
def randomKey():
    
    #Definimos el tamaño de la clave.
    tamKey=8

    #Vamos añadiendo los caracteres generados de forma aleatoria
    #hasta alcanzar el tamaño de la clave.
    randomKey="".join(random.SystemRandom().choice(string.ascii_letters+string.digits))
    for _ in range (tamKey):
        return randomKey
 
