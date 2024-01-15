from flask import *
import string
import random
import json

#método que lee el fichero.
def leeFichero (nombreFichero):
    archivo=open(nombreFichero, "r")

    #en caso de que el fichero esté vacío, atrapamos el error.
    try:
        data=json.load(archivo)
        archivo.close()
        return data
    except json.JSONDecodeError:
        return[] #devolvemos una lista vacía.
    
#metodo que escribe en el fichero.
def escribeFichero(nombreFichero, data):
    archivo=open(nombreFichero,"w")
    json.dump(data, archivo)
    archivo.close

#metodo que genera una cadena aleatoria
def randomKey():

    tamKey=8
    
    randomKey= "".join(
        random.SystemRandom().choice(string.ascii_letters + string.digits)
                for _ in range(tamKey)
        )

    return randomKey