import requests
url= "http://localhost:5050/users"

#Cuando nos pida una autenticación en el request 
#headers={"Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5OTg2NzIxMSwianRpIjoiMjQ3OGEyMDQtYThjNS00OTg4LTg2OWEtMmU1MWZiN2JmNTkxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImlzYSIsIm5iZiI6MTY5OTg2NzIxMSwiZXhwIjoxNjk5ODY4MTExfQ.G9BeS-zRK4PRNTQ89Q-OYgETEWzDZnb5XOhNGxSYnr0"}


token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNTI0NDAwMCwianRpIjoiMGY1YmUyODQtMTUwNy00MjA3LWI1YjctZTE0M2NiMzliZjM1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Imx1aXNhIiwibmJmIjoxNzA1MjQ0MDAwLCJjc3JmIjoiNzY1ZGExYWEtYzE0ZC00YjYzLWIwMjgtN2FiOWUzOTQwYWQwIiwiZXhwIjoxNzA1MjQ0OTAwfQ.hnMh2BnMNznZVznyIOMq6Xc_YYteA4qprpWWLzhuLHU"
headers2={"Authorization":f"Bearer {token}"}

dict = {"username":"paco", "password":"1100" }


response=requests.post(url, json=dict)

print ("Código de estado: ", response.status_code)
