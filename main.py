# Computer Science Project
# Author - George Sil
# Add all needed Libraries
import re
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib import backend_bases
from matplotlib.widgets import Button as Btn
# Add my other files
from extension import *
from db_handler import *
# Configure which matplotlib tools to use
# Currently - Home, Back, Forward, Pan, Zoom
backend_bases.NavigationToolbar2.toolitems = (
    ('Home', 'Reset original view', 'home', 'home'),
    ('Back', 'Back to  previous view', 'back', 'back'),
    ('Forward', 'Forward to next view', 'forward', 'forward'),
    ('Pan', 'Pan axes with left mouse, zoom with right', 'move', 'pan'),
    ('Zoom', 'Zoom to rectangle', 'zoom_to_rect', 'zoom'))
# graph_list is used to hold all the matplotlib graph objects
# so that they can be used to delete graphs
graph_list = []
# Create validation class for logins and sign ups
class Val(Frame):
    # Tk() as parameter
    def __init__(self,master):
    	# Inheritance class
        super(Val, self).__init__(master)
        self.grid()
        # Create frames
        self.loginFrame = Frame(self)
        self.signupFrame = Frame(self)
        # Place login widgets and the frame
        self.create_login_widgets()
        self.loginFrame.grid()
    # Function plots all login widgets  
    def create_login_widgets(self):
    	# Error label is invisible until we need to use it
        self.Error_label = Label(self.loginFrame,text=" ")
        self.Error_label.grid(row=0, column=1, padx=10, pady=10)
        # Username and Password labels
        self.Username_label = Label(self.loginFrame,text="Username:").grid(row=1, column=0, padx=10, pady=10)
        self.Password_label = Label(self.loginFrame,text="Password:").grid(row=2,column=0, padx=10, pady=10)
        # Place username and password entries
        self.username_entry = Entry(self.loginFrame, width=50)
        self.username_entry.grid(row=1, column=1, columnspan=2, padx=5)
        self.password_entry = Entry(self.loginFrame,width = 50, show="*")
        self.password_entry.grid(row =2, column=1, columnspan=2,padx=5)
        # show and hide functions change the password from hidden to shown
        def show():
            # Change the button's command to hide and then show the password
            toggle_button.config(text="hide ",command=lambda:hide(),relief="groove")
            self.password_entry.config(show="")
        def hide():
            # Change the button's command to show and then hide the password
            toggle_button.config(text="show ",command=lambda:show(),relief="groove")
            self.password_entry.config(show="*")
        # Button for showing and hiding the password
        toggle_button = Button(self.loginFrame,text='show',command=lambda:show(),relief="groove")
        toggle_button.grid(row=2, column=4, padx=5)
        # Place the login and signup buttons and also the label "or"
        Button(self.loginFrame,text="Login",width=15,relief="groove",command=lambda:self.check_login_validation()).grid(row=3,column=1,padx=100)
        Label(self.loginFrame,text="or").grid(row=4,column=1,pady=10)
        Button(self.loginFrame,text="sign up",width=15,relief="groove",command=lambda:self.create_new_login()).grid(row=5, column=1, padx=5)
    # class method to check if the logins provided are correct
    def check_login_validation(self):
        # Check if the username and password is correct
        if Login.check_login(self.username_entry.get(), self.password_entry.get()):
            # Username and password is correct
            # Run the main program
            self.accept()
        # Username or password is incorrect    
        else:
            # Show error label then clear the entries
            self.Error_label.config(text="Invalid Username or Password!",relief="raised",bg="red")
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
    # removes login widgets and places the sign up widgets
    def create_new_login(self):
        # remove loginFrame Frame and place the signupFrame
        self.loginFrame.grid_remove()
        self.signupFrame.grid()
        # Change window title and size
        win.title("Sign Up")
        win.geometry("450x250")
        # Error label is invisible until we need to use it
        self.Error_label = Label(self.signupFrame,text=" ")
        self.Error_label.grid(row=0, column=1, padx=10, pady=10)
        # Place Username and Password label
        self.Username_label = Label(self.signupFrame,text="Username:").grid(row=1, column=0, padx=10, pady=10)
        self.Password_label = Label(self.signupFrame,text="Password:").grid(row=2,column=0, padx=10, pady=10)
        # Place the Username and Password entries
        self.username_entry = Entry(self.signupFrame, width=50)
        self.username_entry.grid(row=1, column=1, columnspan=2, padx=5)
        self.password_entry = Entry(self.signupFrame,width = 50, show="*")
        self.password_entry.grid(row =2, column=1, columnspan=2,padx=5)
        # show and hide functions change the password from hidden to shown
        def show():
            # Change the button's command to hide and then show the password
            toggle_button.config(text="hide ",command=lambda:hide(),relief="groove")
            self.password_entry.config(show="")
        def hide():
            # Change the button's command to show and then hide the password
            toggle_button.config(text="show ",command=lambda:show(),relief="groove")
            self.password_entry.config(show="*")
        # Button for showing and hiding the password
        toggle_button = Button(self.signupFrame,text="show",command=lambda:show(),relief="groove")
        toggle_button.grid(row=2, column=4, padx=5)
		# Label for requirements
        Label(self.signupFrame,text= """Your Username and Password has to be between 8 and 20 characters. 
        Your Username cannot contain special characters but your Password can.""").place(x=0,y=130)
        # Place the signup button
        Button(self.signupFrame,text="sign up",width=15,relief="groove",command=lambda:self.validate_new_login()).grid(row=4, column=1, padx=100, pady=65)
    # Validates the sign up details using regular expressions
    def validate_new_login(self):
        # If username and password passes the regular expressions
        if re.fullmatch("[A-Za-z0-9]{8,20}", self.username_entry.get()) and re.fullmatch("[A-Za-z0-9._%+-^$£!*&]{8,20}" , self.password_entry.get()) is not None:
            # Passed regular expression
            # Try to add the username and password to the database,
            # Check if the username doesn't already exist
            # If it doesn't exist login is accepted
            if Login.create_login(self.username_entry.get(), self.password_entry.get()):
                #remove the signupFrame Frame and grid the loginFrame Frame
                self.signupFrame.grid_remove()
                self.loginFrame.grid()
                # Place all of the login widgets. Adjust the window size and rename the title
                self.create_login_widgets()
                win.geometry("450x250")
                win.title("Login")
            # Login already exists  
            else:
                # Show error label then clear the entries
                self.Error_label.config(text="Username already exists!",relief="raised",bg="red")
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)
        # Didn't pass regular expressions
        else:
            # Show error label then clear the entries
            self.Error_label.config(text="Invalid Username or Password!",relief="raised",bg="red")
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
    # Accept state starts the new program
    def accept(self):
        # Remove the Validation window
        win.destroy()
        # Create new Tkinter object and call the App class to open the main program
        global root, app
        root = Tk()
        app = App(root)
        # Bind keyboard inputs to a function
        root.bind("<comma>", lambda x: [app.plot_entry.config(state = NORMAL), Entry_stack.push(","), app.plot_entry.config(state = DISABLED)])
        root.bind("0", lambda x: [app.plot_entry.config(state = NORMAL), Entry_stack.push("0"), app.plot_entry.config(state = DISABLED)])
        root.bind("1", lambda x: [app.plot_entry.config(state = NORMAL), Entry_stack.push("1"), app.plot_entry.config(state = DISABLED)])
        root.bind("2", lambda x: [app.plot_entry.config(state = NORMAL), Entry_stack.push("2"), app.plot_entry.config(state = DISABLED)])
        root.bind("3", lambda x: [app.plot_entry.config(state = NORMAL), Entry_stack.push("3"), app.plot_entry.config(state = DISABLED)])
        root.bind("4", lambda x: [app.plot_entry.config(state = NORMAL), Entry_stack.push("4"), app.plot_entry.config(state = DISABLED)])
        root.bind("5", lambda x: [app.plot_entry.config(state = NORMAL), Entry_stack.push("5"), app.plot_entry.config(state = DISABLED)])
        root.bind("6", lambda x: [app.plot_entry.config(state = NORMAL), Entry_stack.push("6"), app.plot_entry.config(state = DISABLED)])
        root.bind("7", lambda x: [app.plot_entry.config(state = NORMAL), Entry_stack.push("7"), app.plot_entry.config(state = DISABLED)])
        root.bind("8", lambda x: [app.plot_entry.config(state = NORMAL), Entry_stack.push("8"), app.plot_entry.config(state = DISABLED)])
        root.bind("9", lambda x: [app.plot_entry.config(state = NORMAL), Entry_stack.push("9"), app.plot_entry.config(state = DISABLED)])
        root.bind("<BackSpace>", lambda x: [app.plot_entry.config(state = NORMAL), Entry_stack.pop(), app.plot_entry.config(state=DISABLED)])
        root.bind("<period>", lambda x: [app.plot_entry.config(state = NORMAL), Entry_stack.push("."), app.plot_entry.config(state = DISABLED)])
        root.bind("(", lambda x: [app.plot_entry.config(state = NORMAL), Entry_stack.push("("), app.plot_entry.config(state = DISABLED)])
        root.bind(")", lambda x: [app.plot_entry.config(state = NORMAL), Entry_stack.push(")"), app.plot_entry.config(state = DISABLED)])
        root.bind("!", lambda x: [app.plot_entry.config(state = NORMAL), Entry_stack.push("fact"), app.plot_entry.config(state = DISABLED)])
        root.bind("x", lambda x: [app.plot_entry.config(state = NORMAL), Entry_stack.push("x"), app.plot_entry.config(state = DISABLED)])
        root.bind("y", lambda x: [app.plot_entry.config(state = NORMAL), Entry_stack.push("y"), app.plot_entry.config(state = DISABLED)])
        root.bind("<Return>", lambda x:[app.plot_entry.configure(state = NORMAL), Graph_tools.plot_graph(app.plot_entry.get()), Entry_stack.pull(), app.plot_entry.configure(state = DISABLED)])
        # Plot graphs that the user has saved
        # User_info.Load_func() accesses the database to get the x and y values associated with a function
        for x, y, fx in User_info.Load_func("2D"):
            # Plot the graph
            graph = app.ax.plot(x, y, color = "r")
            app.fig_canvas.draw()
            # Insert the function into the listbox
            app.mylist.insert(END, f" y = {fx}")
            # graph_list is a list used to store the current matplotlib objects
            # So it is easier to remove or replace them
            graph_list.append(graph)
        # Window loop
        root.mainloop()
