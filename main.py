# Computer Science Project 
# Author - George Sil



# Add all needed Libraries


from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib import backend_bases
from matplotlib.widgets import Button as Btn


# Add my other files


from extension import *
import validation
from db_handler import *


# Configure which matplotlib tools to use
# Currently - Home, Back, Forward, Pan, Zoom


backend_bases.NavigationToolbar2.toolitems = (
    ('Home', 'Reset original view', 'home', 'home'),
    ('Back', 'Back to  previous view', 'back', 'back'),
    ('Forward', 'Forward to next view', 'forward', 'forward'),
    ('Pan', 'Pan axes with left mouse, zoom with right', 'move', 'pan'),
    ('Zoom', 'Zoom to rectangle', 'zoom_to_rect', 'zoom'))


# Create class called App to be the main Tkinter Frame


class App(Frame):
       
       
       def __init__(self, master):


              super(App, self).__init__(master)


              # grid self


              self.grid()


              # title of program


              root.title('GraphingCalc')


              # dimentions of the screen (in pixels)


              root.geometry("1200x700")


              # grid the main Frame as self.main
              # call method self.launch_main to add widgets and subframes to main Frame
    

              self.main = Frame(self)
              self.launch_main()
              self.main.grid()




       def launch_main(self):


              # create all subframes


              # calculatorFrame holds all the calculator Tkinter buttons and a Tkinter entries


              self.calculatorFrame = Frame(self.main, width= 450, height=700, background="#3c4043")
              self.calculatorFrame.pack(side = RIGHT, fill=Y)


              # calculatorFrame2 holds the Tkinter listbox and the Tkinter Scrollbar
              # used for displaying the current equations and helping to edit and delete equations

              self.calculatorFrame2  = Frame(self.calculatorFrame , width= 200, height = 300, background="#3c4043")
              self.calculatorFrame2.place(x=10, y=276)

              
              # plotFrame holds the matplotlib graph aswell as a matplotlib button which calls the class Index

              self.plotFrame = Frame(self.main, width= 800, height= 500)
              self.plotFrame.pack(anchor=NW)


              # meta_dataFrame is a work in progress
              # meta_dataFrame will hold metadata on graphs (roots, y-intercepts, turning points)

              self.meta_dataFrame = Frame(self.main, width= 800, height=200, background="#3c4043")
              self.meta_dataFrame.pack(anchor=S)


              # call dimwidgets to add all widgets to their subframe


              self.dimwidgets()

                     
                     


       def dimwidgets(self):


              # plot_entry holds the equation for the graph
              # plot_entry is disabled so that you can only input when to press the calculator buttons


              self.plot_entry = Entry(self.calculatorFrame , bg= "#3C4043", width=17, borderwidth= 6, font= "Arial 30", state= DISABLED)
              self.plot_entry.place(x = 6, y = 11)


              # Buttons below when clicked insert a value to the entry using the entry_stack class


              Button(self.calculatorFrame , text="sin", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("sin"), self.plot_entry.config(state = DISABLED)]
               ).place(x=5, y = 70)


              Button(self.calculatorFrame , text="cos", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("cos"), self.plot_entry.config(state = DISABLED)]
               ).place(x=5, y = 109)
              

              Button(self.calculatorFrame , text="tan", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("tan"), self.plot_entry.config(state = DISABLED)]
               ).place(x=5, y = 148)
              

              Button(self.calculatorFrame , text="x", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("x"), self.plot_entry.config(state = DISABLED)]
               ).place(x=5, y = 187)
              

              Button(self.calculatorFrame , text="y", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("y"), self.plot_entry.config(state = DISABLED)]
               ).place(x=5, y = 226)



              Button(self.calculatorFrame , text="^", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("^"), self.plot_entry.config(state = DISABLED)]
               ).place(x=70, y = 70)


              Button(self.calculatorFrame , text="!", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("fact"), self.plot_entry.config(state = DISABLED)]
               ).place(x=70, y = 109)
              

              Button(self.calculatorFrame , text="log", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("log"), self.plot_entry.config(state = DISABLED)]
               ).place(x=70, y = 148)
              

              Button(self.calculatorFrame , text="e", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("e"), self.plot_entry.config(state = DISABLED)]
               ).place(x=70, y = 187)
              

              Button(self.calculatorFrame , text="π", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("pi"), self.plot_entry.config(state = DISABLED)]
               ).place(x=70, y = 226)



              Button(self.calculatorFrame , text="(", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("("), self.plot_entry.config(state = DISABLED)]
               ).place(x=135, y = 70)
              

              Button(self.calculatorFrame , text="1", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("1"), self.plot_entry.config(state = DISABLED)]
               ).place(x=135, y = 109)
              

              Button(self.calculatorFrame , text="4", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("4"), self.plot_entry.config(state = DISABLED)]
               ).place(x=135, y = 148)


              Button(self.calculatorFrame , text="7", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("7"), self.plot_entry.config(state = DISABLED)]
               ).place(x=135, y = 187)


              Button(self.calculatorFrame , text="0", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("0"), self.plot_entry.config(state = DISABLED)]
               ).place(x=135, y = 226)
              


              Button(self.calculatorFrame , text=")", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push(")"), self.plot_entry.config(state = DISABLED)]
               ).place(x=200, y = 70)


              Button(self.calculatorFrame , text="2", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("2"), self.plot_entry.config(state = DISABLED)]
               ).place(x=200, y = 109)
              

              Button(self.calculatorFrame , text="5", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("5"), self.plot_entry.config(state = DISABLED)]
               ).place(x=200, y = 148)


              Button(self.calculatorFrame , text="8", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("8"), self.plot_entry.config(state = DISABLED)]
               ).place(x=200, y = 187)
              

              Button(self.calculatorFrame , text=".", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("."), self.plot_entry.config(state = DISABLED)]
               ).place(x=200, y = 226)


              # button below deletes the end string if there is one


              Button(self.calculatorFrame , text="Delete", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL), entry_stack.pop(), self.plot_entry.config(state = DISABLED)]
               ).place(x=265, y = 70)
        


              Button(self.calculatorFrame , text="3", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("3"), self.plot_entry.config(state = DISABLED)]
               ).place(x=265, y = 109)


              Button(self.calculatorFrame , text="6", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("6"), self.plot_entry.config(state = DISABLED)]
               ).place(x=265, y = 148)


              Button(self.calculatorFrame , text="9", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("9"), self.plot_entry.config(state = DISABLED)]
               ).place(x=265, y = 187)
              

              # button below plots the equation held in plot_entry and calls the staticmethod plot_graph from the class Graph_tools
              # button also clears plot_entry
        
              Button(self.calculatorFrame , text = "Plot", width = 5, font = "Arial 15", bg = "#8ab4f8", fg = "#202124", command=
               lambda:[self.plot_entry.config(state = NORMAL), Graph_tools.plot_graph(self.plot_entry.get()), entry_stack.pull(), self.plot_entry.config(state = DISABLED)]
               ).place(x = 265, y = 226)


              # button below clears plot_entry


              Button(self.calculatorFrame , text="Clear", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL), entry_stack.pull(), self.plot_entry.config(state = DISABLED)]
               ).place(x=330, y = 70)
              

              Button(self.calculatorFrame , text="÷", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("/"), self.plot_entry.config(state = DISABLED)]
               ).place(x=330, y = 109)
              

              Button(self.calculatorFrame , text="*", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("*"), self.plot_entry.config(state = DISABLED)]
               ).place(x=330, y = 148)
              

              Button(self.calculatorFrame , text="-", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("-"), self.plot_entry.config(state = DISABLED)]
               ).place(x=330, y = 187)
              

              Button(self.calculatorFrame , text="+", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command= 
               lambda: [self.plot_entry.config(state = NORMAL) , entry_stack.push("+"), self.plot_entry.config(state = DISABLED)]
               ).place(x=330, y = 226)
              
              
              # button below allows the user to edit a graph that is selected in the Tkinter Listbox
              # button calls staticmethod edit_graph from the class Graph_tools


              Button(self.calculatorFrame , text="edit", width = 15, font = "Arial 16", bg = "#5f6368", fg = "#e8eaed", borderwidth= 3, command=
               lambda:Graph_tools.edit_graph()
               ).place(x=10, y=461)


              # button below allows the user to delete a graph that is selected in the Tkinter Listbox
              # button calls staticmethod delete_graph from the class Graph_tools


              Button(self.calculatorFrame , text="delete",width = 15, font = "Arial 16", bg = "#5f6368", fg = "#e8eaed", borderwidth= 3, command=
               lambda:Graph_tools.delete_graph()
               ).place(x=203, y=461)
              

              # below is a Tkinter slider which represents the theta value of when we want to rotate a graph


              self.slider = Scale(self.meta_dataFrame, from_=0, to=360, bg = "#5f6368", fg = "#e8eaed", troughcolor= "#5f6368", borderwidth= 3, orient= HORIZONTAL, length= 200, command=
               lambda x :dim2_rotation_matrix())
              self.slider.place(x=10,y=10)


              # added Tkinter Scrollbar to scroll on the Listbox if needed
              # Tkinter Scrollbar is attacted to the entire right side of the Listbox


              self.scrollbar = Scrollbar(self.calculatorFrame2 , width = 20)
              self.scrollbar.pack( side = RIGHT, fill=Y )


              # create Tkinter Listbox in calculatorFrame2 subframe
              # allow the scrollbar to scroll the listbox if needed
              # config Listbox command after Listbox is created because command calls itself


              self.mylist = Listbox(self.calculatorFrame2 , yscrollcommand= self.scrollbar.set, width= 50, font = "Arial 10", borderwidth= 6)
              self.mylist.pack(side = LEFT, fill = BOTH )
              self.scrollbar.config(command = self.mylist.yview )

              # create matplotlib Figure


              self.fig = Figure(figsize = (8, 5), dpi = 100)


              # create matplotlib button to call class Index which changes dimention of graph


              self.dim_indx = self.fig.add_axes([0.9, 0.9, 0.09, 0.075])
              self.dim_indx_btn = Btn(self.dim_indx, "2D")
              self.dim_indx_btn.on_clicked(lambda x: Index())


              # create the subplot for which we are graphing


              self.ax = self.fig.add_subplot(111)


              # axvline and axhline creates lines which cross x = 0 and y = 0


              self.ax.axvline(color="black", linestyle="--")
              self.ax.axhline(color="black", linestyle="--")


              # set x and y axis limit to -10 and 10


              self.ax.set_xlim(-10, 10)
              self.ax.set_ylim(-10, 10)


              # label x and y axis


              self.ax.set_ylabel("Y")
              self.ax.set_xlabel("X")


              # create grid on graph


              self.ax.grid()


              # backend the matplotlib figure to the tkinter subframe
              # draw graph
               

              self.fig_canvas = FigureCanvasTkAgg(self.fig, master = self.plotFrame)
              self.fig_canvas.draw()
              self.fig_canvas.get_tk_widget().pack()


              # add built-in matplotlib toolbar


              toolbar = NavigationToolbar2Tk(self.fig_canvas, self.plotFrame, pack_toolbar = False)
              toolbar.update()
              toolbar.pack(side = BOTTOM, fill = X)
              self.fig_canvas.get_tk_widget().pack()
                     
                     
       

