import requests

api_url="http://localhost:6060/tiendas/4"

dict = {"Domicilio":"Puelto Riiiicoooo"}
response = requests.patch(api_url, json=dict)
if response.status_code == 200:
    print("Tienda editada correctamente")
else: 
    print("Error editando la tienda. Asegúrese de que su json está bien formado")