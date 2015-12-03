from Queue import Queue
import time, random

import threading as thd


lock = thd.Lock(  )

def job( task ):

	final = ""
	task_list = list( task )

	while final != task:
		
		task_list = list( task )
		
		done_task = []

		while len( task_list ) > 0:
			
			r = random.randrange( 0, len( task_list ) )
			
			done_task.append( task_list.pop(r) )
		
		final = "".join( done_task )

	with lock:

		print thd.current_thread(  ).name, ":", final, "@", time.time(  ) - start
		
def worker():
	
	while 1:
		try:
			work = q.get()
		finally:
			job( work )
			try:
				q.task_done()
			finally:
				pass

q = Queue()

for x in range( 8 ):
	
	t = thd.Thread( target = worker )
	t.daemon = True
	t.start()
 
start = time.time()
task = "3.141"

for i in range( 8 ):
	
	q.put( task )
	
q.join(  )

print 'Took', time.time(  ) - start