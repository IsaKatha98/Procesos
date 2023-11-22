from multiprocessing import*

#Método con dos números por parámetro
#En caso de que num1 sea mayor que num2, hay que intercambiarlos.
def suma (num1, num2):

    if (num1>num2):
        #Intercambiamos los valores de las variables.
        num1,num2=num2,num1
    
    res=0
    
    #Recorremos el rango sumando los números.
    for n in range (num1, num2+1):
        res=res+n
    
    print ("suma igual a ",res)


if __name__=="__main__":


    with Pool(processes=4) as pool:
        numbers=[(1,2),(2,3),(3,4),(4,5),(5,6)]

        results =pool.starmap(suma, numbers)

    print("All processes have finished.")
    
