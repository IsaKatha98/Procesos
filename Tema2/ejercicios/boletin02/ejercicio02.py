from multiprocessing import *
import time
import random

def randomIP(p1left:PipeConnection):
     
     for _ in range (10):
     
          ip=""

          for i in range(4):
               octeto=random.randint(0,255)
               ip+=str(octeto)
               if i!=3:
           
                   ip+="."
          #cuando ha terminado de recorrer el for, manda la ip generada.
          else:
               p1left.send(ip)
          
def filtraABC(p1right:PipeConnection, p2left:PipeConnection):
     ip=p1right.recv()
     octeto1=



if __name__=="__main__":

     #Declaramos tiempo de inicio
    inicio=time.time()
    
    p1left,p1right=Pipe()
    p2left, p2right=Pipe()

    p1=Process(target=randomIP, args=(p1left,))
    p2=Process(target=filtraABC, args=(p1right,p2left))
   