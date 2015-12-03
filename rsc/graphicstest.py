import pygame as pg
import complex

print complex

window = pg.display.set_mode((600, 600))

exit = 0
x = 0

c = pg.time.Clock(

	def run(self):
		global x, exit

		exit = 0

		while not exit:

			for e in pg.event.get():
				if e.type == pg.QUIT:
					exit = True

			window.fill((100, 100, 100))

			x += 1
			x %= 360

			pg.draw.complex.rrect(window, (255, 255, 255), [ 10, 10, 100, 100 ], 40)
			pg.draw.complex.curve(window, (0, 0, 0), [200, 200], 199, x, x + 180, lnwidth=5)
			pg.draw.complex.triangle(window, (0, 255, 255), [150, 150], 40, x, usecenter=1)
			pg.draw.complex.triangle(window, (255, 255, 255), [200, 150], 20, x, usecenter=0)
			pg.draw.complex.vector(window, (255, 255, 255), [200, 150], x, x, 1000, 1)
			pg.draw.complex.regpolygon(window, (255, 255, 255), [300, 300], 50, 4, x)
			pg.draw.complex.vector(window, (255, 255, 0), [300, 300], 0, x, 1)
			pg.draw.complex.regstar(window, (255, 255, 255), [250, 400], 50, 5, 45)

			pg.draw.complex.reggramm(window, (255, 255, 255), [100, 300], 80, 5, 18)

			pg.display.update()

			c.tick(40)

a = ASD()
a.run()