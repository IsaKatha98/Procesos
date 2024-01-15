import requests

api_url = "http://localhost:6060/tiendas/2"

dict = {"Domicilio": "República Dominicana", "Telefono":8888, "PrecioAlquiler":23456}
response = requests.put(api_url, json=dict)
if response.status_code == 200:
    print("Tienda editada correctamente")
else:
    print("Error editando la tienda. Asegúrese de que su json está bien formado")