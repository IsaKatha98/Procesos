from multiprocessing import*

def hello(name):
    print ("Hello, worl", name)

#se ejecuta antes el fin min que el hello, porque son dos procesos diferentes
if __name__=="__main__":
    p=Process(target=hello, args=("Elena",))
    p.start()

    #ahora p se espera a que el main termine y por eso el hello
    #se va a imprimir antes que el print
    p.join()
    print ("fin main")