from multiprocessing import*

#Método con dos números por parámetro
#En caso de que num1 sea mayor que num2, hay que intercambiarlos.
def suma (num1, num2):

    if (num1>num2):
        #Intercambiamos los valores de las variables.
        num1,num2=num2,num1
    
    res=0
    
    #Recorremos el rango sumando los números.
    for n in range (num1, num2+1):
        res=res+n
    
    print ("suma igual a ",res)

if __name__=="__main__":

    #Nos creamos los procesos que llamen a la función suma.
    p1=Process(target=suma, args=(3,4))
    p1.start()
    p2=Process(target=suma, args=(8,2))
    p2.start()
    p3=Process(target=suma, args=(4,7))
    p3.start()
    p4= Process(target=suma, args=(15,21))
    p4.start()

    #Paramos el proceso del main hasta que hayan terminado todos los procesos.
    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print("Todos los procesos han terminado")