# class Graph_tools does all the graphing calculations and editing graphs


class Graph_tools(App):


       # staticmetod plot_graph runs calculations to plot the equations given


       @staticmethod
       def plot_graph(fx):


              # if statements see if the graph is 2D or 3D
              # graph is 2D


              if str(app.dim_indx_btn.label)[16:18] == "2D":



                     # the method will try and do the calculations
                     # if it fails it does not plot anything

                     try:
                           
                            x, y = User_info.Get_func(fx, "2D")

                            graph = app.ax.plot(x, y, color = "r")

                            graph_list.append(graph)
                            
                            app.fig_canvas.draw()

                            # then add the equation used and the graph (value for graph is an address)

                            User_info.Add_func("2D", fx, x, y)

                            app.mylist.insert(END, f" y = {fx}")



                     except:

                            try:

                                   """How 2D plotting works:
                            ---------------------------------------------------------------------------------
                                   we get a list with 40000 elements between -25 and 25
                                   this is used as our x values

                                   list comprehension is used to iterate through our x values
                                   eval(fx) will use the string in fx as an expression 
                                   this means the iterated value of x will be substituted into the expression
                                   after this is calculated it appends the number into the new list
                            ---------------------------------------------------------------------------------
                                   """
                     

                                   x = range_x(-25, 25, 40000)


                                   y = [eval(fx) for x in x] 


                                   # then plot the values of x and y into matplotlib

                                   graph = app.ax.plot(x, y, color = "r")

                                   graph_list.append(graph)
                            
                                   app.fig_canvas.draw()

                                   # then add the equation used and the graph (value for graph is an address)

                                   User_info.Add_func("2D", fx, x, y)

                                   app.mylist.insert(END, f" y = {fx}")


                            except Exception as error:
                           
                                   print(error)


              # graph is 3D

              if str(app.dim_indx_btn.label)[16:18] == "3D":


                     # the method will try and do the calculations
                     # if it fails it does not plot anything

                     try:
                           
                            x, y, z = User_info.Get_func(fx, "3D")

                            graph = app.ax.plot(x, y, z, color = "r")

                            graph_list.append(graph)
                            
                            app.fig_canvas.draw()

                            # then add the equation used and the graph (value for graph is an address)

                            User_info.Add_func("3D", fx, x, y, z)

                            app.mylist.insert(END, f" z = {fx}")


                     except:

                            try:


                                   """How 3d plotting works:
                            ------------------------------------------------------------------------------------------------------
                                   First we get a list with 100 elements between -10,10 (100 has been chosen to maintain lag).
                                   Next we use this list to make a matrix (X) which has the size: length of list x length of list
                                   we use matrix X as the x values of our graph.

                                   After we make a new matrix (Y) which is the transposed matrix of matrix X
                                   transposing a matrix switches the row and columns of a matrix.

                                   For example:

                                   X = [1,2,3]    Y = [1,1,1]
                                       [1,2,3]        [2,2,2]
                                       [1,2,3]        [3,3,3]

                                   Finally we can get our z values by subbing in X and Y into the equation given.
                                   To do this we need to iterate through the matricies and adding the values into a new matrix (Z).

                                   For example using the function z = x + y:

                                   X = [1,2,3]    Y = [1,1,1]    Z = [2,3,4]
                                       [1,2,3]        [2,2,2]        [3,4,5]
                                       [1,2,3]        [3,3,3]        [4,5,6]

                                   Once we have the matricies X,Y,Z we can now plot our graph
                                   which uses the matplotlib plot_surface function
                            ------------------------------------------------------------------------------------------------------
                            """


                                   x = range_x(-10, 10, 100)


                                   X = ([x for i in x])


                                   Y = ([[X[j][i] for j in range(len(X))] for i in range(len(X[0]))])


                                   Z = np.array([[eval(fx) for x,y in zip(X[i],Y[i])] for i in range(len(X))])



                                   graph = app.ax.plot_surface(X,Y,Z, color = "r")
                                   app.fig_canvas.draw()


                                   User_info.Add_func("3D", fx, X, Y, Z)
                                   graph_list.append(graph)


                                   app.mylist.insert(END, f" z = {fx}")


                            except:


                                   pass


       @staticmethod             
       def delete_graph():


              # get elements from mylist that are selected in the Listbox


              is_selected = app.mylist.curselection()


              # if something is selected


              if is_selected:


                     # if using 2D plane 


                     if str(app.dim_indx_btn.label)[16:18] == "2D":


                            User_info.Del_func((app.mylist.get(is_selected[0]))[5:], "2D")


                            line = graph_list[is_selected[0]].pop()
                            line.remove()

                            graph_list.pop(is_selected[0])
                            

                            app.fig_canvas.draw()

                            app.mylist.delete(is_selected[0])


                     # if using 3D plane 


                     if str(app.dim_indx_btn.label)[16:18] == "3D":


                            # remove the graph and remove the data from the list



                            User_info.Del_func((app.mylist.get(is_selected[0]))[5:], "3D")


                            graph_list[is_selected[0]].remove()


                            graph_list.pop(is_selected[0])

                            app.fig_canvas.draw()

                            app.mylist.delete(is_selected[0])
    

       @staticmethod
       def edit_graph():


              # get elements from mylist that are selected in the Listbox


              is_selected = app.mylist.curselection()


              # if something is selected


              if is_selected:


                     # if using 2D plane 


                     if str(app.dim_indx_btn.label)[16:18] == "2D":


                            # remove graph and data
                            # push function back into the entry_stack

                            User_info.Del_func((app.mylist.get(is_selected[0]))[5:], "2D")


                            line = graph_list[is_selected[0]].pop()
                            line.remove()
                            

                            graph_list.pop(is_selected[0])

       
                            app.fig_canvas.draw()

              
                            app.plot_entry.config(state=NORMAL)
                            entry_stack.strip_push((app.mylist.get(is_selected[0]))[5:])
                            app.plot_entry.config(state=DISABLED)

                            app.mylist.delete(is_selected[0])

                     
                     # if using 3D plane 


                     if str(app.dim_indx_btn.label)[16:18] == "3D":


                            # remove graph and data
                            # push function back into the entry_stack

                     

                            User_info.Del_func((app.mylist.get(is_selected[0]))[5:], "3D")

                            graph_list[is_selected[0]].remove()

                            graph_list.pop(is_selected[0])

                                  
                            app.fig_canvas.draw()

              
                            app.plot_entry.config(state=NORMAL)
                            entry_stack.strip_push((app.mylist.get(is_selected[0]))[5:])
                            app.plot_entry.config(state=DISABLED)

                            app.mylist.delete(is_selected[0])

        


