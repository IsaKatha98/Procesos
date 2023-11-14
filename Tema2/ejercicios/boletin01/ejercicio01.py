from multiprocessing import*

def suma (num):
    
    res=0

    for n in range (num+1):
        res=res+n
    
    print ("suma igual a ",res)

if __name__=="__main__":

    #Nos creamos los procesos que llamen a la función suma.
    p1=Process(target=suma, args=(3,))
    p1.start()
    p2=Process(target=suma, args=(8,))
    p2.start()
    p3=Process(target=suma, args=(4,))
    p3.start()
    p4= Process(target=suma, args=(15,))
    p4.start()

    #Paramos el proceso del main hasta que hayan terminado todos los procesos.
    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print("Todos los procesos han terminado")




