from flask import *
from app.funciones import *

#nos creamos una lista con los diccionarios
dicDirector =[
    {"id":1, "DNI":"12345678A", "Nombre":"Alberto", "Apellidos":"Núnez Feijóo"},
    {"id":2, "DNI":"22222222B", "Nombre":"Mariano", "Apellidos":"Rajoy"}
]

#Creamos el bluepront
directorBP= Blueprint('directores',__name__)

@directorBP.get("/")
def get_directores():
    
    return jsonify(dicDirector)

@directorBP.get("/<int:id>")
def get_director(id):
    for director in dicDirector:
        if director['id'] == id:
            return director, 200
    return {"error": "Director not found"}, 404