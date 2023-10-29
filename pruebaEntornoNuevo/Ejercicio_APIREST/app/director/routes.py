from flask import *
from app.funciones import *

#Guardamos el fichero.
ficheroDirectores="app/ficheros/ficheroDirectores.json"
ficheroSupermercados="app/ficheros/ficheroSupermercados.json"
#Creamos el bluepront
directorBP= Blueprint('directores',__name__)

#Definimos una función para que asigne el siguiente id.
def find_next_id():
    directores=leeFichero(ficheroDirectores)
    max = directores[0]["id"]
    for director in directores:
        if director["id"] > max:
            max = director["id"]

    return max+1


@directorBP.get("/")
def get_directores():
    directores=leeFichero(ficheroDirectores)
    return jsonify(directores)


@directorBP.get("/<int:id>")
def get_director(id):
    directores=leeFichero(ficheroDirectores)
    for director in directores:
        if director['id'] == id:
            return director, 200
    return {"error": "Director not found"}, 404

@directorBP.post("/")
def add_director():
    directores=leeFichero(ficheroDirectores)
    if request.is_json:
        director= request.get_json()
        director["id"]=find_next_id()
        directores.append(director)
        escribeFichero(ficheroDirectores, directores)

        return director, 201
    
    return {"error":"Request must be JSON"}, 415

@directorBP.put("/<int:id>")
@directorBP.patch("/<int:id>")
def modify_director(id):
    directores=leeFichero(ficheroDirectores)
    if request.is_json:
        newDirector= request.get_json()
        for director in directores:
            if director["id"] == id:
                for element in newDirector:
                    director[element] = newDirector[element]
                escribeFichero(ficheroDirectores, directores)
                return director, 200
            
    return {"error": "Request must be JSON"}, 415

@directorBP.delete("/<int:id>")
def delete_director(id):
    directores=leeFichero(ficheroDirectores)
    supermercados= leeFichero(ficheroSupermercados)
    for director in directores:
        if director['id'] == id:
            directores.remove(director)
            for supermercado in supermercados:
                if supermercado["IdDirector"] == id:
                    supermercados.remove(supermercado)
                    escribeFichero(ficheroSupermercados, supermercados)
            escribeFichero(ficheroDirectores, directores)
            return {}, 200
    return {"error": "Director not found"}, 404

@directorBP.get('/<int:id>/supermercados')
def get_supermercados(id):
    list = []
    supermercados= leeFichero("app/ficheros/ficheroSupermercados.json")
    for supermercado in supermercados:
        if supermercado["IdDirector"] == id:
            list.append(supermercado)
    if len(list) > 0:
        return list, 200
    else:
        return {"error": "No hay supermercados asociados a este id"}, 404