import requests

#definimos una url
url="http://localhost:5050/libros/"
dict={"id":2, "ISBN":"0000","Título":"3", "NumPaginas":3, "IdAutor":1}

response=requests.post(url, json=dict)
if (response.status_code==201):
    print(response.json())
else:
    print(response)