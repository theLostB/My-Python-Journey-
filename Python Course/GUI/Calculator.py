from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(scvalue.get())
            except Exception as e:
                scvalue.set("Error")
                screen.update()
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        scvalue.update()
    else:
        scvalue.set(scvalue.get() + text)
        scvalue.update()

root = Tk()
root.geometry("644x900")
root.title("Calculator by LostBoy")
root.configure(bg="yellow")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=99, padx=10)

fr = Frame(root)
frm = Frame(root)
f = Frame(root, bg="lightyellow")

b = Button(f, text="9", padx=21, pady=18, font="lucida 25 bold", bg='white')
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=21, pady=18, font="lucida 25 bold", bg='white')
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=21, pady=18, font="lucida 25 bold", bg='white')
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=21, pady=18, font="lucida 25 bold", bg='white')
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="lightyellow")

b = Button(f, text="6", padx=21, pady=18, font="lucida 25 bold", bg='white')
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=21, pady=18, font="lucida 25 bold", bg='white')
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=21, pady=18, font="lucida 25 bold", bg='white')
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=29, pady=18, font="lucida 25 bold", bg='white')
b.pack(side=LEFT, padx=17, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="lightyellow")

b = Button(f, text="3", padx=21, pady=18, font="lucida 25 bold", bg="white")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=21, pady=18, font="lucida 25 bold", bg='white')
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=21, pady=18, font="lucida 25 bold", bg='white')
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=27, pady=18, font="lucida 25 bold", bg='white')
b.pack(side=LEFT, padx=16, pady=5)
b.bind("<Button-1>", click)
f.pack()
frm.pack(pady=60)


f = Frame(root, bg="lightyellow")

b = Button(f, text="C", padx=25, pady=18, font="lucida 25 bold", bg='white')
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="0", padx=25, pady=18, font="lucida 25 bold", bg='white')
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=25, pady=18, font="lucida 25 bold", bg='white')
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=25, pady=18, font="lucida 25 bold", bg='white')
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=31, pady=18, font="lucida 25 bold", bg='white')
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()
fr.pack()

root.mainloop()