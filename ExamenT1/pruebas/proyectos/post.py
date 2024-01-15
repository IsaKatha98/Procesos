import requests

#Definimos una url
url="http://localhost:5050/proyectos"

dic={"id":"3", "Nombre":"Bases de Datos", "Descripcion":"Asignatura de 1º DAM", "idDepartamento":"1"}

response=requests.post(url, json=dic)

if (response.status_code==201):
    print(response)

else:
    print("Ha ocurrido un error")