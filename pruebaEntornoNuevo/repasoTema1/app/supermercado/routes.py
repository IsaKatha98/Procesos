from flask import *
from flask_jwt_extended import jwt_required
from app.funciones import *

#Guardamos el fichero.
ficheroSupermercados="app/ficheros/ficheroSupermercados.json"

#Creamos el bluepront
supermercadosBP= Blueprint('supermercado',__name__)

#Definimos una función para que asigne el siguiente id.
def find_next_id():
    supermercados=leeFichero(ficheroSupermercados)
    max = supermercados[0]["id"]
    for supermercado in supermercados:
        if supermercado["id"] > max:
            max = supermercado["id"]
    return max+1

#Método get que lee el fichero de los supermercados.
@supermercadosBP.get("/")
def get_supermercados():
    supermercados=leeFichero(ficheroSupermercados)
    return jsonify(supermercados)

#Método get que lee el fichero y busca un id concreto.
@supermercadosBP.get("/<int:id>")
def get_supermercado(id):
    supermercados=leeFichero(ficheroSupermercados)
    for supermercado in supermercados:
        if supermercado['id'] == id:
            return supermercado, 200
    return {"error": "Supermercado not found"}, 404

#Método post que añade un conjunto de datos al fichero.
@supermercadosBP.post("/")
#Requiere un token de usuario.
@jwt_required()
def add_supermercado():
    supermercados=leeFichero(ficheroSupermercados)
    if request.is_json:
        supermercado= request.get_json()
        supermercado["id"]=find_next_id()
        supermercados.append(supermercado)
        escribeFichero(ficheroSupermercados, supermercados)
        return supermercado, 201
    return {"error":"Request must be JSON"}, 415

#Método put que edita todos los datos de un conjunto.
#Método patch que edita un valor de un dato concreto.
@supermercadosBP.put("/<int:id>")
@supermercadosBP.patch("/<int:id>")
#Requiere un token de usuario.
@jwt_required()
def modify_supermercado(id):
    supermercados=leeFichero(ficheroSupermercados)
    if request.is_json:
        newSupermercado= request.get_json()
        for supermercado in supermercados:
            if supermercado["id"] == id:
                for element in newSupermercado:
                    supermercado[element] = newSupermercado[element]
                escribeFichero(ficheroSupermercados, supermercados)
                return supermercado, 200
            
    return {"error": "Request must be JSON"}, 415

#Método delete que borra los datos de un id concreto.
@supermercadosBP.delete("/<int:id>")
#Requiere un token de usuario.
@jwt_required()
def delete_supermercado(id):
    supermercados=leeFichero(ficheroSupermercados)
    for supermercado in supermercados:
        if supermercado['id'] == id:
            supermercados.remove(supermercado)
           
            escribeFichero(ficheroSupermercados, supermercados)
            return {}, 200
    return {"error": "Supermercado not found"}, 404