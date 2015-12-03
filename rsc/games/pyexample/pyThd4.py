from Queue import Queue
import time
import threading as thd

q = Queue()

l = thd.Lock()

for i in range(10):
    q.put( i )
    
def work():
    
    while 1:
        try:
            task = q.get()
        finally:
            if q.unfinished_tasks > 0:
                
                time.sleep(1)
                
                try:
                    q.task_done()
                finally:
                    with l:
                        print thd.current_thread().name, task + 1, "done"

for i in range( 8 ):
    
    t = thd.Thread( target=work )
    t.daemon=True
    t.start()

q.join()

print "Finished", q.unfinished_tasks, "left"