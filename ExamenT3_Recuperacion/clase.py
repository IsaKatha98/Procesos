from threading import *
import time
import random

#definimos la clase
class Colores(Thread):
    
    #definimos los semáforos, condiciones, candados...
    cond= Condition()

    #definimos el constructor
    def __init__(self, nombre, color):
        Thread.__init__(self, name=nombre)
        self.color=color
     

    def run (self):

        accedeDepoCian=False
        accedeDepoAmarillo=False
        accedeDepoMagenta=False
        
        #queremos que el bucle se repita sin fin
        while True:
                
            if self.color =="rojo":
                Colores.cond.acquire()
                while accedeDepoAmarillo and accedeDepoMagenta:
                    print(self.name,"está esperando ")
                    Colores.cond.wait()

              
                print(self.name, "ha cogido el depósito amarillo")
                accedeDepoAmarillo=True
                Colores.cond.notifyAll()
                print(self.name, "ha codigo el depósito magenta")
                accedeDepoMagenta=True
                Colores.cond.notifyAll()
                Colores.cond.release()

                #hace el color
                time.sleep(random.randint(100, 500)/1000)
                print(self.name, "ha terminado de hacer rojo")

                #desbloqueamos los depósitos
                Colores.cond.acquire()
                accedeDepoAmarillo=False
                accedeDepoMagenta=False
                Colores.cond.notifyAll()
                Colores.cond.release()
                print(self.name, "ha soltado el depósito amarillo")
                print(self.name, "ha soltado el depósito magenta")

                
                        
                #tiempo que tarda en volver a hacer el color
                time.sleep(random.randint(1,3))

            if self.color =="azul":

               
                Colores.cond.acquire()
                while accedeDepoCian and accedeDepoMagenta:
                    print(self.name,"está esperando ")
                    Colores.cond.wait()

                
                print(self.name, "ha cogido el depósito cian")
                accedeDepoCian=True
                Colores.cond.notifyAll()
                print(self.name, "ha codigo el depósito magenta")
                accedeDepoMagenta=True
                Colores.cond.notifyAll()
                Colores.cond.release()

                #hace el color
                time.sleep(random.randint(100, 500)/1000)
                print(self.name, "ha terminado de hacer azul")

                #desbloqueamos los depósitos
                Colores.cond.acquire()
                accedeDepoCian=False
                accedeDepoMagenta=False
                Colores.cond.notifyAll()
                Colores.cond.release()
                print(self.name, "ha soltado el depósito cian")
                print(self.name, "ha soltado el depósito magenta")

                   
                        
                #tiempo que tarda en volver a hacer el color
                time.sleep(random.randint(1,3))

            if self.color =="amarillo":

               
                Colores.cond.acquire()
                while accedeDepoCian and accedeDepoAmarillo:
                    print(self.name,"está esperando ")
                    Colores.cond.wait()

                
                print(self.name, "ha cogido el depósito cian")
                accedeDepoCian=True
                Colores.cond.notifyAll()
                print(self.name, "ha codigo el depósito amarillo")
                accedeDepoAmarillo=True
                Colores.cond.notifyAll()
                Colores.cond.release()

                #hace el color
                time.sleep(random.randint(100, 500)/1000)
                print(self.name, "ha terminado de hacer verde")

                #desbloqueamos los depósitos
                Colores.cond.acquire()
                accedeDepoCian=False
                accedeDepoAmarillo=False
                Colores.cond.notifyAll()
                Colores.cond.release()
                print(self.name, "ha soltado el depósito cian")
                print(self.name, "ha soltado el depósito amarillo")

                   
                        
                #tiempo que tarda en volver a hacer el color
                time.sleep(random.randint(1,3))

              
