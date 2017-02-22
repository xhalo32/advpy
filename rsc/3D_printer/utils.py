
def convert( rgb ):
	rgb = [ int( c ) for c in rgb ]
	color = "#"
	for c in rgb:
		h = format( hex( c ).split( 'x' )[ 1 ] )
		if c < 16: h = "0"+h
		color += h

	if len( color ) != 7:return None
	return color

def draw_progress_bar( canvas, progress ):
	width = canvas.width
	height = float( canvas['height'] )
	canvas.delete("all")

	if progress:
		canvas.create_rectangle(
			0, 0, float(progress)*width, height, fill=convert( [255-255*progress, 255*progress, 0] ) )

		canvas.create_text(
			width/2, height/2, text="%.2f" % float( progress*100 ) + "%" )