#Función que lee el fichero.
def producer ():
    with open("fichero04.txt", "r") as fichero:
        
        numbers=[]

        linea=fichero.readline()
        numbers+=linea
        while linea:
            linea=fichero.readline()
            numbers+=linea
          
        print (numbers)
        
       

            #TODO:hay que añadir None , al final de la cola