# Class App holds the main program
class App(Frame):
    # Tk() as parameter
    def __init__(self, master):
        # Inheritance class
        super(App, self).__init__(master)
        # Grid self
        self.grid()
        # Title of program
        root.title('GraphingCalc')
        # Dimensions of the screen (in pixels)
        root.geometry("1200x700")
        # Grid the main Frame as self.main
        # Call method self.launch_main to add widgets and subframes to main Frame
        self.main = Frame(self)
        self.launch_main()
        self.main.grid()
    # Method creates subframes
    def launch_main(self):
              # Create all subframes
              # calculatorFrame holds all the calculator Tkinter buttons and a Tkinter entries
              self.calculatorFrame = Frame(self.main, width= 450, height=700, background="#3c4043")
              self.calculatorFrame.pack(side = RIGHT, fill=Y)
              # calculatorFrame2 holds the Tkinter listbox and the Tkinter Scrollbar
              # Used for displaying the current equations and helping to edit and delete equations
              self.calculatorFrame2  = Frame(self.calculatorFrame , width= 200, height = 300, background="#3c4043")
              self.calculatorFrame2.place(x=10, y=276)
              # plotFrame holds the matplotlib graph as well as a matplotlib button which calls the class Index
              self.plotFrame = Frame(self.main, width= 800, height= 500)
              self.plotFrame.pack(anchor=NW)
              # meta_dataFrame is a work in progress
              # meta_dataFrame will hold metadata on graphs (roots, y-intercepts, turning points)
              self.meta_dataFrame = Frame(self.main, width= 800, height=200, background="#3c4043")
              self.meta_dataFrame.pack(anchor=S)
              # Call dimwidgets to add all widgets to their subframe
              self.dimwidgets()
    # Method for placing widgets
    def dimwidgets(self):
        # plot_entry holds the equation for the graph
        # plot_entry is disabled so that you can only input when to press the calculator buttons
        self.plot_entry = Entry(self.calculatorFrame , bg= "#3C4043", width=17, borderwidth= 6, font= "Arial 30", state= DISABLED)
        self.plot_entry.place(x = 6, y = 11)
        # Buttons below when clicked insert a value to the entry using the Entry_stack class
        Button(self.calculatorFrame , text="sin", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("sin"), self.plot_entry.config(state = DISABLED)]
        ).place(x=5, y = 70)
        Button(self.calculatorFrame , text="cos", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("cos"), self.plot_entry.config(state = DISABLED)]
        ).place(x=5, y = 109)
        Button(self.calculatorFrame , text="tan", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("tan"), self.plot_entry.config(state = DISABLED)]
        ).place(x=5, y = 148)
        Button(self.calculatorFrame , text="x", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("x"), self.plot_entry.config(state = DISABLED)]
        ).place(x=5, y = 187)              
        Button(self.calculatorFrame , text="y", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("y"), self.plot_entry.config(state = DISABLED)]
        ).place(x=5, y = 226)
        Button(self.calculatorFrame , text="^", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("^"), self.plot_entry.config(state = DISABLED)]
        ).place(x=70, y = 70)
        Button(self.calculatorFrame , text="!", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("fact"), self.plot_entry.config(state = DISABLED)]
        ).place(x=70, y = 109)
        Button(self.calculatorFrame , text="log", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("log"), self.plot_entry.config(state = DISABLED)]
        ).place(x=70, y = 148)
        Button(self.calculatorFrame , text="e", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("e"), self.plot_entry.config(state = DISABLED)]
        ).place(x=70, y = 187)
        Button(self.calculatorFrame , text="π", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("pi"), self.plot_entry.config(state = DISABLED)]
        ).place(x=70, y = 226)
        Button(self.calculatorFrame , text="(", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("("), self.plot_entry.config(state = DISABLED)]
        ).place(x=135, y = 70)
        Button(self.calculatorFrame , text="1", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("1"), self.plot_entry.config(state = DISABLED)]
        ).place(x=135, y = 109)
        Button(self.calculatorFrame , text="4", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("4"), self.plot_entry.config(state = DISABLED)]
        ).place(x=135, y = 148)
        Button(self.calculatorFrame , text="7", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("7"), self.plot_entry.config(state = DISABLED)]
        ).place(x=135, y = 187)
        Button(self.calculatorFrame , text="0", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("0"), self.plot_entry.config(state = DISABLED)]
        ).place(x=135, y = 226)
        Button(self.calculatorFrame , text=")", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push(")"), self.plot_entry.config(state = DISABLED)]
        ).place(x=200, y = 70)
        Button(self.calculatorFrame , text="2", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("2"), self.plot_entry.config(state = DISABLED)]
        ).place(x=200, y = 109)
        Button(self.calculatorFrame , text="5", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("5"), self.plot_entry.config(state = DISABLED)]
        ).place(x=200, y = 148)
        Button(self.calculatorFrame , text="8", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("8"), self.plot_entry.config(state = DISABLED)]
        ).place(x=200, y = 187)
        Button(self.calculatorFrame , text=".", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("."), self.plot_entry.config(state = DISABLED)]
        ).place(x=200, y = 226)
        # Button below deletes the end string if there is one
        Button(self.calculatorFrame , text="Delete", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL), Entry_stack.pop(), self.plot_entry.config(state = DISABLED)]
        ).place(x=265, y = 70)
        Button(self.calculatorFrame , text="3", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("3"), self.plot_entry.config(state = DISABLED)]
        ).place(x=265, y = 109)
        Button(self.calculatorFrame , text="6", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("6"), self.plot_entry.config(state = DISABLED)]
        ).place(x=265, y = 148)
        Button(self.calculatorFrame , text="9", width= 5, font = "Arial 15", bg = "#3c4043", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("9"), self.plot_entry.config(state = DISABLED)]
        ).place(x=265, y = 187)
        # Button below plots the equation held in plot_entry and calls the staticmethod plot_graph from the class Graph_tools
        # Button also clears plot_entry
        Button(self.calculatorFrame , text = "Plot", width = 5, font = "Arial 15", bg = "#8ab4f8", fg = "#202124", command=
        lambda:[self.plot_entry.config(state = NORMAL), Graph_tools.plot_graph(self.plot_entry.get()), Entry_stack.pull(), self.plot_entry.config(state = DISABLED)]
        ).place(x = 265, y = 226)
        # Button below clears plot_entry
        Button(self.calculatorFrame , text="Clear", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL), Entry_stack.pull(), self.plot_entry.config(state = DISABLED)]
        ).place(x=330, y = 70)
        Button(self.calculatorFrame , text="÷", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("/"), self.plot_entry.config(state = DISABLED)]
        ).place(x=330, y = 109)
        Button(self.calculatorFrame , text="*", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("*"), self.plot_entry.config(state = DISABLED)]
        ).place(x=330, y = 148)
        Button(self.calculatorFrame , text="-", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("-"), self.plot_entry.config(state = DISABLED)]
        ).place(x=330, y = 187)
        Button(self.calculatorFrame , text="+", width= 5, font = "Arial 15", bg = "#5f6368", fg = "#e8eaed", command=
        lambda: [self.plot_entry.config(state = NORMAL) , Entry_stack.push("+"), self.plot_entry.config(state = DISABLED)]
        ).place(x=330, y = 226)
        # Button below allows the user to edit a graph that is selected in the Tkinter Listbox
        # Button calls staticmethod edit_graph from the class Graph_tools
        Button(self.calculatorFrame , text="edit", width = 15, font = "Arial 16", bg = "#5f6368", fg = "#e8eaed", borderwidth= 3, command=
        lambda:Graph_tools.edit_graph()
        ).place(x=10, y=461)
        # Button below allows the user to delete a graph that is selected in the Tkinter Listbox
        # Button calls staticmethod delete_graph from the class Graph_tools
        Button(self.calculatorFrame , text="delete",width = 15, font = "Arial 16", bg = "#5f6368", fg = "#e8eaed", borderwidth= 3, command=
        lambda:Graph_tools.delete_graph()
        ).place(x=203, y=461)
        # Below is a Tkinter slider and label which represents the theta value of when we want to rotate a graph
        self.slider_label = Label(self.meta_dataFrame, text = "x_axis", font= "Arial 15", bg = "#e8eaed")
        self.slider_label.place(x=80,y=10)
        self.slider = Scale(self.meta_dataFrame, from_=0, to=360, bg = "#5f6368", fg = "#e8eaed", troughcolor= "#5f6368", borderwidth= 3, orient= HORIZONTAL, length= 200, command=
        lambda x :dim2_rotation_matrix())
        self.slider.place(x=10,y=50)
        # Added Tkinter Scrollbar to scroll on the Listbox if needed
        # Tkinter Scrollbar is attacted to the entire right side of the Listbox
        self.scrollbar = Scrollbar(self.calculatorFrame2 , width = 20)
        self.scrollbar.pack( side = RIGHT, fill=Y )
        # Create Tkinter Listbox in calculatorFrame2 subframe
        # Allow the scrollbar to scroll the listbox if needed
        # Config Listbox command after Listbox is created because command calls itself
        self.mylist = Listbox(self.calculatorFrame2 , yscrollcommand= self.scrollbar.set, width= 50, font = "Arial 10", borderwidth= 6)
        self.mylist.pack(side = LEFT, fill = BOTH )
        self.scrollbar.config(command = self.mylist.yview )
        # Create matplotlib Figure
        self.fig = Figure(figsize = (8, 5), dpi = 100)
        # Create matplotlib button to call class Index which changes dimention of graph
        self.dim_indx = self.fig.add_axes([0.9, 0.9, 0.09, 0.075])
        self.dim_indx_btn = Btn(self.dim_indx, "2D")
        self.dim_indx_btn.on_clicked(lambda x: Index())
        # Create the subplot for which we are graphing
        self.ax = self.fig.add_subplot(111)
        # axvline and axhline creates lines which cross x = 0 and y = 0
        self.ax.axvline(color="black", linestyle="--")
        self.ax.axhline(color="black", linestyle="--")
        # Set x and y axis limit to -10 and 10
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        # Label x and y axis
        self.ax.set_ylabel("Y")
        self.ax.set_xlabel("X")
        # Create grid on graph
        self.ax.grid()
        # Backend the matplotlib figure to the tkinter subframe
        # Draw graph
        self.fig_canvas = FigureCanvasTkAgg(self.fig, master = self.plotFrame)
        self.fig_canvas.draw()
        self.fig_canvas.get_tk_widget().pack()
        # Add built-in matplotlib toolbar
        toolbar = NavigationToolbar2Tk(self.fig_canvas, self.plotFrame, pack_toolbar = False)
        toolbar.update()
        toolbar.pack(side = BOTTOM, fill = X)
        self.fig_canvas.get_tk_widget().pack()
