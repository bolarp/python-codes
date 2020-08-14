from tkinter import *
root = Tk()

onelabel = Label(root, text = 'one', fg = 'white', bg='black')
onelabel.pack()
twolabel = Label(root, text = 'two', fg = 'blue', bg='red')
twolabel.pack(fill=X)
threelabel = Label(root, text = 'three', fg = 'green', bg='purple')
threelabel.pack(side = LEFT, fill=Y)


"""topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

button1 = Button(topframe, text='click me', fg='red')
button2 = Button(topframe, text='click me', fg='blue')
button3 = Button(topframe, text='click me', fg='green')
button4 = Button(bottomframe, text='click me', fg='purple')

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)"""


root.mainloop()