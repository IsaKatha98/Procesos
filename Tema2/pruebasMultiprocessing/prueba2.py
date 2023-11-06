from multiprocessing import*
import time


def hello(name):
    print ("Hello, worl", name)


def suma (num1, num2):
    res= num1 +num2
    print ("suma igual a ",res)

#se ejecuta antes el fin min que el hello, porque son dos procesos diferentes
if __name__=="__main__":
    inicio=time.time()
    p1=Process(target=suma, args=(3,5))
    p1.start()
    p2=Process(target=hello, args=("Elena",))
    p2.start()

    p1.join()
    p2.join()

    fin= time.time()

    print("tiempo:", fin-inicio)



    #ahora p se espera a que el main termine y por eso el hello
    #se va a imprimir antes que el print
  