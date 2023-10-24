from flask import *

#Lectura del fichero.
def leeFichero(nombreFichero):
    archivo=open(nombreFichero, "r")
    countries=json.load(archivo)
    archivo.close()
    return countries


def escribeFichero(countries,nombreFichero):
    archivo=open(nombreFichero, "w")
    json.dump(countries,archivo)
    archivo.close

