#Implementa en python un codigo de Productor Consumidor mediante cola sincronizada tal que:
#1. El productor produce años de nacimiento que los almacena en la cola y el tiempo de espera entre 
#la generacion de un numero y otro es de 1 segundos
#2 El consumidor lee los años e indica si el año correspondonte es bisiesto o no 
#el tiempo de espera entre la lectura de completa una cola y la siguiente lectura completa es de es de 4 segundos
#Prueba el algoritmo con una relacion de productor:consumidor de 1:1, 3:2, 2:10

import threading
import time
import random
import queue

class Productor(threading.Thread):
    def __init__(self, cola):
        threading.Thread.__init__(self)
        self.cola = cola

    def run(self):
        for i in range(10):
            item = random.randint(0, 2022)
            self.cola.put(item)
            print("Productor: Año generado %d" %item)
            time.sleep(1)

class Consumidor(threading.Thread):
    def __init__(self, cola):
        threading.Thread.__init__(self)
        self.cola = cola

    def run(self):
        for i in range(10):
            item = self.cola.get()
            print("Consumidor: Año %d %s" % (item, "bisiesto" if item % 4 == 0 else "no bisiesto"))
            time.sleep(4)

def main():
    cola = queue.Queue()
    productor = Productor(cola)
    consumidor = Consumidor(cola)
    productor.start()
    consumidor.start()
    productor.join()
    consumidor.join()

if __name__ == "__main__":
    main()


