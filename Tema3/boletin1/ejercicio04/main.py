from hilosej04 import *
if __name__=="__main__":
    vocales=["a", "e", "i", "o", "u"]
    for vocal in vocales:
        hilo = Vocal(f"{vocal}")
        hilo.start()