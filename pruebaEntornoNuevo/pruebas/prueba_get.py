import requests
url= "https://jsonplaceholder.typicode.com/posts" 
response=requests.get (url)

print ("Código de estado: ", response.status_code)
#print (response.json())
if (response.status_code==200):
    dict= response.json()

    for clave in dict:
        print (clave, ":", dict[clave])

else:
    print("Ha habido un error")