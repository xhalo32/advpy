import random
import time

try:
    raw_input("READY: ")
except:
    pass

last = time.time()
print last

for i in range(10):
    
    r1 = random.randint(0, 20)
    r2 = random.randint(0, 20)
    
    right = False
    
    while not right:
        
        try:
            ans = input("HOW MUCH IS " + str(r1) + " x " + str(r2) + ": ")
        except:
            print "YOUR ANSWER WAS NOT A NUMBER"
        
        if ans == r1 * r2:
            right = True
        else:
            print r1, "x", r2, "IS NOT", ans
        
now = time.time()
print now
print "your time was", round( now - last, 1 )











