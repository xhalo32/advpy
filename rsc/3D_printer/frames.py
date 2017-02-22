from tkinter import *

class Frames:

	def __init__(self, master):
		self.master = master
		self.frames = \
{
	"status" :
	{
		'frame' : None,
		'packargs' :
		{
			'row' : 0,
			'ipady' : 5,
		},
		'frameargs' :
		{
			#'bg' : 'blue',
			'bg' : '#d8d8d8',
			'width' : 32,
		},

		'element_list' : {},		# empty dict for all the elements

		'labels' :
		[
			{
				'id' : 'print_name',		# identification for later value assignment
				'label' :			# Label and arguments
				{
					'text' : '',
					'bg' : '#e8e8e8',
					'width' : 32,
					'relief' : FLAT,
				},
				'grid' :			# grid and arguments
				{
					'row' : 0,
					'columnspan' : 2,
					'sticky' : 'nesw',
				},
				'tooltip' :
				{
					'text' : 'Print name',
					'follow_mouse' : 1,
					'delay' : 500,
					'bg' : '#b3b3b3',
					'relief' : FLAT,
				},
			},
		],

		'buttons' :
		[
			{
				'id' : 'btn_goto_main',
				'button' :
				{
					'text' : 'Main',
					'bg' : '#d8d8d8',
					'relief' : FLAT,
					'command' : lambda: self.master.raise_frame('main'),
				},
				'grid' :
				{
					'row' : 1,
					'column' : 0,
					'columnspan' : 1,
					'sticky' : 'we',
				},
				'tooltip' :
				{
					'text' : 'Main tab',
					'follow_mouse' : 1,
					'delay' : 500,
					'bg' : '#b3b3b3',
					'relief' : FLAT,
				},
			},
			{
				'id' : 'btn_goto_detail',
				'button' :
				{
					'text' : 'Detail',
					'bg' : '#d8d8d8',
					'relief' : FLAT,
					'command' : lambda: self.master.raise_frame('detail'),
				},
				'grid' :
				{
					'row' : 1,
					'column' : 1,
					'columnspan' : 1,
					'sticky' : 'we',
				},
				'tooltip' :
				{
					'text' : 'Detail Tab',
					'follow_mouse' : 1,
					'delay' : 500,
					'bg' : '#b3b3b3',
					'relief' : FLAT,
				},
			}
		],
	},

	"main" : 
	{
		'frame' : None,
		'packargs' :
		{
			'row' : 1,
			'sticky' : 'nesw',
		},
		'frameargs' :
		{
			'bg' : '#e8e8e8',
			#'bg' : 'red'
		},


		'element_list' : {},		# empty dict for all the elements

		'labels' :
		[
			{
				'id' : 'print_time_done',
				'label' :
				{
					'text' : '',
					'bg' : '#d8d8d8',
					'width' : 16,
					'relief' : FLAT,
				},
				'grid' :
				{
					'row' : 1,
					'column' : 0,
					'columnspan' : 1,
					'sticky' : 'nesw',
				},
				'tooltip' :
				{
					'text' : 'Time printed',
					'follow_mouse' : 1,
					'delay' : 500,
					'bg' : '#b3b3b3',
					'relief' : FLAT,
				},
			},

			{
				'id' : 'print_time_left',
				'label' :
				{
					'text' : '',
					'bg' : '#d8d8d8',
					'width' : 16,
					'relief' : FLAT,
				},
				'grid' :
				{
					'row' : 1,
					'column' : 1,
					'columnspan' : 1,
					'sticky' : 'nesw',
				},
				'tooltip' :
				{
					'text' : 'Time left',
					'follow_mouse' : 1,
					'delay' : 500,
					'bg' : '#b3b3b3',
					'relief' : FLAT,
				},
			},
		],

		'buttons' :
		[

		],

		'canvases' :
		[
			{
				'id' : 'bar_progress_time',
				'canvas' :
				{
					'bg' : '#d8d8d8',
					'width' : 0,
					'height' : 16,
				},
				'grid' :
				{
					'row' : 2,
					'columnspan' : 2,
					'sticky' : 'nesw',
				},
				'tooltip' :
				{
					'text' : 'Progress of time',
					'follow_mouse' : 1,
					'delay' : 500,
					'bg' : '#b3b3b3',
					'relief' : FLAT,
				},
				
			},
			{
				'id' : 'bar_progress',
				'canvas' :
				{
					'bg' : '#d8d8d8',
					'width' : 0,
					'height' : 16,
				},
				'grid' :
				{
					'row' : 3,
					'columnspan' : 2,
					'sticky' : 'nesw',
				},
				'tooltip' :
				{
					'text' : 'Progress',
					'follow_mouse' : 1,
					'delay' : 500,
					'bg' : '#b3b3b3',
					'relief' : FLAT,
				},
				
			},
		],
	},

	"detail" :
	{
		'frame' : None,
		'packargs' :
		{
			'row' : 1,
			'sticky' : 'nesw',
		},
		'frameargs' :
		{
			'bg' : 'green',
		},


		'element_list' : {},
		'labels' :
		[
			{
				'id' : 'kana',
				'label' :
				{
					'text' : 'Kukko',
					'width' : 32,
					'bg' : '#d8d8d8',
					'relief' : FLAT,
				},
				'grid' :
				{
					'row' : 0,
					'columnspan' : 2,
					'sticky' : 'e',
				},
				'tooltip' :
				{
					'text' : 'kaan',
					'follow_mouse' : 1,
					'delay' : 500,
					'bg' : '#b3b3b3',
					'relief' : FLAT,
				},
			},
		],
	},
}