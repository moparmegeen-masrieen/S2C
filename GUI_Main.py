from tkinter import *
from PIL import Image,ImageTk


# This Is the main GUI for the program
# First i made the Form1 class with inherting Frame class from tkinter

class Form1(Frame):
    # Here we set our configuration through initialization class here we can specify:
    def __init__(self, master=None):
        # parameters that we want to send through Frame class
        Frame.__init__(self, master)
        # reference to the master widget which is tk window
        self.master = master
        # calling the function init_window which we will create later and making it a part of __init__ and running it
        self.init_window()
    # here we define the function init_window
    def init_window(self):
        # Here we make the master widget's title to 'Task Killer'
        self.master.title('Task Killer')
        # Allowing the window to take fill size of the widget
        self.pack(fill=BOTH, expand=1)

        # Making Quit button and it's event handling
        quit_button = Button(self, text='   Quit\t', command=self.exit_program)
        quit_button.place(y=0, x=0)

        # Making Count button and it's event handling
        count_button = Button(self, text='Count evens until 100\nto make\ntriangle of numbers', command=self.count_even)
        count_button.place(y=150, x=150)

        # Making the mnu bar and configuring it
        menu_bar = Menu(self.master)
        self.master.config(menu=menu_bar)

        # Creating file object in the menu bar
        file = Menu(menu_bar)
        # Here we add a command that runs on exit_program event
        file.add_command(label='Exit', command=self.exit_program)
        file.add_command(label='Show Image', command=self.showimg)
        file.add_command(label='Show Text', command=self.showtxt)
        # adding the File cascade window to the menu bar
        menu_bar.add_cascade(label='File', menu=file)

    def exit_program(self):
        exit()

    def count_even(self):
        list_even = []
        for i in range(2, 100, 2):
            list_even.append(i)
            print(list_even)

    def showimg(self):
        open_image = Image.open('images.jpg')
        render = ImageTk.PhotoImage(open_image)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def showtxt(self):
        text = Label(self, text='Hey There Thatsa nice program')
        text.pack()
        text.place(x=200, y=200)


# Here we create the root window and specify it's starting size
app = Tk()
app.geometry("400x400")
# here we create the window instance
form = Form1(app)
# the mainloop
app.mainloop()
