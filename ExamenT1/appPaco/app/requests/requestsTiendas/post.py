import requests

api_url = "http://localhost:6060/tiendas"

dict = {"Domicilio":"Calle San Marcao", "Telefono":621842, "PrecioAlquiler":46214}

response = requests.post(api_url, json=dict)
if response.status_code == 201:
    print("Tienda creada correctamente")
else: 
    print("Error creando la tienda. Asegúrese de que el json es correcto")