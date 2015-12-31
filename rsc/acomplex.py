import pygame as p
from math import pi
from math import sin, cos

class acomplex(object):

	@classmethod
	def arrect(self, window, color, pos, rradius, lnwidth = -1):

		rdiam = 2 * rradius

		pos[0] = int(pos[0])
		pos[1] = int(pos[1])
		pos[2] = int(pos[2])
		pos[3] = int(pos[3])

		size = window.get_size(  )
		s = p.Surface( size, p.SRCALPHA )
		if lnwidth <= 0:

			p.draw.rect(s, color, [ pos[0], pos[1] + rradius, pos[2], pos[3] - rdiam ])

			p.draw.rect(s, color, [ pos[0] + rradius, pos[1], pos[2] - rdiam, pos[3] ])

			p.draw.circle(s, color, [ pos[0] + rradius, 		   pos[1] + rradius], rradius)
			p.draw.circle(s, color, [ pos[0] + rradius, 		   pos[1] + pos[3] - rradius], rradius)
			p.draw.circle(s, color, [ pos[0] + pos[2] - rradius, pos[1] + rradius], rradius)
			p.draw.circle(s, color, [ pos[0] + pos[2] - rradius, pos[1] + pos[3] - rradius], rradius)

		else:

			p.draw.rect(s, color, [ pos[0], pos[1] + rradius, lnwidth, pos[3] - rdiam ])
			p.draw.rect(s, color, [ pos[0] + pos[2] - lnwidth, pos[1] + rradius, lnwidth, pos[3] - rdiam ])

			p.draw.rect(s, color, [ pos[0] + rradius, pos[1], pos[3] - rdiam, lnwidth ])
			p.draw.rect(s, color, [ pos[0] + rradius, pos[1] + pos[3] - lnwidth, pos[3] - rdiam, lnwidth ])

			p.draw.arc(s, color, [ pos[0], pos[1], rdiam, rdiam ],
			pi/2, pi, lnwidth )

			p.draw.arc(s, color, [ pos[0], pos[1] + pos[3] - rdiam, rdiam, rdiam ],
			pi, 3*pi/2, lnwidth )

			p.draw.arc(s, color, [ pos[0] + pos[2] - rdiam, pos[1], rdiam, rdiam ],
			0, pi/2, lnwidth )

			p.draw.arc(s, color, [ pos[0] + pos[2] - rdiam, pos[1] + pos[3] - rdiam, rdiam, rdiam ],
			3*pi/2, 2*pi, lnwidth )

		window.blit( s, [ 0, 0 ] )

	@classmethod
	def atriangle(self, window, color, pos, radius, rotation = 0, lnwidth = 0, usecenter=True):

		rad = 180.0 / pi

		radrot = - rotation / rad

		size = window.get_size(  )
		s = p.Surface( size, p.SRCALPHA )

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
			p.draw.polygon(s, color, [ pos1, pos2, pos3 ] )
		else:
			p.draw.polygon(s, color, [ pos1, pos2, pos3 ], lnwidth )

		window.blit( s, [ 0, 0 ] )

	@classmethod
	def avector(self, window, color, startpos, angle, lenght, lnwidth = 1, antialiased=False):

		startpos = int( startpos[ 0 ] ), int( startpos[ 1 ] )
		endpos = int( startpos[0] ) + lenght * cos( ( - angle) / ( 180.0 / pi ) ), \
				 startpos[1] + lenght * sin( ( - angle) / ( 180.0 / pi ) )

		size = window.get_size(  )
		s = p.Surface( size, p.SRCALPHA )

		if antialiased:
			p.draw.aaline(s, color, startpos, endpos, lnwidth)
		else:
			p.draw.line(s, color, startpos, endpos, lnwidth)

		window.blit( s, [ 0, 0 ] )

	@classmethod
	def aregpolygon(self, window, color, center, radius, gon, rotation=0, lnwidth = 0):

		poslist = []
		size = window.get_size(  )
		s = p.Surface( size, p.SRCALPHA )

		for i in range(gon):

			angle = ( - rotation + i * ( 360.0 / gon ) ) / ( 180.0 / pi )

			poslist.append(
				[
					center[0] + radius * cos( angle ),
					center[1] + radius * sin( angle )
				]
			)

		p.draw.polygon(s, color, poslist, lnwidth)

		window.blit( s, [ 0, 0 ] )

	@classmethod
	def aregstar(self, window, color, center, radius, gon, rotation=0, lnwidth = 0):

		poslist = []
		size = window.get_size(  )
		s = p.Surface( size, p.SRCALPHA )

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

		p.draw.polygon(s, color, poslist, lnwidth)
		window.blit( s, [ 0, 0 ] )

	@classmethod
	def areggramm(self, window, color, center, radius, gon, rotation=0, lnwidth = 1, antialiased=False):

		poslist = []

		size = window.get_size(  )
		s = p.Surface( size, p.SRCALPHA )
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
						p.draw.aaline(s, color, a, b, lnwidth)

					else:
						p.draw.line(s, color, a, b, lnwidth)

		window.blit( s, [ 0, 0 ] )

	@classmethod
	def acurve(self, window, color, center, radius, startangle, endangle, points=-1, lnwidth = 1, antialiased=False):
		
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

		size = window.get_size(  )
		s = p.Surface( size, p.SRCALPHA )

		for i in range(len(pointlist)):
			try:
				if antialiased:
					p.draw.aaline(s, color, pointlist[i], pointlist[i+1], lnwidth )
				else:
					p.draw.line(s, color, pointlist[i], pointlist[i+1], lnwidth )
			except:
				pass

		window.blit( s, [ 0, 0 ] )

if __name__ == '__main__':
	p.draw.acomplex = acomplex