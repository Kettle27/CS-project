from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from matplotlib import backend_bases
from matplotlib.widgets import Button as Btn
from math import *
from maths import fact
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

              root.title('GraphingCalc.exe')
              root.geometry("1200x700")

              # Valid()
    
              self.main = Frame(self)
              self.launch_main()
              self.main.grid()


       def launch_main(self):

              self.subframe1 = Frame(self.main, width= 450, height=700, background="#3c4043")
              self.subframe1.pack(side = RIGHT, fill=Y)

              self.dimwidgets()

              self.subframe15 = Frame(self.subframe1, width= 200, height = 300, background="black")
              self.subframe15.place(x=10, y=276)

              self.scrollbar = Scrollbar(self.subframe15, width = 20)
              self.scrollbar.pack( side = RIGHT, fill=Y )
              self.mylist = Listbox(self.subframe15, yscrollcommand= self.scrollbar.set, width= 50, font = "Arial 10", borderwidth= 6)
              self.mylist.pack( side = LEFT, fill = BOTH )
              self.scrollbar.config( command = self.mylist.yview )


              self.subframe2 = Frame(self.main, width= 800, height=500, background="red")
              self.subframe2.pack(anchor=NW)

              self.fig = Figure(figsize = (8, 5), dpi = 100)

              self.dim_indx = self.fig.add_axes([0.9, 0.9, 0.09, 0.075])
              self.dim_indx_btn = Btn(self.dim_indx, "2D")
              self.dim_indx_btn.on_clicked(lambda x: Index())

              self.ax = self.fig.add_subplot(111)
              self.ax.axvline(color="black", linestyle="--")
              self.ax.axhline(color="black", linestyle="--")
              self.ax.set_xlim(-10, 10)
              self.ax.set_ylim(-10, 10)
              self.ax.set_ylabel("Y")
              self.ax.set_xlabel("X")
              self.ax.grid()
              self.ax.set_facecolor("snow")
              self.fig_canvas = FigureCanvasTkAgg(self.fig, master = self.subframe2)

              self.fig_canvas.draw()
              self.fig_canvas.get_tk_widget().pack()

              toolbar = NavigationToolbar2Tk(self.fig_canvas, self.subframe2, pack_toolbar = False)
              toolbar.update()
              toolbar.pack(side = BOTTOM, fill = X)
              self.fig_canvas.get_tk_widget().pack()


              self.subframe3 = Frame(self.main, width= 800, height=200, background="#3c4043")
              self.subframe3.pack(anchor=S)

       def dimwidgets(self):

              self.plot_entry = Entry(self.subframe1, bg= "#3C4043", width=17, borderwidth= 6, font= "Arial 30", state= DISABLED)
              self.plot_entry.place(x = 6, y = 11)

              Button(self.subframe1, text="sin", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "sin"), self.plot_entry.config(state = DISABLED)]
               ).place(x=5, y = 70)

              Button(self.subframe1, text="cos", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "cos"), self.plot_entry.config(state = DISABLED)]
               ).place(x=5, y = 109)
              
              Button(self.subframe1, text="tan", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "tan"), self.plot_entry.config(state = DISABLED)]
               ).place(x=5, y = 148)
              
              Button(self.subframe1, text="x", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "x"), self.plot_entry.config(state = DISABLED)]
               ).place(x=5, y = 187)
              
              Button(self.subframe1, text="y", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "y"), self.plot_entry.config(state = DISABLED)]
               ).place(x=5, y = 226)



              Button(self.subframe1, text="^", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "**"), self.plot_entry.config(state = DISABLED)]
               ).place(x=70, y = 70)

              Button(self.subframe1, text="!", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "fact"), self.plot_entry.config(state = DISABLED)]
               ).place(x=70, y = 109)
              
              Button(self.subframe1, text="log", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "log"), self.plot_entry.config(state = DISABLED)]
               ).place(x=70, y = 148)
              
              Button(self.subframe1, text="e", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "e"), self.plot_entry.config(state = DISABLED)]
               ).place(x=70, y = 187)
              
              Button(self.subframe1, text="π", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "pi"), self.plot_entry.config(state = DISABLED)]
               ).place(x=70, y = 226)



              Button(self.subframe1, text="(", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "("), self.plot_entry.config(state = DISABLED)]
               ).place(x=135, y = 70)
              
              Button(self.subframe1, text="1", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "1"), self.plot_entry.config(state = DISABLED)]
               ).place(x=135, y = 109)
              
              Button(self.subframe1, text="4", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "4"), self.plot_entry.config(state = DISABLED)]
               ).place(x=135, y = 148)

              Button(self.subframe1, text="7", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "7"), self.plot_entry.config(state = DISABLED)]
               ).place(x=135, y = 187)

              Button(self.subframe1, text="0", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "0"), self.plot_entry.config(state = DISABLED)]
               ).place(x=135, y = 226)
              


              Button(self.subframe1, text=")", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, ")"), self.plot_entry.config(state = DISABLED)]
               ).place(x=200, y = 70)

              Button(self.subframe1, text="2", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "2"), self.plot_entry.config(state = DISABLED)]
               ).place(x=200, y = 109)
              
              Button(self.subframe1, text="5", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "5"), self.plot_entry.config(state = DISABLED)]
               ).place(x=200, y = 148)

              Button(self.subframe1, text="8", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "8"), self.plot_entry.config(state = DISABLED)]
               ).place(x=200, y = 187)
              
              Button(self.subframe1, text=".", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "."), self.plot_entry.config(state = DISABLED)]
               ).place(x=200, y = 226)



              Button(self.subframe1, text="Delete", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL), self.plot_entry.delete(self.plot_entry.index("end")-1), self.plot_entry.config(state = DISABLED)]
               ).place(x=265, y = 70)
        
              Button(self.subframe1, text="3", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "3"), self.plot_entry.config(state = DISABLED)]
               ).place(x=265, y = 109)

              Button(self.subframe1, text="6", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "6"), self.plot_entry.config(state = DISABLED)]
               ).place(x=265, y = 148)

              Button(self.subframe1, text="9", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "9"), self.plot_entry.config(state = DISABLED)]
               ).place(x=265, y = 187)
        
              Button(self.subframe1, text = "Plot", width = 5, font = "Arial 15", bg = "#8ab4f8", fg = "#202124", command=
               lambda:[self.plot_entry.config(state = NORMAL), Graph_tools.plot_graph(self.plot_entry.get()), self.plot_entry.delete(0, END), self.plot_entry.config(state = DISABLED)]
               ).place(x = 265, y = 226)



              Button(self.subframe1, text="Clear", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL), self.plot_entry.delete(0, END), self.plot_entry.config(state = DISABLED)]
               ).place(x=330, y = 70)
              
              Button(self.subframe1, text="÷", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "/"), self.plot_entry.config(state = DISABLED)]
               ).place(x=330, y = 109)
              
              Button(self.subframe1, text="*", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "*"), self.plot_entry.config(state = DISABLED)]
               ).place(x=330, y = 148)
              
              Button(self.subframe1, text="-", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "-"), self.plot_entry.config(state = DISABLED)]
               ).place(x=330, y = 187)
              
              Button(self.subframe1, text="+", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) ,self.plot_entry.insert(END, "+"), self.plot_entry.config(state = DISABLED)]
               ).place(x=330, y = 226)
              
              

              Button(self.subframe1, text="edit", width = 15, font = "Arial 16", bg = "#5f6368", fg = "#e8eaed", borderwidth= 3, command=
               lambda:Graph_tools.edit_graph()
               ).place(x=10, y=461)


              Button(self.subframe1, text="delete",width = 15, font = "Arial 16", bg = "#5f6368", fg = "#e8eaed", borderwidth= 3, command=
               lambda:Graph_tools.delete_graph()
               ).place(x=203, y=461)



       



