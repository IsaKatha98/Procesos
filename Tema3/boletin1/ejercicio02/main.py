
from collections.abc import Callable, Iterable, Mapping
import threading
from typing import Any

class MyThread (threading.Thread):
    #atributo
    shared=0

    #esto es un constructor de la clase
    def __init__(self, shared):
      threading.Thread.__init__(self)
      self.shared=shared

    def run(self):
        while shared<1000:
            shared+=1
       
          