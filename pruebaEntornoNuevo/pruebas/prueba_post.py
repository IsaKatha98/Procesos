import requests
url= "http://localhost:5050/directores"



dict = {"DNI":"33333389K", "Nombre":"ayuda","Apellidos":"sos","email":"sosayuda@gmail.com"}

response=requests.post (url, json=dict)

print ("Código de estado: ", response.status_code)
print (response.json())


