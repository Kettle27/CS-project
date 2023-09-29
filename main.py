from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from matplotlib import backend_bases
from math import *
# from validation import Valid

backend_bases.NavigationToolbar2.toolitems = (
    ('Home', 'Reset original view', 'home', 'home'),
    ('Back', 'Back to  previous view', 'back', 'back'),
    ('Forward', 'Forward to next view', 'forward', 'forward'),
    (None, None, None, None),
    ('Pan', 'Pan axes with left mouse, zoom with right', 'move', 'pan'),
    ('Zoom', 'Zoom to rectangle', 'zoom_to_rect', 'zoom'),
    (None, None, None, None),)

class App(Frame):

    plotlist = []


    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()

        root.title('Plotting in Tkinter')
        root.geometry("1200x700")

        # Valid()
    
        self.main = Frame(self)
        self.launch_main()
        self.main.grid()

    def launch_main(self):

        self.subframe1 = Frame(self.main, width= 450, height=700, background="blue")
        self.subframe1.pack(side = RIGHT, fill=Y)

        self.plot_entry = Entry(self.subframe1, width=15, font= "Arial 30", state= DISABLED)
        self.plot_entry.place(x = 35, y = 50)

        self.plot_button = Button(self.subframe1, text = "Plot", width = 5, command=lambda:[self.plot_graph(self.plot_entry.get()), self.plot_entry.delete(0, END)])
        self.plot_button.place(x = 330, y = 185)

        Button(self.subframe1, text="1", width= 5,
               command= lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "1"), self.plot_entry.config(state = DISABLED)]
               ).place(x=15, y = 110)
        
        Button(self.subframe1, text="2", width= 5, command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "2"), self.plot_entry.config(state = DISABLED)]
               ).place(x=60, y = 110)
        
        Button(self.subframe1, text="3", width= 5, command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "3"), self.plot_entry.config(state = DISABLED)]
               ).place(x=105, y = 110)

        Button(self.subframe1, text="4", width= 5, command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "4"), self.plot_entry.config(state = DISABLED)]
               ).place(x=15, y = 135)

        Button(self.subframe1, text="5", width= 5, command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "5"), self.plot_entry.config(state = DISABLED)]
               ).place(x=60, y = 135)

        Button(self.subframe1, text="6", width= 5, command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "6"), self.plot_entry.config(state = DISABLED)]
               ).place(x=105, y = 135)

        Button(self.subframe1, text="7", width= 5, command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "7"), self.plot_entry.config(state = DISABLED)]
               ).place(x=15, y = 160)
        
        Button(self.subframe1, text="8", width= 5, command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "8"), self.plot_entry.config(state = DISABLED)]
               ).place(x=60, y = 160)

        Button(self.subframe1, text="9", width= 5, command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "9"), self.plot_entry.config(state = DISABLED)]
               ).place(x=105, y = 160)

        Button(self.subframe1, text="Delete", width= 5, command= 
               lambda: [self.plot_entry.config(state = NORMAL), self.plot_entry.delete(self.plot_entry.index("end")-1), self.plot_entry.config(state = DISABLED)]
               ).place(x=15, y = 185)
        
        Button(self.subframe1, text="0", width= 5, command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "9"), self.plot_entry.config(state = DISABLED)]
               ).place(x=60, y = 185)
        
        Button(self.subframe1, text="Clear", width= 5, command= 
               lambda: [self.plot_entry.config(state = NORMAL), self.plot_entry.delete(0, END), self.plot_entry.config(state = DISABLED)]
               ).place(x=105, y = 185)


        Button(self.subframe1, text="π", width= 5, command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "π"), self.plot_entry.config(state = DISABLED)]
               ).place(x=150, y = 110)

        Button(self.subframe1, text="e", width= 5, command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "e"), self.plot_entry.config(state = DISABLED)]
               ).place(x=195, y = 110)

        Button(self.subframe1, text="log", width= 5, command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "log"), self.plot_entry.config(state = DISABLED)]
               ).place(x=240, y = 110)

        Button(self.subframe1, text="sin", width= 5, command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "sin"), self.plot_entry.config(state = DISABLED)]
               ).place(x=150, y = 135)

        Button(self.subframe1, text="cos", width= 5, command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "cos"), self.plot_entry.config(state = DISABLED)]
               ).place(x=195, y = 135)
        
        Button(self.subframe1, text="tan", width= 5, command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "tan"), self.plot_entry.config(state = DISABLED)]
               ).place(x=240, y = 135)

        Button(self.subframe1, text="sinh", width= 5, command= lambda: self.plot_entry.insert(END, "sinh")).place(x=150, y = 160)
        Button(self.subframe1, text="cosh", width= 5, command= lambda: self.plot_entry.insert(END, "cosh")).place(x=195, y = 160)
        Button(self.subframe1, text="tanh", width= 5, command= lambda: self.plot_entry.insert(END, "tanh")).place(x=240, y = 160)

        Button(self.subframe1, text=".", width= 5, command= lambda: self.plot_entry.insert(END, ".")).place(x=150, y = 185)
        Button(self.subframe1, text="(", width= 5, command= lambda: self.plot_entry.insert(END, "(")).place(x=195, y = 185)
        Button(self.subframe1, text=")", width= 5, command= lambda: self.plot_entry.insert(END, ")")).place(x=240, y = 185)


        Button(self.subframe1, text="ln", width= 5, command= lambda: self.plot_entry.insert(END, "ln")).place(x=285, y = 110)
        Button(self.subframe1, text="-", width= 5, command= lambda: self.plot_entry.insert(END, "-")).place(x=330, y = 110)
        Button(self.subframe1, text="*", width= 5, command= lambda: self.plot_entry.insert(END, "*")).place(x=285, y = 160)

        Button(self.subframe1, text="/", width= 5, command= lambda: self.plot_entry.insert(END, "/")).place(x=285, y = 135)
        Button(self.subframe1, text="^", width= 5, command= lambda: self.plot_entry.insert(END, "**")).place(x=330, y = 135)
        Button(self.subframe1, text="x", width= 5, command= lambda: self.plot_entry.insert(END, "x")).place(x=330, y = 160)

        Button(self.subframe1, text="+", width= 5, command= lambda: self.plot_entry.insert(END, "+")).place(x=285, y = 185)

        self.subframe15 = Frame(self.subframe1, width= 200, height = 300, background="black")
        self.subframe15.place(x=35, y=500)

        self.scrollbar = Scrollbar(self.subframe15, width = 20)
        self.scrollbar.pack( side = RIGHT, fill=Y )
        self.mylist = Listbox(self.subframe15, yscrollcommand= self.scrollbar.set, width= 50)
        self.mylist.pack( side = LEFT, fill = BOTH )
        self.scrollbar.config( command = self.mylist.yview )


        self.edit_button = Button(self.subframe1, text="edit",width = 22)
        self.edit_button.place(x=35, y=664)

        self.delete_button = Button(self.subframe1, text="delete",width = 22, command=lambda:self.delete_graph())
        self.delete_button.place(x=196, y=664)


        self.subframe2 = Frame(self.main, width= 800, height=500, background="red")
        self.subframe2.pack(anchor=NW)


        self.fig= Figure(figsize = (8, 5), dpi = 100, facecolor="grey")
        self.ax = self.fig.add_subplot(111)
        self.ax.axvline(color="black", linestyle="--")
        self.ax.axhline(color="black", linestyle="--")
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.grid()
        self.ax.set_facecolor("snow")
        self.fig_canvas = FigureCanvasTkAgg(self.fig, master = self.subframe2)
        self.fig_canvas.draw()
        self.fig_canvas.get_tk_widget().pack()




        subframe3 = Frame(self.main, width= 800, height=200, background="green")
        subframe3.pack(anchor=S)

        toolbar = NavigationToolbar2Tk(self.fig_canvas, self.subframe2, pack_toolbar = False)
        toolbar.update()
        toolbar.pack(side = BOTTOM, fill = X)
        self.fig_canvas.get_tk_widget().pack()



    def plot_graph(self, fx):

        try:
            Range = np.linspace(-100,100,4000)
            y = [eval(fx) for x in Range]
            graph = self.ax.plot(Range, y)
            self.fig_canvas.draw()

            self.plotlist.append([fx , graph])
            self.mylist.insert(END, f"{self.mylist.size()+1}.  {fx}")
        except:
            pass

    def delete_graph(self):
        is_selected = self.mylist.curselection()
        if is_selected:

            get_info = self.plotlist[int(self.mylist.get(is_selected[0])[0]) - 1]

            self.plotlist.remove(get_info)
            line = get_info[1].pop(0)
            line.remove()
            self.fig_canvas.draw()

            self.mylist.delete(is_selected[0])

        



if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
