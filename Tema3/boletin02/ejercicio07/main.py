from queue import Queue
from consumidor import *
from productor import *



if __name__=="__main__":

    cola= Queue(1)
    cond= Condition()

    prod= Productor("Productor")
    con= Consumidor("Consumidor")

    prod.start()
    con.start()