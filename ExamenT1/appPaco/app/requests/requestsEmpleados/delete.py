import requests

api_url = "http://localhost:6060/empleados/4"
response = requests.delete(api_url)

if response.status_code == 200:
    print("Empleado eliminado correctamente")
else: 
    print("Error eliminando el empleado")