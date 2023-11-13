import requests
url= "http://localhost:5050/supermercados" 

dict={"username":"javi","password":"1111"}

#token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5OTg2NzIxMSwianRpIjoiMjQ3OGEyMDQtYThjNS00OTg4LTg2OWEtMmU1MWZiN2JmNTkxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImlzYSIsIm5iZiI6MTY5OTg2NzIxMSwiZXhwIjoxNjk5ODY4MTExfQ.G9BeS-zRK4PRNTQ89Q-OYgETEWzDZnb5XOhNGxSYnr0"
#headers2={"Authorization":f"Bearer {token}"}

response=requests.get(url)

print ("Código de estado: ", response.status_code)
#print (response.json())
if (response.status_code==200):
    print(response.json())

else:
    print("Ha habido un error")