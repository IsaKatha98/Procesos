from flask import *
from flask_jwt_extended import *
from functions import *

#Guardamos el fichero.
ficheroPedidos="proyecto_recu/ficheros/pedidos.json"

#Creamos el blueprint
pedidosBP=Blueprint('pedidos', __name__)

#Definimos una función para que asigne el siguiente id.
def find_next_id():
    pedidos=leeFichero(ficheroPedidos)
    max = pedidos[0]["id_pedido"]
    for pedido in pedidos:
        if pedido["id_pedido"] > max:
            max = pedido["id_pedido"]

    return max+1

#Método post que añade un pedido.
@pedidosBP.post("/")
@jwt_required()
def add_pedido():
    pedidos=leeFichero(ficheroPedidos)
    if request.is_json:
        pedido = request.get_json()
        #hay que comprobar que el idCliente existe.
        clientes= leeFichero("proyecto_recu/ficheros/clientes.json")
        for cliente in clientes:
            if pedido["id_cliente"]==cliente["id_cliente"]:
                #asignamos un id al pedido
                pedido["id_pedido"]=find_next_id()
                pedidos.append(pedido)
                escribeFichero(ficheroPedidos, pedidos)
              
                return pedido, 201
        
        return {"error":"idCliente no existe"}, 404
    return {"error": "Debe estar en formato JSON"}, 415