# Index class switches between the 3D and 2D plane


class Index(App):


       def __init__(self):
            

            # if using 2D plane 


            if str(app.dim_indx_btn.label)[16:18] == "2D":
                  
              
                  # switch to 3D plane
                  
                  
                  self.dim3()


            # if using 3D plane 


            elif str(app.dim_indx_btn.label)[16:18] == "3D":
                  

                  # switch to 3D plane
                  

                  self.dim2()


       def dim2(self):
            

            # remove the axes and delete all data 
            # create a new 2D axes
            

            app.fig.delaxes(app.fig.axes[1])

            app.fig.set_size_inches((8,5))
            app.ax = app.fig.add_subplot(111)
            app.fig.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
            app.ax.axvline(color="black", linestyle="--")
            app.ax.axhline(color="black", linestyle="--")
            app.ax.set_xlim(-10, 10)
            app.ax.set_ylim(-10, 10)
            app.ax.set_ylabel("Y")
            app.ax.set_xlabel("X")
            app.ax.grid()


            app.dim_indx_btn.label.set_text("2D")
            graph_list.clear()
            app.mylist.delete(0, END)
            
            for x, y, fx in User_info.Load_func("2D"):
          
              graph = app.ax.plot(x, y, color = "r")
                            

              app.mylist.insert(END, f" y = {fx}")

              User_info.Add_func("2D", fx, x, y)

              graph_list.append(graph)

            app.fig_canvas.draw()


            app.x_slider.destroy()
            app.y_slider.destroy()
            app.z_slider.destroy()


            app.slider = Scale(app.meta_dataFrame, from_=0, to=360, bg = "#5f6368", fg = "#e8eaed", troughcolor= "#5f6368", borderwidth= 3, orient= HORIZONTAL, length= 200, command=
             lambda x :dim2_rotation_matrix())
              

            app.slider.place(x=10,y=10)


       

       def dim3(self):
            

            # remove the axes and delete all data 
            # create a new 2D axes
            

            app.fig.delaxes(app.fig.axes[1])


            app.ax = app.fig.add_subplot(111, projection="3d")
            app.fig.set_figheight(8)
            app.fig.set_figwidth(8)
            app.fig.subplots_adjust(left=0, right=0.9, bottom=0, top=1.4)
            app.ax.set_xlim(-10, 10)
            app.ax.set_ylim(-10, 10)
            app.ax.set_ylabel("Y")
            app.ax.set_xlabel("X")
            app.ax.set_zlabel("Z")
            app.ax.set_xlim(-10, 10)
            app.ax.set_ylim(-10, 10)
            app.ax.set_zlim(-10, 10)


            app.dim_indx_btn.label.set_text("3D")
            graph_list.clear()
            app.mylist.delete(0, END)


            for x, y, z, fx in User_info.Load_func("3D"):
              
              z = np.array([[eval(fx) for x,y in zip(x[i],y[i])] for i in range(len(x))])
          
              graph = app.ax.plot_surface(x, y, z, color = "r")

              app.fig_canvas.draw()

              app.mylist.insert(END, f" y = {fx}")

              User_info.Add_func("3D", fx, x, y, z)

              graph_list.append(graph)


            app.fig_canvas.draw()


            app.slider.destroy()


            app.x_slider = Scale(app.meta_dataFrame, from_=0, to=360, bg = "#5f6368", fg = "#e8eaed", troughcolor= "#5f6368", borderwidth= 3, orient= HORIZONTAL, length= 200, command=
             lambda x :dim3_rotation_matrix())
              

            app.x_slider.place(x=10,y=10)


            app.y_slider = Scale(app.meta_dataFrame, from_=0, to=360, bg = "#5f6368", fg = "#e8eaed", troughcolor= "#5f6368", borderwidth= 3, orient= HORIZONTAL, length= 200, command=
             lambda x :dim3_rotation_matrix())
              

            app.y_slider.place(x=220,y=10)


            app.z_slider = Scale(app.meta_dataFrame, from_=0, to=360, bg = "#5f6368", fg = "#e8eaed", troughcolor= "#5f6368", borderwidth= 3, orient= HORIZONTAL, length= 200, command=
             lambda x :dim3_rotation_matrix())
              

            app.z_slider.place(x=430,y=10)





