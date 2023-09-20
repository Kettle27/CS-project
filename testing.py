from tkinter import *
from matplotlib.figure import Figure
import matplotlib as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np




class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()

        root.geometry("1200x700")
        root.title("GraphingCalc.exe")

        self.mainFrame = Frame(self)
        self.create_main_program()
        self.mainFrame.grid()


    def create_main_program(self):

        subframe1 = Frame(root, width = 400, height = 700)
        subframe1.pack(side = left)

        subframe2 = Frame(root, width = 800, height = 500)
        subframe2.pack(anchor = NW)

        fig = Figure(figsize=(8,6))
        ax = fig.add_subplot(111)
        fig_canvas = FigureCanvasTkAgg(fig, root)
        fig_canvas.draw()
        fig_canvas.get_tk_widget().pack(anchor=NW)
        ax.axvline(color = "black" , linestyle = "--")
        ax.axhline(color = "black", linestyle = "--")
        ax.set_xlim(-10,10)
        ax.set_ylim(-10,10)
        ax.grid()

        subframe3 = Frame(root, width = 800, height = 200)
        subframe3.pack(anchor = SW)

        toolbar = NavigationToolbar2Tk(fig_canvas, root)
        toolbar.update()
        fig_canvas.get_tk_widget().pack()

        def plotgraph(co):
            poly = np.poly1d(co)
            Range = np.linspace(-10,10,100)
            y = poly(Range)
            ax.plot(Range, y)



if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
    
