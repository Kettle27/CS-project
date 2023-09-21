from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
import tkinter as tk
from matplotlib import backend_bases


backend_bases.NavigationToolbar2.toolitems = (
    ('Home', 'Reset original view', 'home', 'home'),
    ('Back', 'Back to  previous view', 'back', 'back'),
    ('Forward', 'Forward to next view', 'forward', 'forward'),
    (None, None, None, None),
    ('Pan', 'Pan axes with left mouse, zoom with right', 'move', 'pan'),
    ('Zoom', 'Zoom to rectangle', 'zoom_to_rect', 'zoom'),
    (None, None, None, None),)

class App(Frame):


    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()

        root.title('Plotting in Tkinter')
        root.geometry("1200x700")
    
        self.main = Frame(self)
        self.launch_main()
        self.main.grid()

    def launch_main(self):

        self.subframe1 = Frame(self.main, width= 400, height=700, background="blue")
        self.subframe1.pack(side = RIGHT, fill=Y)

        self.plot_entry = Entry(self.subframe1, width=15, font= "Arial 30" )
        self.plot_entry.place(x = 35, y = 50)

        self.plot_button = Button(self.subframe1, text = "Plot", font = "Arial 30", command=lambda:self.plotgraph([5,3,2,1]))
        self.plot_button.place(x = 35, y = 115)

        self.subframe15 = Frame(self.subframe1, width= 200, height = 300, background="black")
        self.subframe15.place(x=35, y=500)

        self.scrollbar = Scrollbar(self.subframe15, width = 20)
        self.scrollbar.pack( side = RIGHT, fill=Y )
        self.mylist = Listbox(self.subframe15, yscrollcommand= self.scrollbar.set, width= 50)
        self.mylist.pack( side = LEFT, fill = BOTH )
        self.scrollbar.config( command = self.mylist.yview )


        self.edit_button = Button(self.subframe1, text="edit",width = 22)
        self.edit_button.place(x=35, y=664)

        self.delete_button = Button(self.subframe1, text="delete",width = 22)
        self.delete_button.place(x=196, y=664)








        self.subframe2 = Frame(self.main, width= 800, height=500, background="red")
        self.subframe2.pack(anchor=NW)


        self.fig= Figure(figsize = (8, 5), dpi = 100)
        self.ax = self.fig.add_subplot(111)
        self.ax.axvline(color="black", linestyle="--")
        self.ax.axhline(color="black", linestyle="--")
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.grid()
        self.fig_canvas = FigureCanvasTkAgg(self.fig, master = self.subframe2)
        self.fig_canvas.draw()
        self.fig_canvas.get_tk_widget().pack()




        subframe3 = Frame(self.main, width= 800, height=200, background="green")
        subframe3.pack(anchor=S)

        toolbar = NavigationToolbar2Tk(self.fig_canvas, self.subframe2, pack_toolbar = False)
        toolbar.update()
        toolbar.pack(side = BOTTOM, fill = X)
        self.fig_canvas.get_tk_widget().pack()



    def plotgraph(self, co):
        poly = np.poly1d(co)
        Range = np.linspace(-10,10,200)
        y = poly(Range)
        self.ax.plot(Range, y)
        self.fig_canvas.draw()
        #poly = (str(np.poly1d([6,5,3,2,1])).split("\n"))
        #self.mylist.insert(END, f" {poly[0]}")
        #self.mylist.insert(END, f"{poly[1]}")




if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()

