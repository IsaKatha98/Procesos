from threading import *
import random
import time

class Almacen(Thread):
    hayPedido=False

    def __init__(self, nombre, barrera:Barrier, evento:Event):
        Thread.__init__(self, name=nombre)
        self.barrera=barrera
        self.evento=evento


    def run(self):
       #hay que esperar a que todos los trabajadores estén en el almacén.
        print("El trabjador", self.name, "acaba de fichar")
        #ponemos la barrera.
        if self.barrera.wait()==4:
            print("Los trabajadores empiezan a trabajar.")
          
        
        #los trabajadores esperan a que entre un pedido
        while True:

            while not self.evento.is_set():
               
               
                print("Entra un pedido")
                
                self.evento.set()
            

               
            print("Los trabajadores están trabajando")
            time.sleep(random.randint(1,11))
            print("El trabajador", self.name, "ha terminado de preparar el pedido")
            self.barrera.wait()
            self.evento.clear()

              

          



    


         