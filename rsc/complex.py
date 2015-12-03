import pygame
from math import pi
from math import sin, cos

class complex(object):

	@classmethod
	def rrect(self, window, color, pos, rradius, lnwidth = -1):

		rdiam = 2 * rradius

		pos[0] = int(pos[0])
		pos[1] = int(pos[1])
		pos[2] = int(pos[2])
		pos[3] = int(pos[3])

		if lnwidth <= 0:

			pygame.draw.rect(window, color, [ pos[0], pos[1] + rradius, pos[2], pos[3] - rdiam ])

			pygame.draw.rect(window, color, [ pos[0] + rradius, pos[1], pos[2] - rdiam, pos[3] ])

			pygame.draw.circle(window, color, [ pos[0] + rradius, 		   pos[1] + rradius], rradius)
			pygame.draw.circle(window, color, [ pos[0] + rradius, 		   pos[1] + pos[3] - rradius], rradius)
			pygame.draw.circle(window, color, [ pos[0] + pos[2] - rradius, pos[1] + rradius], rradius)
			pygame.draw.circle(window, color, [ pos[0] + pos[2] - rradius, pos[1] + pos[3] - rradius], rradius)

		else:

			pygame.draw.rect(window, color, [ pos[0], pos[1] + rradius, lnwidth, pos[3] - rdiam ])
			pygame.draw.rect(window, color, [ pos[0] + pos[2] - lnwidth, pos[1] + rradius, lnwidth, pos[3] - rdiam ])

			pygame.draw.rect(window, color, [ pos[0] + rradius, pos[1], pos[3] - rdiam, lnwidth ])
			pygame.draw.rect(window, color, [ pos[0] + rradius, pos[1] + pos[3] - lnwidth, pos[3] - rdiam, lnwidth ])

			pygame.draw.arc(window, color, [ pos[0], pos[1], rdiam, rdiam ],
			pi/2, pi, lnwidth )

			pygame.draw.arc(window, color, [ pos[0], pos[1] + pos[3] - rdiam, rdiam, rdiam ],
			pi, 3*pi/2, lnwidth )

			pygame.draw.arc(window, color, [ pos[0] + pos[2] - rdiam, pos[1], rdiam, rdiam ],
			0, pi/2, lnwidth )

			pygame.draw.arc(window, color, [ pos[0] + pos[2] - rdiam, pos[1] + pos[3] - rdiam, rdiam, rdiam ],
			3*pi/2, 2*pi, lnwidth )

	@classmethod
	def triangle(self, window, color, pos, radius, rotation = 0, lnwidth = 0, usecenter=True):

		rad = 180.0 / pi

		radrot = - rotation / rad

		if usecenter:

			pos1 = pos[0] + radius * cos( radrot + 180 / rad ), \
			 	   pos[1] + radius * sin( radrot + 180 / rad )
			
			pos2 = pos[0] + radius * cos( radrot + 60 / rad ), \
				   pos[1] + radius * sin( radrot + 60 / rad )

			pos3 = pos[0] + radius * cos( radrot - 60 / rad ), \
				   pos[1] + radius * sin( radrot - 60 / rad )

		else:
			pos1 = pos

			pos2 = pos[0] + 2 * radius * cos( radrot + 30 / rad ), \
				   pos[1] + 2 * radius * sin( radrot + 30 / rad )

			pos3 = pos[0] + 2 * radius * cos( radrot - 30 / rad ), \
				   pos[1] + 2 * radius * sin( radrot - 30 / rad )

		if lnwidth <= 0:
			pygame.draw.polygon(window, color, [ pos1, pos2, pos3 ] )
		else:
			pygame.draw.polygon(window, color, [ pos1, pos2, pos3 ], lnwidth )

	@classmethod
	def vector(self, window, color, startpos, angle, lenght, lnwidth = 1, antialiased=False):
		
		endpos = startpos[0] + lenght * cos( ( - angle) / ( 180.0 / pi ) ), \
				 startpos[1] + lenght * sin( ( - angle) / ( 180.0 / pi ) )

		if antialiased:
			pygame.draw.aaline(window, color, startpos, endpos, lnwidth)
		else:
			pygame.draw.line(window, color, startpos, endpos, lnwidth)

	@classmethod
	def regpolygon(self, window, color, center, radius, gon, rotation=0, lnwidth = 0):

		poslist = []

		for i in range(gon):

			angle = ( - rotation + i * ( 360.0 / gon ) ) / ( 180.0 / pi )

			poslist.append(
				[
					center[0] + radius * cos( angle ),
					center[1] + radius * sin( angle )
				]
			)

		pygame.draw.polygon(window, color, poslist, lnwidth)

	@classmethod
	def regstar(self, window, color, center, radius, gon, rotation=0, lnwidth = 0):

		poslist = []

		for i in range(gon):

			angle = ( - rotation + i * ( 360.0 / gon ) ) / ( 180.0 / pi )

			poslist.append(
				[
					center[0] + radius * cos( angle ),
					center[1] + radius * sin( angle )
				]
			)

			poslist.append(
				[
					center[0],
					center[1]
				]
			)

		pygame.draw.polygon(window, color, poslist, lnwidth)

	@classmethod
	def reggramm(self, window, color, center, radius, gon, rotation=0, lnwidth = 1, antialiased=False):

		poslist = []

		for i in range(gon):

			angle = ( - rotation + i * ( 360.0 / gon ) ) / ( 180.0 / pi )

			poslist.append(
				[
					center[0] + radius * cos( angle ),
					center[1] + radius * sin( angle )
				]
			)
		for a in poslist:
			for b in poslist:
				if a != b:
					if antialiased:
						pygame.draw.aaline(window, color, a, b, lnwidth)

					else:
						pygame.draw.line(window, color, a, b, lnwidth)

	@classmethod
	def curve(self, window, color, center, radius, startangle, endangle, points=-1, lnwidth = 1, antialiased=False):
		
		if points < 0:
			points = radius

		pointlist = []
		angleindex = - (endangle - startangle)

		#while angleindex < 0:
		#	angleindex = 360 - angleindex

		try:
			pointlen = angleindex / float(points)

		except: raise TypeError( "Radius can not be 0 or less" )

		rad = 180.0 / pi

		for i in range(points + 1):

			pointlist.append(
				[ center[0] + radius * cos( ( - startangle + i * pointlen ) / rad ),
				  center[1] + radius * sin( ( - startangle + i * pointlen ) / rad ) ]
			)

		for i in range(len(pointlist)):
			try:
				if antialiased:
					pygame.draw.line(window, color, pointlist[i], pointlist[i+1], lnwidth )
				else:
					pygame.draw.aaline(window, color, pointlist[i], pointlist[i+1], lnwidth )
			except:
				pass

if __name__ == '__main__':
	pygame.draw.complex = complex