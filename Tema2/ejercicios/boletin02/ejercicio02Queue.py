from multiprocessing import *
import time
import random

def randomIP(cola1):
     for _ in range(10):
          ip=""

          for i in range(4):
               octeto=random.randint(0,255)
               ip+=str(octeto)
               if i!=3:
               
                    ip+="."
          else:
               #manda la ip generada.
               cola1.put(ip)
     else:
     #añadimos un none cuando termine el bucle for
          cola1.put(None)
          
def filtraABC(cola1, cola2):
     #Recibimos la ip.
     ip=cola1.get()

     while ip!=None:
     #Aquí hay que hacer un split del ip (string) que nos llega
          octeto1=ip.split(".")

     #Si el primer octeto es mayor de 223 entonces es cuando la ip es de clase D.
          if int(octeto1[0])<224:
          #Mandamos la ip al proceso 3.
               cola2.put(ip)

          #Pedimos otra ip.
          ip=cola1.get()
     cola2.put(None)

def leeIP (cola2):
     #Recibimos la ip.
     ip=cola2.get()

     while ip!=None:

     #Clasificamos según la clase de la ip.
          octeto1=ip.split(".")

          if int(octeto1[0])<128:
               print (ip, ": es una IP de clase A")

          elif 128<int(octeto1[0])<192:
               print(ip, ":esta IP es de clase B")

          else:
               print (ip,": esta IP es de clase C")

          #Pedimos otra ip.
          ip=cola2.get()



if __name__=="__main__":

     #Declaramos tiempo de inicio
    inicio=time.time()
    
    cola1=Queue()
    cola2=Queue()

    p1=Process(target=randomIP, args=(cola1,))
    p2=Process(target=filtraABC, args=(cola1,cola2))
    p3=Process(target=leeIP, args=(cola2,))

     #Iniciamos los procesos.
    p1.start()
    p2.start()
    p3.start()
     #Esperamos a que terminen.
    p1.join()
    p2.join()
    p3.join()
   
    fin=time.time()

    #esto me da raro
    #TODO:calcular tiempos, preguntar
    print("Tiempo", fin-inicio)
