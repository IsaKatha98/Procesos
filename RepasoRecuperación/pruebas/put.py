import requests

#definimos una url
url="http://localhost:5050/libros/1"
dict={"ISBN":"0000","Título":"gueno", "NumPaginas":3, "IdAutor":1}

response=requests.put(url, json=dict)
if (response.status_code==200):
    print(response.json())
else:
    print(response)