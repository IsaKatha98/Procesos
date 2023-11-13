from requests import *

#Definimos una url
url="http://localhost:5050/proyectos"

dic={"Nombre":"Bases de Datos", "Descripcion":"Asigbnatura de 1º DAM", "idDepartamento":"1"}

response=request.post(url, json=dic)

if (response.status_code==201):
    print(response)

else:
    print("Ha ocurrido un error")