class entry_stack:


    stack = []

    
    dic = {"fact" : "fact",
           "sin" : "sin", "cos": "cos", 
           "tan" : "tan", "log" : "log",
           "e" : "e", "pi" : "pi",
           "x" : "x", "y" : "y",
           "(" : "(", ")" : ")", "0" : "0",
           "1" : "1", "2" : "2", "3" : "3",
           "4" : "4", "5" : "5", "6" : "6",
           "7" : "7", "8" : "8", "9" : "9",
           "." : ".", "/" : "/", "*" : "*",
           "-" : "-", "+" : "+", "^" : "**",
           "," : ","}


    def __len__(self):


        return len(self.stack)


    @staticmethod
    def push(val):
        

        entry_stack.stack.append(entry_stack.dic[val])
        app.plot_entry.insert(END, entry_stack.dic[val])


    @staticmethod
    def pop():


        if len(entry_stack.stack) > 0:
            

            app.plot_entry.delete(app.plot_entry.index("end") - len(entry_stack.stack[-1]), END)
            entry_stack.stack.pop(-1)

    @staticmethod
    def pull():
        

        if len(entry_stack.stack) > 0:
            

            app.plot_entry.delete(0, END)
            entry_stack.stack.clear()


    @staticmethod
    def strip_push(val):
          

          string = ""


          for char in val:
                

                string += char


                if string in entry_stack.dic:
                      

                      entry_stack.push(string)
                      string = ""




