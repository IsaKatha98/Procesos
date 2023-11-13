from requests import *

#Definimos una url
url="http://localhost:5050/proyectos"

response=request.get(url)

if (response.status_code==200):
    print(response)

else:
    print("Ha ocurrido un error")