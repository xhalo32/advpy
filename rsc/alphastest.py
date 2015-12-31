import pygame as pg
from acomplex import acomplex

window = pg.display.set_mode((600, 600))

exit = 0
x = 0

c = pg.time.Clock()

def run():
	global x, exit

	exit = 0

	while not exit:

		for e in pg.event.get():
			if e.type == pg.QUIT:
				exit = True

		window.fill((100, 100, 100))

		x += 1
		x %= 360

		

		acomplex.arrect(window, (255, 0, 255, 100), [ 10, 10, 100, 100 ], x / 10)

		acomplex.acurve(window, (0, 0, 0, 100), [200, 200], 199, x, x + 180, lnwidth=5)

		acomplex.atriangle(window, (0, 255, 255, 150), [150, 150], 40, x, usecenter=1)

		acomplex.atriangle(window, (255, 255, 255, 150), [200, 150], 20, x, usecenter=0)

		acomplex.avector(window, (255, 255, 255, 150), [200, 150], x, x, 3)

		acomplex.avector(window, (255, 255, 0, 150), [300, 300], x, x, 1)

		acomplex.aregpolygon(window, (255, 255, 255, 100), [300, 300], 50, 7, x)

		acomplex.aregstar(window, (255, 255, 255, 150), [250, 400], 50, 9, 45, 2)

		acomplex.areggramm(window, (255, 255, 255, 150), [100, 300], 80, 8, 18)



		pg.display.update()

		c.tick(40)
run()