# Class Graph_tools does all the graphing calculations and editing graphs
class Graph_tools(App):
    # Staticmetod plot_graph runs calculations to plot the equations given
    @staticmethod
    def plot_graph(fx):
        # If current graph is 2D
        if str(app.dim_indx_btn.label)[16:18] == "2D":
            # Checks the database to see if the function has already been done before
            try:
                # Checks the database to see if the function has already been done before
                # If it has then it takes the x and y values and plots them
                # Adds the matplotlib object to graph_list        
                x, y = User_info.Get_func(fx, "2D")
                graph = app.ax.plot(x, y, color = "r")
                graph_list.append(graph)          
                app.fig_canvas.draw()
                # Then add the equation to the database under the user
                # Its deleted when first loaded to delete repeating graphs
                User_info.Add_func("2D", fx, x, y)
                # Add the function to the listbox
                app.mylist.insert(END, f" y = {fx}")
            # Not in database
            except:
                # The method will try and do the calculations
                # If it fails it does not plot anything
                try:
                    """                
                    How 2D plotting works:
                ---------------------------------------------------------------------------------
                    we get a list with 40000 elements between -25 and 25
                    this is used as our x values
                    list comprehension is used to iterate through our x values
                    catch(fx, x) will calculate y using eval(fx) but if it returns an error like
                    ZeroDivisionError it returns a Null type.
                    Once y is calculated it is plotted.
                ---------------------------------------------------------------------------------
                    """
                    def catch(fx, x):
                        try:
                            return eval(fx)
                        except ZeroDivisionError:
                            return np.nan
                    x = range_x(-25, 25, 40000)
                    y = [catch(fx, x) for x in x]
                    # We use these values and plot them
                    # Then add the matplotlib object of the graph to graph_list
                    graph = app.ax.plot(x, y, color = "r")
                    graph_list.append(graph)
                    app.fig_canvas.draw()
                    # Then add the equation to the database under the user
                    # Its deleted when first loaded to delete repeating graphs
                    User_info.Add_func("2D", fx, x, y)
                    # Add the function to the listbox
                    app.mylist.insert(END, f" y = {fx}")
                # Prints the error that occurred
                except Exception as error:
                    print(error)
        # Graph is 3D
        else:
            # Checks the database to see if the function has already been done before
            try:
                # Even if the database has the info the z value is corrupted because of numpy
                # So it must be calculated again            
                X, Y, fx = User_info.Get_func(fx, "3D")
                Z = np.array([[eval(fx) for x,y in zip(X[i],Y[i])] for i in range(len(X))])
                # Plots the values
                # And adds the matplotlib object of the graph to graph_list
                graph = app.ax.plot(X, Y, Z, color = "r")
                graph_list.append(graph)
                app.fig_canvas.draw()
                # Then add the equation to the database under the user
                # Its deleted when first loaded to delete repeating graphs
                User_info.Add_func("3D", fx, X, Y, Z)
                # Add the function to the listbox
                app.mylist.insert(END, f" z = {fx}")
            # Not in database
            except:
                # The method will try and do the calculations
                # If it fails it does not plot anything
                try:
                    """
                    How 3d plotting works:
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
                    To do this we need to iterate through the matrices and add the values into a new matrix (Z).
                    For example using the function z = x + y:
                    X = [1,2,3]    Y = [1,1,1]    Z = [2,3,4]
                        [1,2,3]        [2,2,2]        [3,4,5]
                        [1,2,3]        [3,3,3]        [4,5,6]
                    Once we have the matrices X,Y,Z we can now plot our graph
                    which uses the matplotlib plot_surface function
                ------------------------------------------------------------------------------------------------------
                    """
                    x = range_x(-10, 10, 100)
                    X = ([x for i in x])
                    Y = ([[X[j][i] for j in range(len(X))] for i in range(len(X[0]))])
                    Z = np.array([[eval(fx) for x,y in zip(X[i],Y[i])] for i in range(len(X))])
                    # We use these values and plot them
                    # Then add the matplotlib object of the graph to graph_list
                    graph = app.ax.plot_surface(X,Y,Z, color = "r")
                    app.fig_canvas.draw()
                    graph_list.append(graph)
                    # Then add the equation to the database under the user
                    # Its deleted when first loaded to delete repeating graphs
                    User_info.Add_func("3D", fx, X, Y, Z)
                    # Add the function to the listbox
                    app.mylist.insert(END, f" z = {fx}")
                # Prints the error that occurred
                except Exception as error:
                    print(error)
    # Staticmethod deletes graphs                          
    @staticmethod            
    def delete_graph():
        # If a graph is selected
        is_selected = app.mylist.curselection()
        if is_selected:
            # If current graph is 2D
            if str(app.dim_indx_btn.label)[16:18] == "2D":
                # Deletes the function from the database then removes it from the plot
                User_info.Del_func((app.mylist.get(is_selected[0]))[5:], "2D")
                line = graph_list[is_selected[0]].pop()
                line.remove()
                app.fig_canvas.draw()
                # Removes the matplotlib object from graph_list and the function from the listbox
                graph_list.pop(is_selected[0])
                app.mylist.delete(is_selected[0])
            # Graph is 3D
            else:
                # Deletes the function from the database then removes it from the plot
                User_info.Del_func((app.mylist.get(is_selected[0]))[5:], "3D")
                graph_list[is_selected[0]].remove()
                app.fig_canvas.draw()
                # Removes the matplotlib object from graph_list and the function from the listbox
                graph_list.pop(is_selected[0])
                app.mylist.delete(is_selected[0])
    # Staticmethod removes graph but places the function string back into the entry
    @staticmethod
    def edit_graph():
        # If a graph is selected
        is_selected = app.mylist.curselection()
        if is_selected:
            # If current graph is 2D
            if str(app.dim_indx_btn.label)[16:18] == "2D":
                # Deletes the function from the database then removes it from the plot
                User_info.Del_func((app.mylist.get(is_selected[0]))[5:], "2D")
                line = graph_list[is_selected[0]].pop()
                line.remove()
                app.fig_canvas.draw()
                # Removes the matplotlib object from graph_list then takes the function string and pushes it through strip_push
                # strip push breaks down the string and puts it in the stack then into the entry
                graph_list.pop(is_selected[0])
                app.plot_entry.config(state=NORMAL)
                Entry_stack.strip_push((app.mylist.get(is_selected[0]))[5:])
                app.plot_entry.config(state=DISABLED)
                # Deletes function from listbox
                app.mylist.delete(is_selected[0])
            # Current graph is 3D
            else:
                # Deletes the function from the database then removes it from the plot
                User_info.Del_func((app.mylist.get(is_selected[0]))[5:], "3D")
                graph_list[is_selected[0]].remove()
                app.fig_canvas.draw()
                # Removes the matplotlib object from graph_list then takes the function string and pushes it through strip_push
                # strip push breaks down the string and puts it in the stack then into the entry
                graph_list.pop(is_selected[0])
                app.plot_entry.config(state=NORMAL)
                Entry_stack.strip_push((app.mylist.get(is_selected[0]))[5:])
                app.plot_entry.config(state=DISABLED)
                # Deletes function from listbox
                app.mylist.delete(is_selected[0])
