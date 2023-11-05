from flask import *
import string
import random

#Método que lee del fichero.
def leeFichero(nombreFichero):
    archivo=open(nombreFichero, "r")
    data=json.load(archivo)
    archivo.close()
    return data

#Método que escribe en el fichero.
def escribeFichero(nombreFichero,data):
    archivo=open(nombreFichero, "w")
    json.dump(data,archivo)
    archivo.close

#Método que genera una cadena aleatoria.
def randomKey():

    tamKey=8

    randomKey= "".join(
        random.SystemRandom().choice(string.ascii_letters + string.digits)
                for _ in range(tamKey)
        )
        
    return randomKey


    
    