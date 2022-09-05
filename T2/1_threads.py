# -*- coding: utf-8 -*-
"""
A simple threading example. Create some threads by subclassing `threading.Thread`,
keep track of them and wait for them to join.
"""

import random
import threading
import time


class SleepingThread(threading.Thread):

    #: How long we're going to sleep for
    sleep_length = None
    id = None

    def __init__(self, sleep_length=None, id=None):
        super().__init__()
        self.sleep_length = sleep_length or random.randrange(1, 20)
        self.id=str(id)

    def run(self):
        print('starting thread ' + self.id)
        time.sleep(self.sleep_length)
        print('ending thread ' + self.id)


if __name__ == '__main__':


    threads = list()
    for i in range(4):
        t = SleepingThread(id=i)
        threads.append(t)
        print('Launching Thread {}'.format(i))
        t.start()


    # wait for each to finish (join)
    for i, t in enumerate(threads):
        t.join()
        print('Thread {} Stopped'.format(t.id))
    
  

