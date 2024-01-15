import requests

api_url="http://localhost:6060/usuarios"

dict = {"usuario":"Luisa", "password":1234}
response = requests.post(api_url, dict)