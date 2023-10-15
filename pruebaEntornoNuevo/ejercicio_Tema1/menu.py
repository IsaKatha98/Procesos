from funciones import*
url= "https://jsonplaceholder.typicode.com/posts" 

#hacemos las variables
num=1

while num!=0 :

     print("1-> Mostrar todas las publicaciones")
     print("2-> Mostrar una publicación concreta")
     print("3-> Añadir una nueva publicación")
     print("4-> Modificar todos los datos de una publicación")
     print("5-> Modificar un dato concreto")
     print("6-> Eliminar una publicación ")
     print("0->Salir")
     print ("Seleccione su opción:") 
     
     num=int (input())
     
     if num==1:
          #mostrar todos los posts
          getAll(url)

     elif num==2: 
          print ("Introduzca el número del post que desea buscar: ")
          post= int (input())

          #mostrar un post en concreto
          getPost(url, post)

     elif num==3:

        print ("Introduzca los siguientes datos: ")
        print("userId: ")
        userId= int(input())
        print("Title: ")
        title= input()
        print("Body: ")
        body= input()

        #añadimos un post nuevo
        addPost(url, userId, title, body)

     elif num==4: 
        
        print ("Introduzca el número del post que desea buscar: ")
        post= int (input())

        
        print ("Introduzca los siguientes datos: ")
        print("userId: ")
        userId= int(input())
        print("Title: ")
        title= input()
        print("Body: ")
        body= input()

        #modificamos un post
        modAll(url, post, userId,title,body)

     elif num==5:
         
         print ("Introduzca el número del post que desea buscar:")
         post=int (input())

         print ("Introduzca qué tipo de dato quiere cambiar (userId, title, body):")
         type=(input())

         print("Introduzca el dato modificado:")
         data=(input())

         #modificamos un dato concreto de esa publicación.
         modPost(url, post, type, data)

     elif num==6:

          print("Introduzca el número del post que quiere eliminar:")
          post=int(input())

          deletePost (url, post)
     
     elif num==0:
         
         print ("El programa se ha cerrado.")








