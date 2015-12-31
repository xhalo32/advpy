import asyncio

async def coro(name, lock):
    print('coro {}: waiting for lock'.format(name))
    async with lock:
        print('coro {}: holding the lock'.format(name))
        print('coro {}: releasing the lock'.format(name))

loop = asyncio.get_event_loop()
lock = asyncio.Lock()
coros = asyncio.gather(coro(1, lock), coro(2, lock))
try:
    loop.run_until_complete(coros)
finally:
    loop.close()

def asdf( a, b, c, d ):
	print( a, b, c, d )

asdf( **{
	'a' : 1, 
	'd' : 4,
	'b' : 2,
	'c' : 3,
 } )