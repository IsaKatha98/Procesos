from flask import *
from flask_jwt_extended import JWTManager
#import de los blueprints.
#ejemnplo:from departamento.routes import departamentosBP

from Utils import functions

app=Flask(__name__)

#Llamamos a la función que genera la clave aleatoria.
app.config['SECRET_KEY']=functions.randomKey() # añadir función de la clave.
jwt=JWTManager(app)

#registramos los blueprints.
#app.register_blueprint(departamentosBP, url_prefix="/departamentos")


if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)