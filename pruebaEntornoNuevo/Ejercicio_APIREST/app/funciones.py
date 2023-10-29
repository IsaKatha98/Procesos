from flask import *

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

