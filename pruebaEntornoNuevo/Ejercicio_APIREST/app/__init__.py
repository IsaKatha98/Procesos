from flask import *
from .director.routes import directorBP
from .supermercado.routes import supermercadosBP
from .users.routes import usersBP
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config['SECRET_KEY']='tu_clave'
jwt=JWTManager(app)

app.register_blueprint(usersBP,url_prefix="/users")
app.register_blueprint(directorBP, url_prefix="/directores")
app.register_blueprint(supermercadosBP, url_prefix="/supermercados")