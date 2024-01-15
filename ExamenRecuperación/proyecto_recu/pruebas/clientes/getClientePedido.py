import requests

#asignamos una url
url="http://localhost:5050/clientes/2/pedidos/102"


#hacemos el request
res= requests.get(url)
if (res.status_code==200):
    print(res.json())
else:
    print(res.json())