import requests

url= "http://localhost:5050/countries" 



dict = {'name':"Spain", 'capital':"Madrid", 'area':50000 }

response=requests.post (url, json=dict)

print ("Código de estado: ", response.status_code)
print (response.json())