class Graph_tools(App):

       @staticmethod
       def plot_graph(fx):
              if str(app.dim_indx_btn.label)[16:18] == "2D":
                     try:
                            x = np.linspace(-50,50,2000)
                            y = [eval(fx) for x in x]
                            graph = app.ax.plot(x, y)
                            app.fig_canvas.draw()

                            app.plotlist.append([fx , graph])
                            app.mylist.insert(END, f" y = {fx}")
                     except:
                            pass

              if str(app.dim_indx_btn.label)[16:18] == "3D":
                     try:
                            x = y = np.linspace(-10, 10, 100)
                            X, Y = np.meshgrid(x, y)
                            zs = np.array([eval(fx) for x,y in zip(X,Y)])
                            Z = zs.reshape(X.shape)

                            graph = app.ax.plot_surface(X,Y,Z)
                            app.fig_canvas.draw()

                            app.plotlist.append([fx , graph])
                            app.mylist.insert(END, f" z = {fx}")
                     except:
                            pass


       @staticmethod             
       def delete_graph():
              is_selected = app.mylist.curselection()
              if is_selected:
                     if str(app.dim_indx_btn.label)[16:18] == "2D":

                            get_info = app.plotlist[is_selected[0]]
                            app.plotlist.remove(get_info)
                            line = get_info[1].pop()
                            line.remove()

                            app.fig_canvas.draw()
                            app.mylist.delete(is_selected[0])

                     if str(app.dim_indx_btn.label)[16:18] == "3D":

                            get_info = app.plotlist[is_selected[0]]
                            app.plotlist.remove(get_info)
                            get_info[1].remove()

                            app.fig_canvas.draw()
                            app.mylist.delete(is_selected[0])
    

       @staticmethod
       def edit_graph():
              is_selected = app.mylist.curselection()
              if is_selected:
                     if str(app.dim_indx_btn.label)[16:18] == "2D":
                     
                            get_info = app.plotlist[is_selected[0]]
                            app.plotlist.remove(get_info)
                            line = get_info[1].pop(0)
                            line.remove()
                            app.fig_canvas.draw()
                            app.mylist.delete(is_selected[0])
                            app.plot_entry.config(state=NORMAL)
                            app.plot_entry.insert(END, get_info[0])
                            app.plot_entry.config(state=DISABLED)

                     if str(app.dim_indx_btn.label)[16:18] == "3D":
                     
                            get_info = app.plotlist[is_selected[0]]
                            app.plotlist.remove(get_info)
                            get_info[1].remove()
                            app.fig_canvas.draw()
                            app.mylist.delete(is_selected[0])
                            app.plot_entry.config(state=NORMAL)
                            app.plot_entry.insert(END, get_info[0])
                            app.plot_entry.config(state=DISABLED)
        

