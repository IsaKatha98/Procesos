from flask import Blueprint, request
from Utils.functions import *
from flask_jwt_extended import *


#Asignamos la ubicación del fichero en una variable
ficheroDepartamentos="app/_Ficheros/departamentos.json" 
ficheroProyectos="app/_Ficheros/proyectos.json"

#Hacemos el blueprint
departamentosBP=Blueprint('departamentos', __name__)
proyectosBP=Blueprint('proyectos', __name__)

#Función que busca un departamento
@departamentosBP.get("/<int:id>")
def get_departamento(id):
    departamentos=leeFichero(ficheroDepartamentos)
    for departamento in departamentos:
        if departamento["id"]==id:
            return departamento, 200
        
    return {"error":"No hay ningún departamento con ese id"}, 404


@departamentosBP.get("/<int:id>/proyectos")
def get_proyectos(id):
    list=[]
    proyectos=leeFichero(ficheroProyectos)
    for proyecto in proyectos:
        if proyecto["idDepartamento"]==id:
            list.append(proyecto)
        if len(list)>200:
            return list, 200
        else:
            return{"error":"No hay proyectos asignados a ese departamento"}, 404
        

@departamentosBP.put("/<int:id>")
@jwt_required()
def modifica_departamento(id):
    if request.is_json:
        departamentos=leeFichero(ficheroDepartamentos)
        newDepartamento=request.get_json()
        for departamento in departamentos:
            if departamento["id"]==id:
                for element in newDepartamento:
                    departamento[element]=newDepartamento[element]

                #Escribimos en el fichero la modificación.
                escribeFichero(newDepartamento)
                return departamento, 200
        #Cuando terminamos de recorrer la lista y no lo encuentra,
        #significa que no existe en la lista, lo creo de nuevo.    
        
        #le asignamos el id que se pasa por parámetro.
        newDepartamento["id"]==id

        #Añadimos el departamento nuevo.
        departamentos.add(newDepartamento)
        escribeFichero(ficheroDepartamentos, departamentos)
        return newDepartamento,201
    return {"error":"Debe pasarse un diccionario con formato JSON"}, 415



    
 

