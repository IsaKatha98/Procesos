import requests

#primero hacemos la request del token y lo guardamos en una variable.
urluser= url="http://localhost:5050/users"
dicuser={"username":"isa", "password":"1234"}

rget=requests.get(urluser, json=dicuser)

if (rget.status_code==200):
    token=rget.json()
    token=token ["token"]

    #asignamos una url
    url="http://localhost:5050/clientes/5"
    headers={"Authorization":f"Bearer {token}"}

    #hacemos el request
    res= requests.delete(url, headers=headers)
    if (res.status_code==200):
        print(res.json())
    else:
        print(res.json)
else:
    print("Algo ha fallado con el token")

