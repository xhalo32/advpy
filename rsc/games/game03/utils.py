
	## ======COMMANDS======

def write( arg ):
	return arg

def say( arg ):
	print arg

def create_snake( parent ):
	snake_amount = 0
	for obj in parent.handler.object_list:
		if isinstance( obj, parent.handler.Snake ): snake_amount += 1

	if snake_amount == 0: parent.handler.create( "Snake", { "speed" : [2,0] } )
	if snake_amount == 1: parent.handler.create( "Snake", { 
			"speed" : [2,0],
			"pos" : [ 100,100 ],
			"DN" : p.K_DOWN,
			"UP" : p.K_UP,
			"RT" : p.K_RIGHT,
			"LT" : p.K_LEFT,
			"color" : [ 200,200,50 ],
		} )
	if snake_amount == 2: parent.handler.create( "Snake", { 
			"speed" : [2,0],
			"pos" : [ 100, parent.scr.get_height(  ) - 100 ],
			"DN" : p.K_j,
			"UP" : p.K_u,
			"RT" : p.K_k,
			"LT" : p.K_h,
			"color" : [ 100,50,200 ],
		} )
