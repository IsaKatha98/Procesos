from ong import Voluntarios, Gestores

if __name__ == "__main__":
    cantidadGestores = 4
    cantidadVoluntarios = 4

#Itemo por voluntarios y voy creando un voluntario con cada iteración
    for v in range(cantidadVoluntarios):
        hilo = Voluntarios(str(v))
        hilo.start()

#Hago lo mismo para los gestores
    for g in range(cantidadGestores):
        hilo = Gestores(str(g))
        hilo.start()


#Con el mismo número de gestores que de voluntarios, el dinero se mantiene más o menos estable ya que recaudan cantidades parecidas a las que se generan
#Con un número de voluntarios de 10 y un número de gestores de 4, el bote va aumentando muy poco a poco
#Cuanto mayor sea el número de voluntarios con respecto al de gestores, mayor probabilidad de acceder a la sección crítica tienen los voluntarios y menos los gestores, por lo que el bote común sube más rápido.
#En el caso contrario, si hay pocos voluntarios y muchos gestores, el bote difícilmente subirá debido a que los gestores estarán recaudando todas las ganancias del voluntario constantemente.