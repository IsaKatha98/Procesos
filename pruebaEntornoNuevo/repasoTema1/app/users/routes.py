import bcrypt
from flask import *
from flask_jwt_extended import create_access_token
from app.funciones import *

ficheroUsers="app/ficheros/ficheroUsers.json"

usersBP=Blueprint('users',__name__)

#Definimos una función para que asigne el siguiente id.
def find_next_id():
    users=leeFichero(ficheroUsers)
    max = users[0]["id"]
    for user in users:
        if user["id"] > max:
            max = user["id"]
    return max+1


@usersBP.post('/')
def registerUser():
    users=leeFichero(ficheroUsers)
    if request.is_json:
        user=request.get_json()
        password=user['password'].encode('utf-8')
        salt=bcrypt.gensalt()
        hashPassword=bcrypt.hashpw(password,salt).hex()
        user['password']=hashPassword
        users.append(user)
        escribeFichero(ficheroUsers,users)
        token=create_access_token(identity=user['username'])
        return{'token':token},201
    
    return{"error":"Request must be JSON"}, 415

@usersBP.get('/')
def loginUser():
    users=leeFichero(ficheroUsers)
    if request.is_json:
        user=request.get_json()
        #cogemos el usuario y la contraseña y la asignamos a unas variables
        username=user['username']
        password=user['password'].encode('utf-8')
        #buscamos ese user
        for userFile in users:
            #si lo encuentra cogemos la contraseña que hay en el fichero.
            if userFile['username']==username:
                #si la contraseña que nos llega es igual que al que hay en el json
                passwordFile=userFile['password']
                #comparamos
                if bcrypt.checkpw(password, bytes.fromhex(passwordFile)):
                    #generamos el token y lo devolvemos.
                    token= create_access_token(identity=username)
                    return {"token":token}, 200
                else:
                    return {"error":"no authorized"}, 401
                
        return {"error":"User not found"}, 404
    return {"error":"Request must be JSON"}, 415