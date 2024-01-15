import requests

api_url = "http://localhost:6060/empleados/2"

dict = {"Nombre": "Adama", "Apellidos":"Traore", "Telefono":85738, "Correo":"adamatraore@gmail.com", "NumCuenta":135412, "IdTienda":1}
response = requests.put(api_url, json=dict)
if response.status_code == 200:
    print("Empleado editado correctamente")
else:
    print("Error editando el empleado. Asegúrese de que su json está bien formado")