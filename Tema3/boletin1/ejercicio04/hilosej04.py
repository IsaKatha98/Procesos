from threading import Thread
import random

class Vocal (Thread):
    
    def __init__(self, nombre):
      Thread.__init__(self, name=nombre)

    def run(self):
        res=0
        #abrimos el fichero.
        fileRoute="ejercicio04/vocales" 
        with open(fileRoute, "r") as file:
            for line in file:
                chain=line.strip()
            for letras in chain:
                #si el hilo encuentra una letra igual que su nombre, suma 1.
                if self.name==letras:
                    res=res+1
            #cuando termine el bucle for, imprimimos la cuenta de que cada vocal    
            print ("Hilo", self.name, "ha contado la vocal", res, "veces")       


