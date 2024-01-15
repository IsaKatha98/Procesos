import requests

#definimos una url
url="http://localhost:5050/autores/1"

response=requests.get(url)
if (response.status_code==200):
    print(response.json())
else:
    print(response)