from requests import *

#Definimos una url
url="http://localhost:5050/users"

dic={"username":"isa", "password":"1234"}

response=request.get(url, json=dic)

if (response.status_code==200):
    print(response)

else:
    print("Ha ocurrido un error")