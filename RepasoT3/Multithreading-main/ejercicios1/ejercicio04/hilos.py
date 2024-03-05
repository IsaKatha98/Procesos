from threading import Thread

class Hilo(Thread):
    def __init__(self, vocal, frase):
        # Llamamos al constructor de la clase base
        Thread.__init__(self)
        self.vocal = vocal
        self.frase = frase