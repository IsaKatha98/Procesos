from flask import *
from app.funciones import *

#Guardamos el fichero.
ficheroSupermercados="app/ficheros/ficheroSupermercados.json"

#Creamos el bluepront
supermercadosBP= Blueprint('supermercados',__name__)

#Definimos una función para que asigne el siguiente id.
def find_next_id():
    supermercados=leeFichero(ficheroSupermercados)
    max = supermercados[0]["id"]
    for supermercado in supermercados:
        if supermercado["id"] > max:
            max = supermercado["id"]

    return max+1


@supermercadosBP.get("/")
def get_supermercados():
    supermercados=leeFichero(ficheroSupermercados)
    return jsonify(supermercados)

@supermercadosBP.get("/<int:id>")
def get_supermercado(id):
    supermercados=leeFichero(ficheroSupermercados)
    for supermercado in supermercados:
        if supermercado['id'] == id:
            return supermercado, 200
    return {"error": "Supermercado not found"}, 404

@supermercadosBP.post("/")
def add_supermercado():
    supermercados=leeFichero(ficheroSupermercados)
    if request.is_json:
        supermercado= request.get_json()
        supermercado["id"]=find_next_id()
        supermercados.append(supermercado)
        escribeFichero(ficheroSupermercados, supermercados)

        return supermercado, 201
    
    return {"error":"Request must be JSON"}, 415

@supermercadosBP.put("/<int:id>")
@supermercadosBP.patch("/<int:id>")
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

@supermercadosBP.delete("/<int:id>")
def delete_supermercado(id):
    supermercados=leeFichero(ficheroSupermercados)
    for supermercado in supermercados:
        if supermercado['id'] == id:
            supermercados.remove(supermercado)
           
            escribeFichero(ficheroSupermercados, supermercados)
            return {}, 200
    return {"error": "Supermercado not found"}, 404