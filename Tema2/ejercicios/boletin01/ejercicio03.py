from multiprocessing import*

def suma (num):
    
    res=0

    for n in range (num+1):
        res=res+n
    
    print ("suma igual a ",res)

#Función que lee el fichero.
def producer ():
    with open("ejercicio03Fichero.txt", "r") as fichero:
        
        numbers=[]

        linea=fichero.readline()
        numbers+=linea
        while linea:
            linea=fichero.readline()
            numbers+=linea

            #TODO:hay que añadir None , al final de la cola


if __name__=="__main__":

    queue=Queue()
    
    p1=Process(target=producer, args=(queue,))
    p2=Process(target=suma,args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    queue.put(None)

    p2.join()

   