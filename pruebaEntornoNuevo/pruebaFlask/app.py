from flask import *

app= Flask (__name__)



countries=[
    {"id":1, "name":"thailand", "Capital":"Bangkok", "area":513120},
    {"id":2, "name":"australia", "Capital":"Canberra", "area":7617930},
    {"id":3, "name":"Egypt", "Capital":"Cairo", "area":1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries)+1

@app.route('/')



def index():
    return 'Hola mundo!'


@app.get("/countries")


def get_countries():

    return jsonify(countries)


@app.get("/countries/<int:id>")
def getCountry(id):
    for country in countries:
        if country["id"]==id:
            return country, 200
    return {"error":"country not found"},404

@app.post("/countries")
def addCountry():
    if request.is_json:
        country= request.get_json()
        country["id"]=_find_next_id()
        countries.append(country)

        return country, 201
    
    return {"error":"Request must be JSON"}, 415



    

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)