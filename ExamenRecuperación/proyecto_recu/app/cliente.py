from flask import *
from flask_jwt_extended import jwt_required
from functions import *

#Guardamos el fichero.
ficheroClientes="proyecto_recu/ficheros/clientes.json"
ficheroPedidos="proyecto_recu/ficheros/pedidos.json"
#Creamos el blueprint
clientesBP= Blueprint('clientes',__name__)
pedidosBP=Blueprint('pedidos', __name__)

#Método put que edita todos los datos de un cliente.
@clientesBP.put("/<int:id>")
@jwt_required()
def modify_cliente(id):
    clientes=leeFichero(ficheroClientes)
    if request.is_json:
        newCliente= request.get_json()
        for cliente in clientes:
            if cliente["id_cliente"] == id:
                for element in newCliente:
                    cliente[element] = newCliente[element]
                escribeFichero(ficheroClientes, clientes)
                return cliente, 200
        return {"error":"No hay ningún cliente con ese ID"}, 404          
    return {"error": "Formato distinto a JSON"}, 415

#Método delete que borra los datos de un id concreto y los pedidos asociados a ese id.
@clientesBP.delete("/<int:id>")
@jwt_required()
def delete_cliente(id):
    clientes=leeFichero(ficheroClientes)
    pedidos= leeFichero(ficheroPedidos)
    for cliente in clientes:
        if cliente['id_cliente'] == id:
            clientes.remove(cliente)
            for pedido in pedidos:
                if pedido["id_cliente"] == id:
                    pedidos.remove(pedido)
                    escribeFichero(ficheroPedidos, pedidos)
            escribeFichero(ficheroClientes, clientes)
            return {}, 200
    return {"error": "No hay ningún cliente con ese ID"}, 404

#Método get de un id concreto y sus datos asociados en el fichero Pedidos.
@clientesBP.get('/<int:idCliente>/pedidos/<int:idPedido>')
def get_pedidoByClientes(idCliente, idPedido):
    #Hacemos una lista con los pedidos de un cliente
    listaPedidos = []
    pedidos= leeFichero(ficheroPedidos)
    for pedido in pedidos:
        if pedido["id_cliente"] == idCliente:
            listaPedidos.append(pedido)
            #dentro de esa lista, buscamos el pedido que se corresponda.
            if len(listaPedidos) > 0:
               for pedidoCliente in listaPedidos:
                   if pedidoCliente["id_pedido"]==idPedido:
                       return pedidoCliente, 200
                   return {"error":"No hay ningún pedido con ese ID"}, 404
        
    return {"error": "No hay pedidos asociados a este idCliente"}, 404

#Método que devuelve el total gastado por un cliente.
@clientesBP.get('/<int:id>/total')
def get_totalCliente(id):
    #Hacemos una lista con los pedidos de un cliente
    listaPedidos = []
    pedidos= leeFichero(ficheroPedidos)
    for pedido in pedidos:
       
        if pedido["id_cliente"] == id:
            listaPedidos.append(pedido)
    #Comprobamos que esta lista no esté vacía.
    if len(listaPedidos)>0:

        #ahora recorremos esa lista y vamos sumando al valor total.
        total=0
        for totalPedido in listaPedidos:
                
            total=(total+totalPedido["total_pedido"])
                
        return {"Total": f"{total}"}, 200
    else:   
        return {"error": "No hay pedidos asociados a este cliente"}, 404
    
        
        