import requests

api_url = "http://localhost:6060/empleados"

dict = {"Nombre":"Maria", "Apellidos":"Huertas", "Telefono":746284, "Correo":"mariahuertas@gmail.com", "NumCuenta":74628, "IdTenda":2}

response = requests.post(api_url, json=dict)
if response.status_code == 201:
    print("Empleado creado correctamente")
else: 
    print("Error creando el empleado. Asegúrese de que el json es correcto")