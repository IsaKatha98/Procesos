from requests import *

#Definimos una url
url="http://localhost:5050/proyectos/1"

token="" #aquí hay que hacer una paetiion get a users
headers={"Authorization": f"Bearer {token}"}

response=request.remove(url, headers=headers)

if (response.status_code==200):
    print(response)

else:
    print("Ha ocurrido un error")