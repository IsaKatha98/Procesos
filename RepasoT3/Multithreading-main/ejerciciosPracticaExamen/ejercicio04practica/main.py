from threading import *
from trabajadores import Trabajadores
import random

if __name__ == "__main__":
    numTrabajadores = 5
    evento = Event()
    barrera = Barrier(numTrabajadores)
    tiempoEntrePedidos = 6
    pedidoSolicitado = False
    realizandoPedido = False

    def pedidoPedido():
        print("Pedido solicitado")
        evento.set()

    def pedidoAcabado():
        print("Pedido entregado")

    for trabajador in range(numTrabajadores):
        Trabajadores(str(trabajador), evento, barrera).start()    

    while True:
        if not evento.is_set() and not pedidoSolicitado:
            print("Los trabajadores están esperando a un pedido...")
            Timer(tiempoEntrePedidos, pedidoPedido).start()
            pedidoSolicitado = True
            realizandoPedido = False
        
        if evento.is_set() and not realizandoPedido:
            print("Los trabajadores están trabajando en un pedido...")
            Timer(random.randint(4,8), pedidoAcabado).start()
            realizandoPedido = True
            pedidoSolicitado = False
        