import threading
import time
import random


def run (nombre):
    while True:
        print("Soy", nombre, "y estoy trabajando.")
        num= random.randint(0, 10)
        time.sleep(num)
        print ("Soy", nombre, "y he terminado de trabajar. He trabajado", num, "horas")

t1= threading.Thread(target= run, args=("Pedro",))
t2=threading.Thread (target=run, args=("Javi", ))
t3=threading.Thread (target=run, args=("Luisa", ))
t4=threading.Thread (target=run, args=("Paco", ))
t5=threading.Thread (target=run, args=("Miguel", ))
t6=threading.Thread (target=run, args=("Elena", ))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()








