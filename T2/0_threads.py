# %%
"""
# Multithreading

This is the idea behind parallel processing, or the ability to set up and run multiple tasks concurrently.

"""

# %%
"""
##  Threading 


#### I/O-intensive processes improved with multithreading:
* webscraping
* reading and writing to files
* sharing data between programs
* network communications

"""

# %%
"""
## Multithreading Example: Webscraping

Historically, the programming knowledge required to set up multithreading was beyond the scope of this course, as it involved a good understanding of Python's Global Interpreter Lock (the GIL prevents multiple threads from running the same Python code at once). Also, you had to set up special classes that behave like Producers to divvy up the work, Consumers (aka "workers") to perform the work, and a Queue to hold tasks and provide communcations. And that was just the beginning.

Fortunately, we've already learned one of the most valuable tools we'll need – the `map()` function. When we apply it using two standard libraries, *multiprocessing* and *multiprocessing.dummy*, setting up parallel processes and threads becomes fairly straightforward.

"""

# %%
"""
Here's a classic multithreading example provided by [IBM](http://www.ibm.com/developerworks/aix/library/au-threadingpython/) and adapted by [Chris Kiehl](http://chriskiehl.com/article/parallelism-in-one-line/) where you divide the task of retrieving web pages across multiple threads:


    import time 
    import threading 
    import Queue 
    import urllib2 

    class Consumer(threading.Thread): 
      def __init__(self, queue): 
        threading.Thread.__init__(self)
        self._queue = queue 

      def run(self):
        while True: 
          content = self._queue.get() 
          if isinstance(content, str) and content == 'quit':
            break
          response = urllib2.urlopen(content)
        print 'Thanks!'


    def Producer():
      urls = [
        'http://www.python.org', 'http://www.yahoo.com'
        'http://www.scala.org', 'http://www.google.com'
        # etc.. 
      ]
      queue = Queue.Queue()
      worker_threads = build_worker_pool(queue, 4)
      start_time = time.time()

      # Add the urls to process
      for url in urls: 
        queue.put(url)  
      # Add the poison pill
      for worker in worker_threads:
        queue.put('quit')
      for worker in worker_threads:
        worker.join()

      print 'Done! Time taken: {}'.format(time.time() - start_time)

    def build_worker_pool(queue, size):
      workers = []
      for _ in range(size):
        worker = Consumer(queue)
        worker.start() 
        workers.append(worker)
      return workers

    if __name__ == '__main__':
      Producer()
"""