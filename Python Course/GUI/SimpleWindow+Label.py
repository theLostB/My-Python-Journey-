from tkinter import *

root = Tk()

# Width X Height 
#geometry defines the size of window
root.geometry("644x434")
#minsize stops reducing the size of window when it comes to it given size
root.minsize(80,65)
root.maxsize(900,800)
text = Label(text="Hello World!")
text.pack()

root.mainloop()