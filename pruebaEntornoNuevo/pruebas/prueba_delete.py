import requests
url= "http://localhost:5050/directores/5"

token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5OTg2ODQ0NywianRpIjoiMTEyYjFjY2ItYTlmZC00ZjUyLWIwMWYtNmVhZmExZTQwMDYyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImlzYSIsIm5iZiI6MTY5OTg2ODQ0NywiZXhwIjoxNjk5ODY5MzQ3fQ.joB1vxPbbSQCJM_C5vGsT1bdtxKyOnSSXQ4WkHBIaIs"
headers={"Authorization":f"Bearer {token}"}

headers2={"Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5OTg2ODQ0NywianRpIjoiMTEyYjFjY2ItYTlmZC00ZjUyLWIwMWYtNmVhZmExZTQwMDYyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImlzYSIsIm5iZiI6MTY5OTg2ODQ0NywiZXhwIjoxNjk5ODY5MzQ3fQ.joB1vxPbbSQCJM_C5vGsT1bdtxKyOnSSXQ4WkHBIaIs"}




response=requests.delete (url, headers=headers)

print ("Código de estado: ", response.status_code)
print (response.json())