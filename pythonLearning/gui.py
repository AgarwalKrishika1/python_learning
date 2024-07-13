import tkinter as tk
r = tk.Tk()
r.title('gui trial')
#button
button = tk.Button(r, text='Stop',background= 'black',foreground= 'white',
                   activebackground= 'red', activeforeground= 'white' , width=30, command= r.destroy)
#button.pack()
button1 = tk.Button(r, text='wait',background= 'black',foreground= 'white',
                    activebackground= 'red', activeforeground= 'white' , width=30, command= r.config)
button.pack()
button1.pack()
r.mainloop()
from tkinter import *
master = Tk()
#w = Canvas(master, width=50, height=100)
#w.pack()
#canvas_height=50
#canvas_width=500
#y = int(canvas_height/2)
#w.create_line(0, y, canvas_width, y)

var1= IntVar()
Radiobutton(master, text='male', variable=var1, value=1).grid(row=0, sticky=W)
var2= IntVar()
Radiobutton(master, text='female', variable=var2, value=2).grid(row=1, sticky=W)
Label(master, text='First name').grid(row=3)
Label(master, text='Last name').grid(row=4)
e= Entry(master)
e1= Entry(master)
e.grid(row=3, column=1)
e1.grid(row=4, column=1)

w =Label(master, text='first try')
w.grid()

lb= Listbox(master)
lb.insert(1, 'a')
lb.insert(2, 'b')
lb.insert(3, 'c')
lb.insert(4, 'd')
lb.grid(row=3, column=3)

mb = Menubutton( text= 'gfg')
mb.grid()
mb.menu = Menu(mb, tearoff = 0)
mb["menu"]= mb.menu
cVar = IntVar()
aVar = IntVar()
mb.menu.add_checkbutton( label='Contact', variable= cVar)
mb.menu.add_checkbutton( label='About', variable= aVar)
mb.grid()

menu = Menu(master)
master.config(menu=menu)
filename = Menu(menu)
menu.add_cascade(label='File', menu=filename)
filename.add_command(label='New')
filename.add_command(label='Open...')
filename.add_separator()
filename.add_command(label='Exit', command=master.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

ourMessage= 'this is my message'
messageVar= Message(master, text=ourMessage)
messageVar.config(bg='pink')
messageVar.grid()

w= Scale(master, from_=0, to=100)
w.grid(row=6, column=1)
w=Scale(master, from_=0, to=10, orient=HORIZONTAL)
w.grid(row=6, column=2)

master = Tk()
w = Spinbox(master, from_ = 0, to = 10)
w.grid(row=7, column=2)

#m1 = PanedWindow()
#m1.pack(fill = BOTH, expand = 1)
#left = Entry(m1, bd = 5)
#m1.add(left)
#m2 = PanedWindow(m1, orient = VERTICAL)
#m1.add(m2)
#top = Scale( m2, orient = HORIZONTAL)
#m2.add(top)
master.mainloop()