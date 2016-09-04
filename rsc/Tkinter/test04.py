from Tkinter import *
root = Tk(  )


lbl1 = Label( root, text="USR" )
lbl2 = Label( root, text="PASSWD" )

ent1 = Entry( root )
ent2 = Entry( root )

btn1 = Button( root, text="CONTINUE" )
ckb1 = Checkbutton( root, text="REMEMBER LOGIN" )


lbl1.grid( row=0, sticky=E )
lbl2.grid( row=1, sticky=E )

ent1.grid( row=0, column=1)
ent2.grid( row=1, column=1 )

ckb1.grid( columnspan=2 )

btn1.grid( columnspan=2 )



root.mainloop(  )