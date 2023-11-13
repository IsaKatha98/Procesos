from flask import *
from Utils.functions import *
from flask_jwt_extended import *


#Asignamos la ubicación del fichero en una variable
ficheroProyectos="app/_Ficheros/proyectos.json"

#Hacemos el blueprint
proyectosBP=Blueprint('proyectos', __name__)

@proyectosBP.get("/")
def get_proyectos():
    proyectos=leeFichero(ficheroProyectos)
    return jsonify(proyectos)

@proyectosBP.post("/")
def crea_proyecto():
    proyectos=leeFichero(ficheroProyectos)
    if request.is_json:
        idDepartamento=request.get_json("idDepartamento")
        
        if idDepartamento!="":
            return {"error":"La petición está mal formada"}, 400
        else:
            proyecto=request.get_json()
            proyecto["id"]=find_next_id() #Falta definir esta función
            proyectos.append(proyecto)

            escribeFichero(ficheroProyectos, proyectos)

            return proyecto, 201
        
    return {"errro":"El diccionario debe estar en formato JSON"}, 415
        






@proyectosBP.delete("/<int:id>")
def borra_proyecto(id):
   proyectos=leeFichero(ficheroProyectos)
   for proyecto in proyectos:
       if proyecto["id"]==id:
           proyectos.remove(proyecto)

           return {""}, 200
       return {"error":"No se ha encontrado el proyecto"}, 404 
