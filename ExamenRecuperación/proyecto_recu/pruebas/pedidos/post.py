import requests

#primero hacemos la request del token y lo guardamos en una variable.
urluser= url="http://localhost:5050/users"
dicuser={"username":"isa", "password":"1234"}

rget=requests.get(urluser, json=dicuser)

if (rget.status_code==200):
    token=rget.json()
    token=token ["token"]

    #asignamos una url
    url="http://localhost:5050/pedidos/"
    dic={ "id_pedidos":106, "fecha_pedido": "2024-01-13",
        "total_pedido": 10.0,
        "estado_pedido": "En proceso",
        "id_cliente": 3 }
    headers={"Authorization":f"Bearer {token}"}

    #hacemos el request
    res= requests.post(url, headers=headers, json=dic)
    if (res.status_code==201):
        print(res.json())
    else:
        print(res.json)
else:
    print("Algo ha fallado con el token")

