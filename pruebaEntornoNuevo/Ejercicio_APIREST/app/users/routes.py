import bcrypt
from flask import *
from flask_jwt_extended import create_access_token
from app.funciones import *

ficheroUsers="../app/ficheros/ficheroUsers.json"

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
        username=user['username']
        password=user['password'].encode('utf-8')
        for userFile in users:
            if userFile['username']==username:
                passwordFile=userFile['password']
                if bcrypt.checkpw(password, bytes.fromhex(passwordFile)):
                    token= create_access_token(identity=username)
                    return {"token":token}, 200
                else:
                    return {"error":"no authorized"}, 401
                
            return {"error":"User not found"}, 404
        return {"error":"Request must be JSON"}, 415