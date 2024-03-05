from hilos import *

if __name__ == "__main__":

    #funcion para contar vocales del texto recogido del archivo
    def contar_vocales(vocal, frase):
        cantidadVocal = frase.count(vocal) #El hilo cuenta la vocal en concreto
        print(f'Se contaron {cantidadVocal} "{vocal}".')

    with open('ejercicios1/ejercicio04/archivo.txt', 'r') as f: #Abrimos y leemos el archivo
        frase = f.read()

    vocales = ["a", "e", "i", "o", "u"]
    hilos = [] 

    # Recorremos la lista de vocales
    for vocal in enumerate(vocales):
        hilo = Hilo(vocal, frase) # Creamos un hilo con la vocal correspondiente
        hilos.append(hilo)
        hilo.start()

    # Llamamos a la función contar_vocales() en el hilo principal
    for vocal in vocales:
        contar_vocales(vocal, frase)

    # Recorremos la lista de hilos  
    for hilo in hilos:
        hilo.join()