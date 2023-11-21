from Utils.functions import *
from flask import Blueprint
from requests import *
import bcrypt
from flask_jwt_extended import *

#Asignamos la ubicación del fichero en una variable
ficheroUsers="app/_Ficheros/users.json"

#Hacemos el blueprint
usersBP=Blueprint('users', __name__)

@usersBP.post("/")
def registroUser():
    users=leeFichero(ficheroUsers)
    if request.is_json:
        user=request.get_json()
        password=user["password"].encode('utf-8')
        salt=bcrypt.gensalt()
        hashPassword=bcrypt.hashpw(password,salt).hex()
        user["password"]=hashPassword
        users.append(user)
        escribeFichero(ficheroUsers, users)

        #No hacía falta generar el token, porque no había que devolverlo.
        #token=create_access_token(identity=user["username"])
        return {"Se ha registrado correctamente"}, 201
    
    return{"error":"El diccionario debe estar en formato JSON"}, 415


@usersBP.get("/")
def loginUser():
    users=leeFichero(ficheroUsers)
    if request.is_json:
        user=request.get_json()
        username=user["username"]
        password=user["password"].encode('utf-8')
        for userFile in users:
            if userFile["username"]==username:
                passwordFile=userFile["password"]

                if bcrypt.checkpw(password, bytes.fromhex(passwordFile)):
                    token=create_access_token(identity=username)
                    return{"token":token}, 200
                else:
                    return{"error":"No authorized"}, 401
        return{"error":"Usuario no encontrado"}, 404
    return{"error":"El diccionario debe estar en formato JSON"}, 415


