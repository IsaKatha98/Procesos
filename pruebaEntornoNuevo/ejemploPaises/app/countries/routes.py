from flask import *
from app.funciones import *

#Las rutas relativas van sin barra
nombreFichero="ejemploPaises\\countries.json"

#Nos creamos el blueprint
countriesBP=Blueprint ('countries',__name__)

def _find_next_id():
    countries=leeFichero()
    return max(country["id"] for country in countries)+1

@countriesBP.get("/")
def get_countries():
    countries=leeFichero()
    return jsonify(countries)
