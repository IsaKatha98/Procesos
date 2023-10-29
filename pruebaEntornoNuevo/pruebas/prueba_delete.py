import requests
url= "http://localhost:5050/directores/4"
response=requests.delete (url)

print ("Código de estado: ", response.status_code)
print (response.json())