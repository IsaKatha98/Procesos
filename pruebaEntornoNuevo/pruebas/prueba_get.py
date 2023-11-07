import requests
url= "https://jsonplaceholder.typicode.com/posts" 

#Cuando nos pida una autenticación en el request 
token="token_creado"
headers={"Authorization":"Bearer"+token}

response=requests.get (url, headers=headers)

print ("Código de estado: ", response.status_code)
#print (response.json())
if (response.status_code==200):
    dict= response.json()

    for clave in dict:
        print (clave, ":", dict[clave])

else:
    print("Ha habido un error")