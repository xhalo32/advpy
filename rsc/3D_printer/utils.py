import time


def convert( rgb ):
	rgb = [ int( c ) for c in rgb ]
	color = "#"
	for c in rgb:
		h = format( hex( c ).split( 'x' )[ 1 ] )
		if c < 16: h = "0"+h
		color += h

	if len( color ) != 7:raise AttributeError("%d %d %d must be in range 0-255" % (rgb[0], rgb[1], rgb[2]))
	return color

def draw_progress_bar( canvas, progress, value=0 ):
	width = canvas.width
	height = float( canvas['height'] )
	canvas.delete("all")

	if progress:
		if progress <= 0.5:
			canvas.create_rectangle(
				0, 0, float(progress)*width, height, fill=convert( [255, 510*progress+(255-510*progress)*value/255, value] ) )
		else:
			canvas.create_rectangle(
				0, 0, float(progress)*width, height, fill=convert( [510-510*progress+(510*progress-255)*value/255, 255, value] ) )

		canvas.create_text(
			width/2, height/2, text="%.2f" % float( progress*100 ) + "%" )

def get_col( current, range, mult=0.8 ):
	if current:
		if current < range[0]:
			return convert([0,255*mult,0])
		elif current >= range[1]:
			return convert([255*mult,0,0])

		else:
			curinr=(current-range[0])/(range[1]-range[0])

			if curinr <= 0.5:
				return convert( [510*curinr*mult ,255*mult, 0] )

			else:
				return convert( [255*mult, (510-510*curinr)*mult, 0] )
	else:
		return '#000000'


def draw_graph( canvas, tool_data, bed_data, ran=[ [0, 250], [0, 250] ], multtime=1, lastpos=(None, None) ):
	if not tool_data or not bed_data: return

	multtime=float(multtime)
	width=int( canvas['width'] )
	height=int( canvas['height'] )

	canvas.delete('all')

	tool_datastruct={}
	for x in tool_data['history']:
		tool_datastruct[ str( x['time'] ) ] = x['tool0']['actual'], x['tool0']['target']

	bed_datastruct={}
	for y in bed_data['history']:
		bed_datastruct[ str( y['time'] ) ] = y['bed']['actual'], y['bed']['target']


	tool_timeline=list( tool_datastruct.keys() )
	tool_timeline.sort()
	bed_timeline=list( bed_datastruct.keys() )
	bed_timeline.sort()

	toolactual=[]
	tooltarget=[]

	bedactual=[]
	bedtarget=[]

	t=time.time()

	for i in range(len(tool_timeline)):
		
		if i!=len(tool_timeline)-1:
			toolactual.append([	width-(t-int(tool_timeline[i]))/multtime,
								height-height*( float(tool_datastruct[tool_timeline[i]][0] )/ran[0][1] ),

								width-(t-int(tool_timeline[i + 1]))/multtime,
								height-height*( float(tool_datastruct[tool_timeline[i + 1]][0] )/ran[0][1] )])

	for i in range(len(tool_timeline)):

		if i!=len(tool_timeline)-1:
			tooltarget.append([	width-(t-int(tool_timeline[i]))/multtime,
								height-height*( float(tool_datastruct[tool_timeline[i]][1] )/ran[0][1] ),

								width-(t-int(tool_timeline[i + 1]))/multtime,
								height-height*( float(tool_datastruct[tool_timeline[i + 1]][1] )/ran[0][1] )])


	for i in range(len(bed_timeline)):
		
		if i!=len(bed_timeline)-1:
			bedactual.append([	width-(t-int(bed_timeline[i]))/multtime,
								height-height*( float(bed_datastruct[bed_timeline[i]][0] )/ran[1][1] ),

								width-(t-int(bed_timeline[i + 1]))/multtime,
								height-height*( float(bed_datastruct[bed_timeline[i + 1]][0] )/ran[1][1] )])

	for i in range(len(bed_timeline)):

		if i!=len(bed_timeline)-1:
			bedtarget.append([	width-(t-int(bed_timeline[i]))/multtime,
								height-height*( float(bed_datastruct[bed_timeline[i]][1] )/ran[1][1] ),

								width-(t-int(bed_timeline[i + 1]))/multtime,
								height-height*( float(bed_datastruct[bed_timeline[i + 1]][1] )/ran[1][1] )])


	for line in bedtarget:
		canvas.create_line( *line, fill=convert( [128,128,255] ) )

	for line in bedactual:
		canvas.create_line( *line, fill=convert( [0,0,255] ) )


	for line in tooltarget:
		canvas.create_line( *line, fill=convert( [255,128,128] ) )

	for line in toolactual:
		canvas.create_line( *line, fill=convert( [255,0,0] ) )

	if lastpos[0] and lastpos[1]:

		canvas.create_line( lastpos[0], 0, lastpos[0], height, fill='gray' )

		#canvas.create_line( 0, lastpos[1], width, lastpos[1], fill='gray' )

		temp_at_pos=[]

		for i in range(len(tool_timeline)):
			if lastpos[0] -8/multtime < width-(t-int(tool_timeline[i]))/multtime < lastpos[0] +8/multtime:
				temp_at_pos.append([ tool_datastruct[str(tool_timeline[i])], i ])
				break

		for i in range(len(bed_timeline)):
			if lastpos[0] -8/multtime < width-(t-int(bed_timeline[i]))/multtime < lastpos[0] +8/multtime:
				temp_at_pos.append([ bed_datastruct[str(bed_timeline[i])], i])
				break

		text_offset=[-10,-5]
		if temp_at_pos:

			canvas.create_text(lastpos[0]+text_offset[0], 
				height-height*( float(tool_datastruct[tool_timeline[ temp_at_pos[0][1] ]][0] )/ran[0][1] )-text_offset[1], 
				text="%.1f" % temp_at_pos[0][0][0], fill=convert( [128,0,0] ), font=('Arial', 8) )

			canvas.create_text(lastpos[0]+text_offset[0], 
				height-height*( float(bed_datastruct[bed_timeline[ temp_at_pos[1][1] ]][0] )/ran[0][1] )+text_offset[1], 
				text="%.1f" % temp_at_pos[1][0][0], fill=convert( [0,0,128] ), font=('Arial', 8) )


	canvas.create_text(
		15, 6, text="%.1f" % (8/multtime) )