import requests
url= "https://jsonplaceholder.typicode.com/posts" 



def getAll(url) :

    response=requests.get (url)
    
    #print (response.json())
    if (response.status_code==200):
        lista= response.json()

    #una lista guarda una serie de diccionarios (clave, valor) por eso hay que hacer dos for
        for element in lista:

            for clave in element:
                print (clave, ":", element[clave])
            print()

    else:
        print("Ha habido un error")

def getPost (url, numPub):

    response= requests.get(url+"/"+numPub)
   
    if (response.status_code==200):
        dic=response.json()

        for clave in dic:
            print (clave;":","dic[clave]")

    else:
        print("Ha habido un error")

def addPost(url, userId, title, body):

    dic ={'userId': userId, 'title':title,'body':body}
    response=requests.post (url, json=dic)

    if (response.status_code==201):
       
       getPost(url+"/"+101)

    else:
        print("Ha habido un error")


def modAll(url, post, userid, title, body):


def modPost():


def deleteData():


def deletePost():
    

