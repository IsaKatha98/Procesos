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
    dic={ "id_cliente": 5,
        "nombre_cliente": "Katharina Loerzer",
        "direccion_envio": "Avenida Principal 567, Ciudad B",
        "correo_electronico": "isaka@example.com",
        "numero_telefono": "012-345-6789"}
    headers={"Authorization":f"Bearer {token}"}

    #hacemos el request
    res= requests.put(url, headers=headers, json=dic)
    if (res.status_code==200):
        print(res.json())
    else:
        print(res.json)
else:
    print("Algo ha fallado con el token")

