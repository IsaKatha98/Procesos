import requests

#Definimos una url
url="http://localhost:5050/proyectos"

response=requests.get(url)

if (response.status_code==200):
    print(response.json())

else:
    print("Ha ocurrido un error")