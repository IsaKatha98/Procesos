import requests

api_url = "http://localhost:6060/tiendas/4"
response = requests.delete(api_url)

if response.status_code == 200:
    print("Tienda eliminada correctamente")
else: 
    print("Error eliminando la tienda")