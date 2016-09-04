from Tkinter import *

def nothin(  ):
	print "Nope"


root = Tk(  )


menu = Menu( root )
root.config( menu=menu )

submenu = Menu( menu )
menu.add_cascade(label="FILE", menu=submenu)

submenu.add_command(label="New File", command=nothin)
submenu.add_command(label="New Document", command=nothin)
submenu.add_command(label="New Life", command=nothin)

submenu.add_separator()

submenu.add_command(label="QUIT!", command=root.quit)



submenu2 = Menu( menu )
menu.add_cascade(label="EDIT", menu=submenu2)

submenu2.add_command(label="Edit File", command=nothin)
submenu2.add_command(label="Edit Document", command=nothin)
submenu2.add_command(label="ADD MONEH!", command=nothin)


root.mainloop(  )