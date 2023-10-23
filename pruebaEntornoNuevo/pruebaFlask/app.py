from flask import *

app= Flask (__name__)

#Las rutas relativas van sin barra
fichero="pruebaFlask\\countries.json"

#Lectura del fichero.
def leeFichero():
    archivo=open(fichero, "r")
    countries=json.load(archivo)
    archivo.close()
    return countries


def escribeFichero(countries):
    archivo=open(fichero, "w")
    json.dump(countries,archivo)
    archivo.close


def _find_next_id():
    countries=leeFichero()
    return max(country["id"] for country in countries)+1

@app.route('/')



def index():
    return 'Hola mundo!'


@app.get("/countries")
def get_countries():
    countries=leeFichero()
    return jsonify(countries)


@app.get("/countries/<int:id>")
def getCountry(id):
    countries=leeFichero()
    for country in countries:
        if country["id"]==id:
            return country, 200
    return {"error":"country not found"},404

@app.post("/countries")
def addCountry():
    countries=leeFichero()
    
    if request.is_json:
        country= request.get_json()
        country["id"]=_find_next_id()
        countries.append(country)
        escribeFichero(countries)
        return country, 201
    
    return {"error":"Request must be JSON"}, 415

@app.put ("/countries/<int:id>")
@app.patch ("/countries/<ind:id>")

def modifyCountry(id):
    countries=leeFichero()
    if request.is_json:
        newCountry =request.get_json()

        for country in countries:
            if country["id"]==id:
                for element in newCountry:
                    country[element]=newCountry[element]

                escribeFichero(countries)
                return country, 200
            return {"error":"Country not found"},404
        return {"error":"Request must be JSON"}, 415



@app.delete("/countries/<int:id>")

def deleteCountry(id):
    countries=leeFichero()
    for country in countries:
        if country["id"]==id:
            countries.remove(country)
            escribeFichero(countries)

            return "{}",200
    
    return {"error":"Country not found"},404




    

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)