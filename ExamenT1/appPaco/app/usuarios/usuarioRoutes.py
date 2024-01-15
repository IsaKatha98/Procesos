from flask import *
import bcrypt
from utils.funciones import *
from flask_jwt_extended import *

ficheroUsuarios = "GestionTiendaEmpleados/datosTiendas/usuarios.json"

usuariosBP = Blueprint('usuarios', __name__)

@usuariosBP.get('/')
def getUsuario():
    usuarios = leeFichero(ficheroUsuarios)
    if request.is_json:
        usuario = request.get_json()
        password = usuario['password'].encode('utf-8')
        for user in usuarios:
            if user['usuario'] == usuario['usuario']:
                passwordUsuarioExistente = user['password']
                if bcrypt.checkpw(password, bytes.fromhex(passwordUsuarioExistente)):
                    token = create_access_token(identity=usuario['usuario'])
                    return{'token':token}, 200
                else:
                    return {'error':"La contraseña introducida no es válida"}, 401
       
        return {"error":"El usuario introducido no existe"},404
    return{"error":"Request must be json"}, 415

@usuariosBP.post('/')
def postUsuario():
    usuarios = leeFichero(ficheroUsuarios) #leemos el fichero de usuarios
    if request.is_json: #si la request está bien formada
        usuario = request.get_json() #tomamos el json
        password = usuario['password'].encode('utf-8') #convertimos la contraseá en un conjunto de bytes
        salt = bcrypt.gensalt() #generamos la sal
        hashPassword = bcrypt.hashpw(password, salt).hex() #calculamos el hash y lo convertimos en hexadecimal
        usuario['password'] = hashPassword #machacamos el campo contraseña con el hash calculado
        usuarios.append(usuario) #añadimos el usuario a la lista de usuarios
        escribeFichero(ficheroUsuarios, usuarios) #Reescribimos el fichero de usuarios
        token = create_access_token(identity=usuario['usuario'])#creamos el token y el codigo 201
        return {'token':token}, 201
    return {"error":"Request must be json"},415