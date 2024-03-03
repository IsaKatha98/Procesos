from ong import*

#declaramos el main
if __name__=="__main__":
    
    numGestores=4
    numVoluntarios=4

    #creamos los hilos de cada integrante
    for a in range(numGestores):
        hilo=Gestores(str(a))
        hilo.start()

    for b in range(numVoluntarios):
        hilo=Voluntarios(str(b))
        hilo.start()


