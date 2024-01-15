import requests

#Definimos una url
url="http://localhost:5050/proyectos/2"

token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNTI1NzYyMywianRpIjoiMzQ4ZGVkNjEtY2UxZS00NWRhLTgyYTctYTNhNWE2NmJhNzdjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImlzYSIsIm5iZiI6MTcwNTI1NzYyMywiY3NyZiI6ImYzNDVkMTJhLWJhNTctNDQwMC1hYWU0LWQzNzBmNDA3OTM1ZCIsImV4cCI6MTcwNTI1ODUyM30.H9XIn-On_AFtAuVkjzM45w6BDJl1eri7U1r8T4-RwEk" #aquí hay que hacer una paetiion get a users
headers={"Authorization": f"Bearer {token}"}

response=requests.delete(url, headers=headers)

if (response.status_code==200):
    print(response.json())

else:
    print("Ha ocurrido un error")