from multiprocessing import *

#función recibe el nombre de un departamento, lee el fichero salarios
# y envía la información al proceso2.
def proceso1 (cola, departamento):
    #declaramos el fichero salarios.
    fichero="ejercicio02/ficheros/salarios.txt"
    #abrimos el fichero salarios en modo lectura.
    with open (fichero, "r") as file:
        for linea in file:
            #leemos
            lineaArray=linea.split(";")
            #quitamos el salto de línea y guardamos en una variable auxiliar
            departamentoAux=lineaArray[3].strip("\n")
            #comparamos si los departamentos son iguales
            if departamentoAux==departamento:
                #en caso afirmativo, enviamos un array con toda la info menos el departamento
                #lo mandamos así para poder trabajar de forma más sencilla.
                info=[lineaArray[0], lineaArray[1],lineaArray[2]]
                cola.put(info)
               
        #ponemos non, cuando termine el bucle for.
        else:
            cola.put(None)

#función que recibe el salario mínimo y la cola.
#clasifica según si el salario es mayor o menor que el salario introducido
def proceso2(cola, salarioMinimo):
    #llamamos la cola
    linea=cola.get()
    #comprobamos que la linea no es None
    while linea!=None:
        #comparamos, teniendo en cuenta de que son dos int.
        if int(linea[2])>=int(salarioMinimo):
            #si son iguales, mandamos la línea.
            cola.put(linea)
         #llamamos la cola
        linea=cola.get()
    #cuando termine el bucle ponemos None en la cola.
    else:
        cola.put(None)
       
#función que recibe la info de un empleado, la formatea y la escribe en un fichero.
def proceso3(cola):
     #llamamos la cola
    linea=cola.get()
    #comprobamos que la linea no es None
    while linea!=None:
        #creamos el archivo en modo concatenación.
        with open ("ejercicio02/ficheros/empleados.txt", "a") as file:
            #escribimos
            file.write(f"{linea[1]} {linea[0]}, {linea[2]}\n")
            
        #llamamos a la cola
        linea=cola.get()
    #cuando termine el bucle ponemos None en la cola.
    else:
        cola.put(None)

if __name__=="__main__":

    #Pedimos al usuario que introduzca los datos
    departamento=input("Por favor, introduzca el nombre de un departamento: ")
    
    
    #declaramos la cola. Utilizamos una cola para que en cuanto se genere la información que queremos
    #pase por todos los procesos.
    cola=Queue()

    #declaramos los procesos
    p1= Process(target= proceso1, args=(cola, departamento))
    p1.start()
    p1.join()

    salarioMinimo=input("Por favor, introduzca un salario mínimo: ")
    p2=Process(target=proceso2, args=(cola, salarioMinimo))
    p3=Process(target=proceso3, args=(cola,))

    #iniciamos
    
    p2.start()
    p3.start()

    #esperamos.
  
    p2.join()
    p3.join()

    print("Todos los procesos han finalizado")


   

