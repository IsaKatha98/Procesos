from hamburguesería import Hamburguesería
import time

if __name__ == "__main__":
    numeroClientes = 10 #Número de clientes que van a entrar en la Hamburguesería
    clientes = [] 

#Iteramos los clientes
    for i in range(numeroClientes):
        hilo = Hamburguesería(str(i)) #Creamos un cliente en cada iteración
        clientes.append(hilo) 
        hilo.start() #Iniciamos el cliente
        #time.sleep(1)
    
    for hilo in clientes:
        hilo.join() 

    print("Fin del main")