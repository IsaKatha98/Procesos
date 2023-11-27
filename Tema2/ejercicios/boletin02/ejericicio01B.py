from multiprocessing import*
import time

file="ejercicios/boletin02/ficheros/vocales.txt"
#function that receives a vocal letter and counts
#how many times it appears in a file
def countsVocals (vocal):

    res=0
    
    #calls the fileReader functions
    chain=fileReader()
    for vocal in chain:
        res=vocal.count()
    
    print (vocal,"repeats itself", res, "times")

#Function that reads a file
def fileReader ():

    fileRoute="ejercicios/boletin02/ficheros/vocales.txt"

    with open(fileRoute, "r") as file:
        for line in file:
            aux=line.split("/n")

            chain+=aux
            line=next()

    return chain
            


if __name__=="__main__":

    #Declaramos tiempo de inicio
    inicio=time.time()

    vocals=["a","e","i","o","u"]

    with Pool(processes=5) as pool:
        

        results =pool.map(countsVocals, vocals)

    fin=time.time()

    #esto me da raro
    #TODO:calcular tiempos, preguntar
    print("Tiempo", fin-inicio)


