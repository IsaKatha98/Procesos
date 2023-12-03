from multiprocessing import*
import time

#function that receives a vocal letter and counts
#how many times it appears in a file
def countsVocals (vocal):

    res=0
    
    #calls the fileReader functions
    chain=fileReader()
    for letras in chain:
        res+=letras.count(vocal)
    
    print (vocal,"repeats itself", res, "times")

#Function that reads a file
def fileReader ():

    fileRoute="Tema2/ejercicios/boletin02/ficheros/vocales.txt" 
    with open(fileRoute, "r") as file:
        for line in file:
            chain=line.strip()
            print(chain)         
    return chain

            


if __name__=="__main__":

    #Declaramos tiempo de inicio
    inicio=time.time()

    with Pool(processes=5) as pool:
        vocals=["a","e","i","o","u"]

        results =pool.map(countsVocals, vocals)

    fin=time.time()

    #esto me da raro
    #TODO:calcular tiempos, preguntar
    print("Tiempo", fin-inicio)