class Index(App):


       def __init__(self):

            if str(app.dim_indx_btn.label)[16:18] == "2D":
                self.dim3()

            elif str(app.dim_indx_btn.label)[16:18] == "3D":
                self.dim2()


       def dim2(self):

            app.fig.delaxes(app.fig.axes[1])

            app.ax = app.fig.add_subplot(111)
            app.ax.axvline(color="black", linestyle="--")
            app.ax.axhline(color="black", linestyle="--")
            app.ax.set_xlim(-10, 10)
            app.ax.set_ylim(-10, 10)
            app.ax.set_ylabel("Y")
            app.ax.set_xlabel("X")
            app.ax.grid()

            app.dim_indx_btn.label.set_text("2D")
            app.plotlist = []
            app.mylist.delete(0, END)
            app.fig_canvas.draw()
       

       def dim3(self):
            app.fig.delaxes(app.fig.axes[1])

            app.ax = app.fig.add_subplot(111, projection="3d")
            app.ax.set_xlim(-10, 10)
            app.ax.set_ylim(-10, 10)
            app.ax.set_ylabel("Y")
            app.ax.set_xlabel("X")
            app.ax.set_zlabel("Z")


            app.dim_indx_btn.label.set_text("3D")
            app.plotlist = []
            app.mylist.delete(0, END)

            app.fig_canvas.draw()


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()                
