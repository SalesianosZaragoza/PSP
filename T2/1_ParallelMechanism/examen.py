import time
import threading
import random
import queue as Queue

class Producer(threading.Thread):
    """
    Produces random integers to a list
    """

    def __init__(self, queue, pt):
        """
        Constructor.

        @param integers list of integers
        @param queue queue synchronization object
        """
        threading.Thread.__init__(self)
        self.queue = queue
        self.pt=pt
    
    def run(self):
        """
        Thread run method. Append random integers to the integers
        list at random time.
        """
        while True:

            # examen
            for i in range(10):  
                self.queue.put(random.randint(10, 1000))   
            time.sleep(self.pt) # PT producer time


class Consumer(threading.Thread):
    """
    Consumes random integers from a list
    """

    def __init__(self, queue, ct, x):
        """
        Constructor.

        @param integers list of integers
        @param queue queue synchronization object
        """
        threading.Thread.__init__(self)
        self.queue = queue
        self.ct=ct
        self.x=x
    
    def run(self):
        """
        Thread run method. Consumes integers from list
        """
        while True:
            list = []
            for i in range(self.x):  
                list.append(self.queue.get())
            
            self.calculateMCD(list)

            time.sleep(self.ct)  # CT consumer time
        
    def calculateMCD(self, list):
        print("MCD: " + str(list[0]) + " " + str(list[1]) + " " + str(list[2])
            + " = " + str(gcd(list[0], gcd(list[1], list[2]))))

def mainEj2(nP,nC):
	integers = []
	queue = Queue.Queue()
	listProducer = []
	for i in range(nP):
		t1 = Producer(queue, 2)
		listProducer.append(t1)

	listConsumer = []
	for i in range(nC):
		t2 = Consumer(queue,4,2)
		listConsumer.append(t2)

	for i in listProducer:
		i.start()
		
	for i in listConsumer:
		i.start()
        
	for i in listProducer:
        	i.join()

        for i in listConsumer:
		i.join()
                              



if __name__ == '__main__':
    #mainEj2(1,1)
    #mainEj2(4,2)
    mainEj2(2,10)
 
