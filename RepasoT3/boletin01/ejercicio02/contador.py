from threading import *

#definimos la clase
class Contador(Thread):

    #definimos una variable global y compartida
    num=0
    numMax=1000

    #vamos a utilizar un candado para la parte de la comprobación
    lock=Lock()
    
    #definimos el constructor
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    #definimos la función que gestiona los hilos
    def run(self):

        print("Soy el", self.name)

        ##vamos a ejecutar un bucle que sea mientras el numero no sea mayor que 1000
        while not Contador.num>Contador.numMax:

            #ponemos el candado
            Contador.lock.acquire()

            #añadimos uno al número
            print("Soy el", self.name, "y voy a aumentar el contador:")
            Contador.num+=1

            print(Contador.num)
            Contador.lock.release()

        else:
            print (Contador.num, "es mayor que", Contador.numMax)