# Index class switches between the 3D and 2D graphs
class Index(App):
    def __init__(self):
        # If current graph is 2D
        if str(app.dim_indx_btn.label)[16:18] == "2D":
            # Switch to 3D graph
                self.dim3()
        # Current graph is 3D
        else:
            # Switch to 2D graph
            self.dim2()
    # Change to 2D
    def dim2(self):
        # Remove the axes and delete all data
        # Create a new 2D axes
        app.fig.delaxes(app.fig.axes[1])
        graph_list.clear()
        app.mylist.delete(0, END)
        app.fig.set_size_inches((8,5))
        app.ax = app.fig.add_subplot(111)
        app.fig.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
        # Draws line on x = 0 and y = 0
        app.ax.axvline(color="black", linestyle="--")
        app.ax.axhline(color="black", linestyle="--")
        # Sets x and y limits to -10 to 10
        # Labels x and y axis
        app.ax.set_xlim(-10, 10)
        app.ax.set_ylim(-10, 10)
        app.ax.set_ylabel("Y")
        app.ax.set_xlabel("X")
        # grid() adds a grid onto the plot
        app.ax.grid()
        # Change label to 2D
        app.dim_indx_btn.label.set_text("2D")
        # Load Users data for 2D graphs    
        for x, y, fx in User_info.Load_func("2D"):
            # plots values
            # Inserts function into listbox
            # Adds matplotlib object to graph_list
            graph = app.ax.plot(x, y, color = "r")                
            app.mylist.insert(END, f" y = {fx}")
            graph_list.append(graph)
        app.fig_canvas.draw()
        # Delete 3D sliders
        app.x_slider.destroy()
        app.y_slider.destroy()
        app.z_slider.destroy()
        app.slider_labelx.destroy()
        app.slider_labely.destroy()
        app.slider_labelz.destroy()
        # Place slider and label
        app.slider_label = Label(app.meta_dataFrame, text = "x_axis", font= "Arial 15", bg = "#e8eaed")
        app.slider_label.place(x=80,y=10)
        app.slider = Scale(app.meta_dataFrame, from_=0, to=360, bg = "#5f6368", fg = "#e8eaed", troughcolor= "#5f6368", borderwidth= 3, orient= HORIZONTAL, length= 200, command=
        lambda x :dim2_rotation_matrix())
        app.slider.place(x=10,y=50)
    # Change to 3D
    def dim3(self):
        # Remove the axes and delete all data
        # Create a new 3D axes
        app.fig.delaxes(app.fig.axes[1])
        graph_list.clear()
        app.mylist.delete(0, END)
        app.ax = app.fig.add_subplot(111, projection="3d")
        app.fig.set_figheight(8)
        app.fig.set_figwidth(8)
        app.fig.subplots_adjust(left=0, right=0.9, bottom=0, top=1.4)
        # Sets x, y and z limits to -10 to 10
        # Labels x, y and z axis
        app.ax.set_ylabel("Y")
        app.ax.set_xlabel("X")
        app.ax.set_zlabel("Z")
        app.ax.set_xlim(-10, 10)
        app.ax.set_ylim(-10, 10)
        app.ax.set_zlim(-10, 10)
        # Change label to 2D
        app.dim_indx_btn.label.set_text("3D")
        # Load Users data for 3D graphs
        for x, y, fx in User_info.Load_func("3D"):
            # Even if the database has the info the z value is corrupted because of numpy
            # So it must be calculated again
            z = np.array([[eval(fx) for x,y in zip(x[i],y[i])] for i in range(len(x))])
            # Plots the graph and insert the function into the listbox
            graph = app.ax.plot_surface(x, y, z, color = "r")
            app.fig_canvas.draw()
            app.mylist.insert(END, f" y = {fx}")
            # Add the matplotlib object to graph_list
            graph_list.append(graph)
        app.fig_canvas.draw()
        # Destroy slider and label
        app.slider.destroy()
        app.slider_label.destroy()
        # Place 3 new sliders and labels for the combined 3D rotating
        app.slider_labelx = Label(app.meta_dataFrame, text = "x_axis", font= "Arial 15", bg = "#e8eaed")
        app.slider_labelx.place(x=80,y=10)
        app.slider_labely = Label(app.meta_dataFrame, text = "y_axis", font= "Arial 15", bg = "#e8eaed")
        app.slider_labely.place(x=300,y=10)
        app.slider_labelz = Label(app.meta_dataFrame, text = "z_axis", font= "Arial 15", bg = "#e8eaed")
        app.slider_labelz.place(x=510,y=10)
        app.x_slider = Scale(app.meta_dataFrame, from_=0, to=360, bg = "#5f6368", fg = "#e8eaed", troughcolor= "#5f6368", borderwidth= 3, orient= HORIZONTAL, length= 200, command=
        lambda x :dim3_rotation_matrix())
        app.x_slider.place(x=10,y=50)
        app.y_slider = Scale(app.meta_dataFrame, from_=0, to=360, bg = "#5f6368", fg = "#e8eaed", troughcolor= "#5f6368", borderwidth= 3, orient= HORIZONTAL, length= 200, command=
        lambda x :dim3_rotation_matrix())
        app.y_slider.place(x=220,y=50)
        app.z_slider = Scale(app.meta_dataFrame, from_=0, to=360, bg = "#5f6368", fg = "#e8eaed", troughcolor= "#5f6368", borderwidth= 3, orient= HORIZONTAL, length= 200, command=
        lambda x :dim3_rotation_matrix())
        app.z_slider.place(x=430,y=50)
