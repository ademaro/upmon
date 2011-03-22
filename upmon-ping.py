#!/usr/bin/env python
from threading import Thread
import subprocess
from Queue import Queue

num_threads = 4
queue = Queue()
ips = ["8.8.8.8", "z-gu.ru", "10.0.1.11", "stat.z-gu.ru"]
#wraps system ping command
def pinger(i, q):
    """Pings subnet"""
    while True:
        ip = q.get()
        print ("Thread %s: Pinging %s" % (i, ip))
        ret = subprocess.call("ping -c 1 %s" % ip,
                        shell=True,
                        stdout=open('/dev/null', 'w'),
                        stderr=subprocess.STDOUT)
        if ret == 0:
            print ("%s: is alive" % ip)
        else:
            print ("%s: did not respond" % ip)
        q.task_done()
#Spawn thread pool
for i in range(num_threads):

    worker = Thread(target=pinger, args=(i, queue))
    worker.setDaemon(True)
    worker.start()
#Place work in queue
for ip in ips:
    queue.put(ip)
#Wait until worker threads are done to exit    
queue.join()