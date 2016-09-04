import Tkinter

root = Tkinter.Tk()

def fill(image, color):
  r,g,b = color
  width = image.width()
  height = image.height()
  hexcode = "#%02x%02x%02x" % (r,g,b)
  horizontal_line = "{" + " ".join([hexcode]*width) + "}"
  image.put(" ".join([horizontal_line]*height))
 
photo = Tkinter.PhotoImage(width=32, height=32)

fill(photo, (255,0,0))  # Fill with red...

label = Tkinter.Label(root, image=photo)
label.grid()
root.mainloop()