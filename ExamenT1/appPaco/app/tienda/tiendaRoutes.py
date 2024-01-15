from flask import *
from utils.funciones import *
from flask_jwt_extended import *


tiendasBP = Blueprint('tiendas', __name__)

#Variables en las que guardamos las rutas de los ficheros con los datos de la APIs
ficheroEmpleados="GestionTiendaEmpleados/datosTiendas/empleados.json"
ficheroTiendas="GestionTiendaEmpleados/datosTiendas/tiendas.json"

@tiendasBP.get('/') #decorador para indicar que vamos a iniciar el código del método get
def getTiendas():
    tiendas = leeFichero(ficheroTiendas) #Extraemos los datos del fichero
    return jsonify(tiendas) #Los devolvemos en formato json

@tiendasBP.get("/<int:id>") #Vamos a crear la función para buscar tiendas específicas. Indicamos que se le pasa un id por parámetros
def getTienda(id): 
    tiendas = leeFichero(ficheroTiendas) #Extraemos los datos del fichero de tiendas
    for tienda in tiendas: #Iteramos por cada elemento json del fichero
        if(tienda["Id"] == id): #Si el id de algún elemento json coincide con el id pasado por parámetros
            return tienda, 200 #Devolvemos dicho elemento con el código 200, indicando éxito en la búsqueda
    return{"error":"Tienda no encontrada"} #Si no, indicamos que ha habido un error

@tiendasBP.post('/')
@jwt_required
def postTienda():
    tiendas = leeFichero(ficheroTiendas) #Leemos el fichero y guardamos los datos en una variable
    if request.is_json: #Si la request es correcta
        tienda = request.get_json() #Guardamos el objeto de la request en una variable
        newId = find_next_id(ficheroTiendas) #Conseguimos el nuevo id
        tienda["Id"] = newId #Asignamos el id a la nueva tienda
        tiendas.append(tienda) #La añadimos a la lista de tiendas
        escribeFichero(ficheroTiendas, tiendas) #Machacamos el fichero de tiendas
        return tienda, 201 #Devolvemos un mensaje de éxito
    return {"error": "Request must be json"}, 400 #Si no entra en el if, es que la request está mal formada

@tiendasBP.put('/<int:id>') #Decoradores para indicar que vamos a escribir las funciones de put y patch
@tiendasBP.patch('/<int:id>')
@jwt_required
def editaTienda(id): #A ambos se les pasa un id por parámetros
    tiendas = leeFichero(ficheroTiendas) #Tomamos los datos del fichero de tiendas
    if request.is_json: #Si la request está bien formada
        newTienda = request.get_json() #Guardamos la tienda actualizada en una variable
        for tienda in tiendas: #Iteramos las tiendas hasta encontrar una cuyo id encaje con el pasado por parámetros
            if tienda["Id"] == id:
                for element in newTienda: #A cada elemento de la tienda le asignamos el elemento de la tienda actualizada
                    tienda[element] = newTienda[element] 
                escribeFichero(ficheroTiendas, tiendas) #Machacamos el fichero con la tienda actualizada
                return tienda, 200 #Si todo ha salido bien, mostramos un mensaje de éxito
        return {"error": "Esa tienda no existe"} #Si no entra en el if del primer bucle for, es que la tienda no se ha encontrado
    return {"error":"Request must be json"} #Si no entra en el primer bucle for, es que la request es errónea

@tiendasBP.delete('/<int:id>') #Decorador para indicar que vamos a codificar el método delete
@jwt_required
def eliminaTienda(id): 
    tiendas = leeFichero(ficheroTiendas) #Cogemos los datos del fichero de las tiendas 
    for tienda in tiendas: #Iteramos por los elementos de la lista recogida
        if tienda["Id"] == id: #Si el id de la tienda en la que estamos iterando es igual al pasado por parámetros
            tiendas.remove(tienda) #Eliminamos la tienda de la lista
            escribeFichero(ficheroTiendas, tiendas) #Machacamos el fichero de tiendas
            return {}, 200
    return {"error":"Esa tienda no existe"} #Si no se entra en el if, la tienda no existe

@tiendasBP.get('/<int:id>/empleados') #Decorador para indicar que vamos a sacar los empleados de una tienda en concreto
def getEmpleadosTienda(id):
    listaEmpleados = [] #Lista donde vamos a ir guadando los empleados que encontremos de la tienda introducida
    empleados = leeFichero(ficheroEmpleados) #Sacamos los datos de los empleados del fichero correspondiente
    for empleado in empleados: #Iteramos por cada empleado 
        if empleado["IdTienda"] == id: #Si el id de la tienda del empleado iterado coincide con el id pasado por parámetros
            listaEmpleados.append(empleado) #Lo metemos en la lista
    if len(listaEmpleados) > 0: #Si al terminar de iterar la lista tiene elementos, devolvemos un mensaje de éxito junto a la lista 
        return listaEmpleados, 200
    else: #En cambio, si la lista no tiene empleados, es que la tienda o no existe o aún no ha contratado a nadie
        return {"error":"No existen empleados para esa tienda o no existe esa tienda"} 