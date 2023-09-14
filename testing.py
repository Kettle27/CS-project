from tkinter import *
from matplotlib.figure import Figure
import matplotlib as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np

root = Tk()
root.geometry("1200x700")

Range = np.linspace(-10,10,100)
y = [x**2 + 3*x + 3 for x in Range]


fig = Figure(figsize=(8,6))
ax = fig.add_subplot(111)
fig_canvas = FigureCanvasTkAgg(fig, root)
fig_canvas.draw()
fig_canvas.get_tk_widget().pack(anchor=NW)

toolbar = NavigationToolbar2Tk(fig_canvas, root)
toolbar.update()
fig_canvas.get_tk_widget().pack(anchor=SW)

def plotgraph(co):
    poly = np.poly1d(co)
    Range = np.linspace(-10,10,100)
    y = poly(Range)
    ax.plot(Range, y)
    ax.axvline(color = "black" , linestyle = "--")
    ax.axhline(color = "black", linestyle = "--")
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)
    ax.grid()


root.mainloop()