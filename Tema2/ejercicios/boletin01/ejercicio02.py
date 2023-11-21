from multiprocessing import*
import time

def suma (num):
    
    res=0

    for n in range (num+1):
        res=res+n
    
    print ("suma igual a ",res)

if __name__=="__main__":

    #Declaramos tiempo de inicio
    inicio=time.time()

    with Pool(processes=4) as pool:
        numbers=[1,2,3,4,5]

        results =pool.map(suma, numbers)

    fin=time.time()

    #esto me da raro
    #TODO:calcular tiempos, preguntar
    print("Tiempo", fin-inicio)