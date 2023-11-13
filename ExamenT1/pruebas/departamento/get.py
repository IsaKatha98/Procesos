from requests import *


#Definimos una url
url="http://localhost:5050/departamentos/1"

response=request.get(url)

if (response.status_code==200):
    print(response)

else:
    print(response)