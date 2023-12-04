from multiprocessing import *
from multiprocessing.connection import PipeConnection
import time
import random

def randomIP(p1left:PipeConnection):

     for _ in range(10):
          ip=""

          for i in range(4):
               octeto=random.randint(0,255)
               ip+=str(octeto)
               if i!=3:
               
                    ip+="."
          else:
               #manda la ip generada.
               p1left.send(ip)
     else:
     #añadimos un none cuando termine el bucle for
          p1left.send(None)
          
def filtraABC(p1right:PipeConnection, p2left:PipeConnection):
     #Recibimos la ip.
     ip=p1right.recv()

     while ip!=None:
     #Aquí hay que hacer un split del ip (string) que nos llega
          octeto1=ip.split(".")

     #Si el primer octeto es mayor de 223 entonces es cuando la ip es de clase D.
          if int(octeto1[0])<224:
          #Mandamos la ip al proceso 3.
               p2left.send(ip)

          #Pedimos otra ip.
          ip=p1right.recv()
     p2left.send(None)

def leeIP (p2right:PipeConnection):
     #Recibimos la ip.
     ip=p2right.recv()

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
          ip=p2right.recv()



if __name__=="__main__":

     #Declaramos tiempo de inicio
    inicio=time.time()
    
    p1left,p1right=Pipe()
    p2left, p2right=Pipe()

    p1=Process(target=randomIP, args=(p1left,))
    p2=Process(target=filtraABC, args=(p1right,p2left))
    p3=Process(target=leeIP, args=(p2right,))

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
