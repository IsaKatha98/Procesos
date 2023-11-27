from multiprocessing import *
import time

def randomIP(left:conn):


def filtersP1():



def filtersAndPrints():


if __name__=="__main__":

     #Declaramos tiempo de inicio
    inicio=time.time()

    #Declares the pipe.
    left1, left2, right1, right2=Pipe()
    
    #Hacemos los procesos.
    p1=Process(target=randomIP, args=(left1,))
    p2=Process(target=filtersP1, args=(left2,right1))
    p3=Process(target=filtersAndPrints, args=(right2,))

    #Iniciamos los procesos.
    p1.start()
    p2.start()
    p3.start()

    #Esperamos a que terminen.
    p1.join()
    p2.join()
    p3.join()

    print("All processes have finished.")