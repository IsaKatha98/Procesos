from flask import *
from utils.funciones import *
from flask_jwt_extended import *

empleadosBP = Blueprint('empleados', __name__)

#definimos la ruta para el fichero de empleados
ficheroEmpleados="GestionTiendaEmpleados/datosTiendas/empleados.json"

@empleadosBP.get('/')
def getAll():
    empleados = leeFichero(ficheroEmpleados)
    return jsonify(empleados)

@empleadosBP.get('/<int:id>')
def getEmpleado(id):
    empleados = leeFichero(ficheroEmpleados)
    for empleado in empleados:
        if(empleado["Id"] == id):
            return empleado, 200
    return{"error":"El empleado no existe"}

@empleadosBP.post('/')
@jwt_required
def insertEmpleado():
    empleados = leeFichero(ficheroEmpleados)
    if request.is_json:
        empleado = request.get_json()
        newId = find_next_id(ficheroEmpleados)
        empleado["Id"] = newId
        empleados.append(empleado)
        escribeFichero(ficheroEmpleados, empleados)
        return empleado, 201
    return {"error":"Request must be json"}, 400

@empleadosBP.put('<int:id>')
@empleadosBP.patch('<int:id>')
@jwt_required
def editaEmpleado(id):
    empleados = leeFichero(ficheroEmpleados)
    if request.is_json:
        empleadoEdit = request.get_json()
        for empleado in empleados:
            if(empleado["Id"] == id):
                for elemento in empleadoEdit:
                    empleado[elemento] = empleadoEdit[elemento]
                    escribeFichero(ficheroEmpleados, empleados)
                return empleado, 200
        return {"error":"El empleado insertado no existe"},404
    return{"error":"Request must be json"}, 400

@empleadosBP.delete('<int:id>')
@jwt_required
def eliminaEmpleado(id):
    empleados = leeFichero(ficheroEmpleados)
    for empleado in empleados:
        if(empleado["Id"] == id):
            empleados.remove(empleado)
            escribeFichero(ficheroEmpleados, empleados)
            return {}, 200
    return{"error":"El empleado no existe"}, 400