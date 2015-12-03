import threading as td
import random, time

lock = td.Lock()

def Split(words):

	lock.acquire()
	try:
		l = words.split()
		new = []
		while l:
			new.append(l.pop(random.randrange(0, len(l))))
		print " ".join(new)
	finally:
		lock.release()

words = "I am not human. I am robot!"
thdlen = 5
thdlist = []
for i in range(thdlen):
	t = td.Thread(target=Split, args=(words,) )
	t.start()
	thdlist.append(t)

time.sleep(0.1)
print td.activeCount()