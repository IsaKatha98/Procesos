from flask import *
from .director.routes import directorBP
from .supermercado.routes import supermercadosBP


app = Flask(__name__)

app.register_blueprint(directorBP, url_prefix="/directores")
app.register_blueprint(supermercadosBP, url_prefix="/supermercados")