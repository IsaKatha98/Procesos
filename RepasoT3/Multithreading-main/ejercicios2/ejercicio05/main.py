from estudiantes import *

#Este literalmente lo hice contigo en clase Elena
if __name__ == "__main__":
    cantidadLibros = 9
    lista = []
    
    for _ in range(cantidadLibros):
        Libro.libros.append(False)

    for i in range(10):
        hilo = Libro(str(i))
        hilo.start()
        lista.append(hilo)
    
    for j in lista:
        j.join()

    print("Fin del main")