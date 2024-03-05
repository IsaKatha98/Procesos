
from threading import *
import time
import random



#declaramos la clase
class Almacen(Thread):

    empiezaTurno=Barrier(10)
    pedido=Event()

    #constructor
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run (self):

        print("El trabajador", self.name, "ha llegado")

        #ponemos la barrera
        if Almacen.empiezaTurno.wait()==9:
            print("Todos los trabajadores empiezan a trabajar")

      

        while not Almacen.pedido.is_set():
            Almacen.pedido.set()
            print("Se genera un pedido")
            num= random.randint(1,6)
            time.sleep(num)
            print("Los trabajadores se ponen con el pedido")
            Almacen.pedido.clear()
            num= random.randint(1,6)
            time.sleep

