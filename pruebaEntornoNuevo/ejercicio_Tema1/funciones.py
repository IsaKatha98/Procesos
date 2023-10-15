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
            print (clave ,":",dic[clave])
            print()


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

    #escribimos el post con la info nueva
    dic ={'userId': userId, 'title':title,'body':body}

    #modificamos la info del post que se ha pedido
    response=requests.put(url+"/"+post, json=dic)

    if (response.status_code==200):
        
        #si ha ido bien, llamamos a ese post
        getPost(url+"/"+post)


    else:
        print("Ha habido un error")


def modPost(url, post, type, data):

    #en caso de que type sea userId, tenemos que pasar data a it.
    if type=="userbody":
        data=int(data)
    
    #escribimos lo que vayamnos a modificar
    dic={type:data}

    #llamamos al post.
    response=requests.patch(url+"/"+post, json=dic)

    if (response.status_code==200):
        
        #si ha ido bien, llamamos a ese post
        getPost(url+"/"+post)


    else:
        print("Ha habido un error")


def deletePost(url, post):

    response=requests.delete(url+"/"+post)

    if (response.status_code==200):
        
        #si ha ido bien, confirmamos
        print("Se confirma el borrado del post:",post)


    else:
        print("Ha habido un error")

    

