import threading as td
import time

def doThis():
	global x, lock

	lock.acquire()
	try:
		while x < 300:
			x += 1

		print x, td.current_thread().name

	finally:
		time.sleep(1)
		lock.release()

def doAfter():
	global x, lock
	
	lock.acquire()
	try:
		while x < 600:
			x += 1

		print x, td.current_thread().name

	finally:
		lock.release()

def main():

	global x, lock
	x = 0

	lock = td.Lock()
	
	t1 = td.Thread( target = doThis )
	t2 = td.Thread( target = doAfter )

	t1.start()

	# WAITING FOR T1 TO FINISH
	# t1.join()

	t2.start()

if __name__ == '__main__':
	main()