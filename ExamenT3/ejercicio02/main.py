from threading import *
from asociacion import *

if __name__=="__main__":

    #creamos una condición compartida entre todos los hilos
    #para poder acceder a la sección crítica del código de uno en uno
    #y notificar de los cambios que haga un hilo en la variable cant
    #al resto de los hilos.
    cond=Condition()

    for i in range (1,11):

        voluntario= Voluntario(str(i), cond)

        voluntario.start()

      

   
    for i in range (1,3):
        
        gestor = Gestor(str(i), cond)
        
        gestor.start()

    

    

    