class Entry_stack:
    """
    Entry_stack is a class to help enforce that the Tkinter entry for the calculator stays secure and error proof.\n
    Inside Entry_stack is an array which we use as a stack and a dictionary which is used to correctly format a string
    and used to break down strings to be put into the stack
    """
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
    # When len(Entry_stack.stack) is called it returns the length
    def __len__(self):
        return len(self.stack)
    # Staticmethod push adds a value to the top of stack
    @staticmethod
    def push(val):
        # Adds the dictionary version of the value to the stack
        # Adds the value to the entry
        Entry_stack.stack.append(Entry_stack.dic[val])
        app.plot_entry.insert(END, Entry_stack.dic[val])
    # Staticmethod pop removes from the top of the stack
    @staticmethod
    def pop():
        # If the stack is not empty
        if len(Entry_stack.stack) > 0:
            # Deletes from the entry
            # Removes from the stack
            app.plot_entry.delete(app.plot_entry.index("end") - len(Entry_stack.stack[-1]), END)
            Entry_stack.stack.pop(-1)
    # Staticmethod clears the stack
    @staticmethod
    def pull():
        # If the stack is not empty
        if len(Entry_stack.stack) > 0:
            # Clears the entry
            # Clears the stack
            app.plot_entry.delete(0, END)
            Entry_stack.stack.clear()
    # Takes a string and breaks it down to be put into the stack
    @staticmethod
    def strip_push(val, string = ""):
        # Iterate through the string  
        for char in val:
            # Adds one letter from the string until it is recognised in the dictionary    
            string += char
            # If the string is in the dictionary
            if string in Entry_stack.dic:
                # Push the string to the stack
                # clear the string    
                Entry_stack.push(string)
                string = ""
