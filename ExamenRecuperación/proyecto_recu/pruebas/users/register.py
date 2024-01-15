import requests

#asignamos una url
url="http://localhost:5050/users"
dicuser={"username":"isa", "password":"1234"}


#hacemos el request
res= requests.post(url, json=dicuser)
if (res.status_code==200):
    print(res.json())
else:
    print(res)