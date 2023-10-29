import requests
url= "http://localhost:5050/directores/5"

dict = {"Nombre":"SOS"}

response=requests.put (url, json=dict)

print ("Código de estado: ", response.status_code)
print (response.json())