# Calculating 2D rotation
class dim2_rotation_matrix:
    # __init__ method
    def __init__(self):
        # If graph is selected
        is_selected = app.mylist.curselection()
        if is_selected:
            # Use the function to get the x and y values from the database
            fx = (app.mylist.get(is_selected[0]))[5:]
            X, Y = User_info.Get_func(fx, "2D")
            # Get the angle of rotation from the slider
            θ = (app.slider.get() * (pi/180))
            # Using list comprehension we iterate through both X and Y
            # And sub x and y into the 2D rotation matrix
            self.rot_x = [x*math.cos(θ) - y*math.sin(θ) for x, y in zip(X, Y)]
            self.rot_y = [x*math.sin(θ) + y*math.cos(θ) for x, y in zip(X, Y)]
            # Delete the graph
            line = graph_list[is_selected[0]].pop()
            line.remove()
            # Plot the new rotated graph and replace the matplotlib object  
            graph = app.ax.plot(self.rot_x, self.rot_y, color = "r")
            graph_list[is_selected[0]] = graph
            app.fig_canvas.draw()
# Calculating 3D rotation
class dim3_rotation_matrix:
    # __init__ method
    def __init__(self):
        # If graph is selected
        is_selected = app.mylist.curselection()
        if is_selected:
            # Even if the database has the info the z value is corrupted because of numpy
            # So it must be calculated again  
            fx = (app.mylist.get(is_selected[0]))[5:]
            X, Y = User_info.Get_func(fx, "3D")
            Z = np.array([[eval(fx) for x,y in zip(X[i],Y[i])] for i in range(len(X))])
            # Get all 3 angles
            # Gamma is for the z-axis, Beta for the y-axis and Alpha for the x-axis
            gamma = app.z_slider.get() * (pi/180)
            beta = app.y_slider.get() * (pi/180)
            alpha = app.x_slider.get() * (pi/180)
            # Substitute our new values into the combined 3D rotation matrix
            R = [[[math.cos(beta)*math.cos(gamma)],[math.sin(alpha)*math.sin(beta)*math.cos(gamma)-math.cos(alpha)*math.sin(gamma)],[math.cos(alpha)*math.sin(beta)*math.cos(gamma) + math.sin(alpha)*math.sin(gamma)]],
                [[math.cos(beta)*math.sin(gamma)], [math.sin(alpha)*math.sin(beta)*math.sin(gamma)+math.cos(alpha)*math.cos(gamma)],[math.cos(alpha)*math.sin(beta)*math.sin(gamma)-math.sin(alpha)*math.cos(gamma)]],
                [[-math.sin(beta)],                [math.sin(alpha)*math.cos(beta)],                                                [math.cos(alpha)*math.cos(beta)]]]
            # Get our new rotated values by iterating through X, Y and Z and combining it with the matrix
            rot_x = [[R[0][0][0]*x + R[0][1][0]*y + R[0][2][0]*z for x, y, z in zip(X[i], Y[i], Z[i])] for i in range(len(X))]
            rot_y = [[R[1][0][0]*x + R[1][1][0]*y + R[1][2][0]*z for x, y, z in zip(X[i], Y[i], Z[i])] for i in range(len(X))]
            rot_z = np.array([[R[2][0][0]*x + R[2][1][0]*y + R[2][2][0]*z for x, y, z in zip(X[i], Y[i], Z[i])] for i in range(len(X))])
            # Remove graph
            graph_list[is_selected[0]].remove()
            # Plot new rotated graph
            # replace the matplotlib object with the new one
            graph = app.ax.plot_surface(rot_x, rot_y, rot_z, color = "r")
            graph_list[is_selected[0]] = graph
            app.fig_canvas.draw()
# If this is the file being executed
if __name__ == "__main__":
    # Create new tkinter object
    win = Tk()
    # Make the window appear at (300,300) on the screen
    # Make the title "Login"
    win.geometry("450x250+300+300")
    win.title("Login")
    # Call the class to make a login
    val = Val(win)
    win.mainloop()
