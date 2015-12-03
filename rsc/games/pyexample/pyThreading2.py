import threading as td
import time

def doThis():
	global x
	x = 0
	time.sleep(0.1)
	while x < 300:
		x += 1

	print x

def doAfter():
	global x
	while 300 <= x < 600:
		x += 1

	print x

def main():
	
	t1 = td.Thread( target = doThis )
	t2 = td.Thread( target = doAfter )
	t1.start()

	# WAITING FOR T1 TO FINISH
	t1.join()

	t2.start()
	
main()