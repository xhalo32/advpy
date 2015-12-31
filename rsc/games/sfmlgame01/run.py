from sfml import sf
from pygame.time import Clock

size = sf.Vector2( 600, 400 )

timelist = [  ]
speed = 5

width, height = size
s = sf.RenderWindow( sf.VideoMode( width, height ), "HIIII" )
font = sf.Font.from_file( "../Ubuntu-L.ttf" )

#s.vertical_synchronization = True

clock = Clock(  )
sfclock = sf.Clock(  )

def rect( window, colors, pos, outline_thickness=0 ):

	o = sf.RectangleShape()
	o.position = pos[ 0 : 2 ]
	o.size = pos[ 2 : 4 ]

	o.outline_thickness = outline_thickness
	try:
		o.outline_color = sf.Color( colors[ 1 ][ 0 ], colors[ 1 ][ 1 ], colors[ 1 ][ 2 ] )
	except: o.outline_color = sf.Color( 0, 0, 0 )

	o.fill_color = sf.Color( colors[ 0 ][ 0 ], colors[ 0 ][ 1 ], colors[ 0 ][ 2 ] )
	o.origin = ( 0, 0 )

	window.draw( o )
	return o

def circle( window, colors, pos, radius, outline_thickness=0 ):

	o = sf.CircleShape()
	o.radius = radius
	o.outline_thickness = outline_thickness
	try:
		o.outline_color = sf.Color( colors[ 1 ][ 0 ], colors[ 1 ][ 1 ], colors[ 1 ][ 2 ] )
	except: o.outline_color = sf.Color( 0, 0, 0 )
	o.fill_color = sf.Color( colors[ 0 ][ 0 ], colors[ 0 ][ 1 ], colors[ 0 ][ 2 ] )

	o.origin = ( 0, 0 )
	o.position = pos

	window.draw( o )
	return o

def message( window, color, message, pos, size = 25 ):

	g = sf.Text(  )
	g.string = str( message )
	g.font = font
	g.character_size = size
	g.position = pos
	g.color = sf.Color( color[ 0 ], color[ 1 ], color[ 2 ] )

	window.draw( g )


x, y = size / 2
index = 0.
step = 8

while s.is_open:

	for e in s.events:
		if type( e ) == sf.CloseEvent:
			s.close(  )

	if sf.Keyboard.is_key_pressed( sf.Keyboard.RIGHT ):
		x += speed

	if sf.Keyboard.is_key_pressed( sf.Keyboard.LEFT ):
		x += -speed

	if sf.Keyboard.is_key_pressed( sf.Keyboard.UP ):
		y += -speed

	if sf.Keyboard.is_key_pressed( sf.Keyboard.DOWN ):
		y += speed

	mx = sf.Mouse.get_position(s).x
	my = sf.Mouse.get_position(s).y

	x = mx
	y = my


	s.clear( sf.Color( 0, 255, 0 ) )

	for o in range( 44 ):
		circle( s, ( ( 255, 255, 255 ), ), [ 8 * o + 16, 8 * o + 16 ], 5, 3 )

	circle( s, ( ( 255, 255, 255 ), ), [ ( x // step ) * step, ( y // step ) * step ], 6, 3 )

	rect( s, ( ( 255, 0, 0 ), ), [ 10, 10, 20, 20 ] )

	try:
		message( s, ( 255, 0, 255 ), round( 1 / ( index / len( timelist ) ), 2 ), ( size[ 0 ] - 100, 40 ) )
	except:pass
	s.display(  )


	timelist.append( sfclock.restart(  ).seconds )
	if len( timelist ) > 60:
		del timelist[ 0 ]
	index = 0.
	for i in timelist:
		index += i

	clock.tick( 60 )