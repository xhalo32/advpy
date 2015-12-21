import threading as td
import random, time

lock = td.Lock()

def Split(words):

	l = words.split()
	new = []
	while l:
		new.append(l.pop(random.randrange(0, len(l))))
	return " ".join(new)

def List(words):

	l = list( words )
	new = []
	while l:
		new.append(l.pop(random.randrange(0, len(l))))
	return int( "".join(new) )

words = "1234"
wanted = words


avg = 0
for x in range( 0 ):

	r = None
	n = 0
	while r != wanted:
		r = Split( words )
		n += 1
	avg += n

avg = 0
for x in range( 1000 ):

	n = 0
	done = False
	while not done:
		if List( words ) == List( words ):
			done = True
		n += 1
	avg += n

print avg / 1000.0