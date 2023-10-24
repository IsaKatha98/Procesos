from flask import *
from .director.routes import directorBP


app = Flask(__name__)

app.register_blueprint(directorBP, url_prefix="/directores")
