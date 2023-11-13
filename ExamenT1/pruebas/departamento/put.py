import requests

#Definimos una url
url="http://localhost:5050/departamentos/1"

token="" #aquí hay que hacer una paetiion get a users
headers={"Authorization": f"Bearer {token}"}

dic={"Nombre":"Departamento de Procesos y Servicios","Responsable":"Elena Rivero"}

response=requests.put(url, headers=headers, json=dic)

if (response.status_code==200 or response.status_code==201):
    print(response.json)

else:
    print("Ha ocurrido un error")