class dim2_rotation_matrix:


    def __init__(self):


       is_selected = app.mylist.curselection()


       if is_selected:


              fx = (app.mylist.get(is_selected[0]))[5:]

              X, Y = User_info.Get_func(fx, "2D")

              θ = (app.slider.get() * (pi/180))

              self.rot_x = [x*math.cos(θ) - y*math.sin(θ) for x, y in zip(X, Y)]
              self.rot_y = [x*math.sin(θ) + y*math.cos(θ) for x, y in zip(X, Y)]


              line = graph_list[is_selected[0]].pop()
              line.remove()

              
              graph = app.ax.plot(self.rot_x, self.rot_y, color = "r")
              graph_list[is_selected[0]] = graph

              app.fig_canvas.draw()








class dim3_rotation_matrix:
      

    def __init__(self):


       is_selected = app.mylist.curselection()


       if is_selected:


              fx = (app.mylist.get(is_selected[0]))[5:]


              x = range_x(-10, 10, 100)


              X = ([x for i in x])


              Y = ([[X[j][i] for j in range(len(X))] for i in range(len(X[0]))])


              Z = np.array([[eval(fx) for x,y in zip(X[i],Y[i])] for i in range(len(X))])


              gamma = app.z_slider.get() * (pi/180)
              beta = app.y_slider.get() * (pi/180)
              alpha = app.x_slider.get() * (pi/180)


              R = [[[math.cos(beta)*math.cos(gamma)], [math.sin(alpha)*math.sin(beta)*math.cos(gamma)-math.cos(alpha)*math.sin(gamma)], [math.cos(alpha)*math.sin(beta)*math.cos(gamma) + math.sin(alpha)*math.sin(gamma)]], 
                  [[math.cos(beta)*math.sin(gamma)], [math.sin(alpha)*math.sin(beta)*math.sin(gamma)+math.cos(alpha)*math.cos(gamma)], [math.cos(alpha)*math.sin(beta)*math.sin(gamma)-math.sin(alpha)*math.cos(gamma)]],
                  [[-math.sin(beta)],       [math.sin(alpha)*math.cos(beta)],                      [math.cos(alpha)*math.cos(beta)]]]


              rot_x = [[R[0][0][0]*x + R[0][1][0]*y + R[0][2][0]*z for x, y, z in zip(X[i], Y[i], Z[i])] for i in range(len(X))]
              rot_y = [[R[1][0][0]*x + R[1][1][0]*y + R[1][2][0]*z for x, y, z in zip(X[i], Y[i], Z[i])] for i in range(len(X))]
              rot_z = np.array([[R[2][0][0]*x + R[2][1][0]*y + R[2][2][0]*z for x, y, z in zip(X[i], Y[i], Z[i])] for i in range(len(X))])


              graph_list[is_selected[0]].remove()



              graph = app.ax.plot_surface(rot_x, rot_y, rot_z, color = "r")
              graph_list[is_selected[0]] = graph


              app.fig_canvas.draw()




