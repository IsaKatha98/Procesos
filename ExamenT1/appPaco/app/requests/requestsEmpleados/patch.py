import requests

api_url="http://localhost:6060/empleados/4"

dict = {"Nombre":"Luis"}
response = requests.patch(api_url, json=dict)
if response.status_code == 200:
    print("Empleado editado correctamente")
else: 
    print("Error editando el empleado. Asegúrese de que su json está bien formado")