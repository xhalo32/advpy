import json

settings_json = json.dumps( 
	[ 
		{
			'type' : 'title',
			'title' : 'ex title lalala',
		},
		{
			'type' : 'bool',
			'title' : 'a boolean value',
			'desc' : 'Description',
			'section' : 'example',
			'key' : 'boolex',
		},
		{
			'type' : 'numeric',
			'title' : 'a numeric value',
			'desc' : 'Description',
			'section' : 'example',
			'key' : 'intex',
		},
		{
			'type' : 'options',
			'title' : 'a boolean value',
			'desc' : 'Description',
			'section' : 'example',
			'key' : 'optionex',
			'options' : [ '1', '2', '3' ]
		},
		{
			'type' : 'string',
			'title' : 'a string',
			'desc' : 'Description',
			'section' : 'example',
			'key' : 'stringex',
		},
		{
			'type' : 'path',
			'title' : 'a path',
			'desc' : 'Description',
			'section' : 'example',
			'key' : 'pathex',
		},
	]
)