if __name__ == "__main__":
    

    root = Tk()
    app = App(root)

    root.bind("<comma>", lambda x: [app.plot_entry.config(state = NORMAL), entry_stack.push(","), app.plot_entry.config(state = DISABLED)])
    root.bind("0", lambda x: [app.plot_entry.config(state = NORMAL), entry_stack.push("0"), app.plot_entry.config(state = DISABLED)])
    root.bind("1", lambda x: [app.plot_entry.config(state = NORMAL), entry_stack.push("1"), app.plot_entry.config(state = DISABLED)])
    root.bind("2", lambda x: [app.plot_entry.config(state = NORMAL), entry_stack.push("2"), app.plot_entry.config(state = DISABLED)])
    root.bind("3", lambda x: [app.plot_entry.config(state = NORMAL), entry_stack.push("3"), app.plot_entry.config(state = DISABLED)])
    root.bind("4", lambda x: [app.plot_entry.config(state = NORMAL), entry_stack.push("4"), app.plot_entry.config(state = DISABLED)])
    root.bind("5", lambda x: [app.plot_entry.config(state = NORMAL), entry_stack.push("5"), app.plot_entry.config(state = DISABLED)])
    root.bind("6", lambda x: [app.plot_entry.config(state = NORMAL), entry_stack.push("6"), app.plot_entry.config(state = DISABLED)])
    root.bind("7", lambda x: [app.plot_entry.config(state = NORMAL), entry_stack.push("7"), app.plot_entry.config(state = DISABLED)])
    root.bind("8", lambda x: [app.plot_entry.config(state = NORMAL), entry_stack.push("8"), app.plot_entry.config(state = DISABLED)])
    root.bind("9", lambda x: [app.plot_entry.config(state = NORMAL), entry_stack.push("9"), app.plot_entry.config(state = DISABLED)])
    root.bind("<BackSpace>", lambda x: [app.plot_entry.config(state = NORMAL), entry_stack.pop(), app.plot_entry.config(state=DISABLED)])
    root.bind("<period>", lambda x: [app.plot_entry.config(state = NORMAL), entry_stack.push("."), app.plot_entry.config(state = DISABLED)])
    root.bind("(", lambda x: [app.plot_entry.config(state = NORMAL), entry_stack.push("("), app.plot_entry.config(state = DISABLED)])
    root.bind(")", lambda x: [app.plot_entry.config(state = NORMAL), entry_stack.push(")"), app.plot_entry.config(state = DISABLED)])
    root.bind("!", lambda x: [app.plot_entry.config(state = NORMAL), entry_stack.push("fact"), app.plot_entry.config(state = DISABLED)])
    root.bind("x", lambda x: [app.plot_entry.config(state = NORMAL), entry_stack.push("x"), app.plot_entry.config(state = DISABLED)])
    root.bind("y", lambda x: [app.plot_entry.config(state = NORMAL), entry_stack.push("y"), app.plot_entry.config(state = DISABLED)])

    global graph_list
    graph_list = []

    for x, y, fx in User_info.Load_func("2D"):
          
       graph = app.ax.plot(x, y, color = "r")
                            
       app.fig_canvas.draw()

       app.mylist.insert(END, f" y = {fx}")

       User_info.Add_func("2D", fx, x, y)

       graph_list.append(graph)


    root.mainloop()

