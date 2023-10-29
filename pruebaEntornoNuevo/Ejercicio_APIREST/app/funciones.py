from flask import *

#Lectura del fichero.
def leeFichero(nombreFichero):
    archivo=open(nombreFichero, "r")
    data=json.load(archivo)
    archivo.close()
    return data


def escribeFichero(nombreFichero,data):
    archivo=open(nombreFichero, "w")
    json.dump(data,archivo)
    archivo.close

