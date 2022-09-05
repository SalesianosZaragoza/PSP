# -*- coding: utf-8 -*-
"""
A simple threading example. Create some threads by subclassing `threading.Thread`,
keep track of them and wait for them to join.
"""

import random
import threading
import time


class SleepingThread(threading.Thread):

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
    t1 = SleepingThread(id=1)
    t2 = SleepingThread(id=2)
    t3 = SleepingThread(id=3)
    t4 = SleepingThread(id=4)
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    print('Thread {} is {} alive '.format(t4.id, t4.is_alive()))
    t4.join()
    print('Thread {} Stopped'.format(t4.id))

    t3.join(0.2)
    print('Thread {} is {} alive '.format(t3.id, t3.is_alive()))
    if(t3.is_alive()):
        print('Thread {} Not Stopped yet '.format(t3.id))
    else:
        print('Thread {} Stopped'.format(t3.id))
    
    

    print('Thread {} is {} alive '.format(t2.id, t2.is_alive()))
    t2.join()
    print('Thread {} Stopped'.format(t2.id))

    print('Thread {} is {} alive '.format(t1.id, t1.is_alive()))
    t1.join()
    print('Thread {} Stopped'.format(t1.id))
