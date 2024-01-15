from flask import *
from flask_jwt_extended import JWTManager
from Departamentos.routes import departamentosBP
from Proyectos.routes import proyectosBP
from Users.routes import usersBP


#from Proyectos import proyectosBP
#from Users import usersBP
from Utils import functions

app=Flask(__name__)

#Llamamos a la función que genera la clave aleatoria.
app.config['SECRET_KEY']=functions.randomKey() # añadir función de la clave.
jwt=JWTManager(app)

#registramos los blueprints.
app.register_blueprint(departamentosBP, url_prefix="/departamentos")
app.register_blueprint(proyectosBP, url_prefix="/proyectos")
app.register_blueprint(usersBP, url_prefix="/users")

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)