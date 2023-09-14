from tkinter import *
import sqlite3
import re
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.grid()


        self.loginFrame = Frame(self)
        self.graphingFrame = Frame(self)
        self.signupFrame = Frame(self)


        self.create_login_widgets()
        self.loginFrame.grid()


    def create_login_widgets(self):


        self.Error_label = Label(self.loginFrame,text=" ")
        self.Error_label.grid(row=0, column=1, padx=10, pady=10)


        self.Username_label = Label(self.loginFrame,text="Username:").grid(row=1, column=0, padx=10, pady=10)
        self.Password_label = Label(self.loginFrame,text="Password:").grid(row=2,column=0, padx=10, pady=10)




        self.username_entry = Entry(self.loginFrame, width=50)
        self.username_entry.grid(row=1, column=1, columnspan=2, padx=5)


        self.password_entry = Entry(self.loginFrame,width = 50, show="*")
        self.password_entry.grid(row =2, column=1, columnspan=2,padx=5)




        def show():


            toggle_button.config(text="hide ",command=lambda:hide(),relief="groove")
            self.password_entry.config(show="")
        def hide():


            toggle_button.config(text="show ",command=lambda:show(),relief="groove")
            self.password_entry.config(show="*")
   
        toggle_button = Button(self.loginFrame,text='show',command=lambda:show(),relief="groove")
        toggle_button.grid(row=2, column=4, padx=5)




        login_button = Button(self.loginFrame,text="          Login          ",relief="groove",command=lambda:check_login_validation()).grid(row=3,column=1,padx=100)
        or_label = Label(self.loginFrame,text="or").grid(row=4,column=1,pady=10)
        signup_button = Button(self.loginFrame,text='        sign up         ',relief="groove",command=lambda:self.create_new_login()).grid(row=5, column=1, padx=5)


        def check_login_validation():
            try:
                conn = sqlite3.connect("logins.db")
                cursor = conn.cursor()




                statement = f"""SELECT * FROM login
                                WHERE Username = "{self.username_entry.get()}" AND Password = "{self.password_entry.get()}" """
                cursor.execute(statement)


                if cursor.fetchall() == []:
                    self.Error_label.config(text="Invalid Username or Password!",relief="raised",bg="red")
                    self.username_entry.delete(0, END)
                    self.password_entry.delete(0, END)
               
                else:
                    self.Error_label.config(text=f"Welcome back {self.username_entry.get()}",relief="raised",bg="green")
                    self.username_entry.delete(0, END)
                    self.password_entry.delete(0, END)
                    self.loginFrame.grid_remove()
                    self.graphingFrame.grid()
                    self.create_calculator_widgets()
               


            except sqlite3.Error as err:
                print("An error occured", err)
            conn.close()
       
    def create_new_login(self):
        self.loginFrame.grid_remove()
        self.signupFrame.grid()


        root.title("Sign Up")
        root.geometry("450x200")




        self.Error_label = Label(self.signupFrame,text=" ")
        self.Error_label.grid(row=0, column=1, padx=10, pady=10)


        self.Username_label = Label(self.signupFrame,text="Username:").grid(row=1, column=0, padx=10, pady=10)
        self.Password_label = Label(self.signupFrame,text="Password:").grid(row=2,column=0, padx=10, pady=10)




        self.username_entry = Entry(self.signupFrame, width=50)
        self.username_entry.grid(row=1, column=1, columnspan=2, padx=5)


        self.password_entry = Entry(self.signupFrame,width = 50, show="*")
        self.password_entry.grid(row =2, column=1, columnspan=2,padx=5)


        def show():


            toggle_button.config(text="hide ",command=lambda:hide(),relief="groove")
            self.password_entry.config(show="")


        def hide():


            toggle_button.config(text="show ",command=lambda:show(),relief="groove")
            self.password_entry.config(show="*")
   
        toggle_button = Button(self.signupFrame,text='show',command=lambda:show(),relief="groove")
        toggle_button.grid(row=2, column=4, padx=5)
           
        signup_button = Button(self.signupFrame,text='          sign up         ',relief="groove",command=lambda:validate_new_login()).grid(row=3, column=1, padx=100, pady=15)


        def validate_new_login():
            if re.fullmatch("[A-Za-z0-9]{8,}", self.username_entry.get()) and re.fullmatch("[A-Za-z0-9._%+-^$£!*&]{8,}", self.username_entry.get()) is not None:
                try:
                    conn = sqlite3.connect("logins.db")
                    cursor = conn.cursor()


                    statement = f"""SELECT * FROM login
                                WHERE Username = "{self.username_entry.get()}" """
                    cursor.execute(statement)


                    if cursor.fetchall() == []:
                        statement = f"""INSERT INTO login (Username, Password)
                                VALUES ("{self.username_entry.get()}","{self.password_entry.get()}")"""
                        cursor.execute(statement)
                        conn.commit()
                        self.signupFrame.grid_remove()
                        self.loginFrame.grid()
                        self.create_login_widgets()
                        root.geometry("450x250")
                        root.title("Login")
                   
                    else:
                        self.Error_label.config(text="Username already exists!",relief="raised",bg="red")
                        self.username_entry.delete(0, END)
                        self.password_entry.delete(0, END)


 
                except sqlite3.Error as err:
                    print("An error occured", err)
                conn.close()

            else:
                self.Error_label.config(text="Invalid Username or Password!",relief="raised",bg="red")
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)






    def create_calculator_widgets(self):
        root.geometry("1200x700")
        root.title("GraphingCalc.exe")








if __name__ == "__main__":
    root = Tk()
    root.geometry("450x250")
    root.title("Login")
    app = App(root)
    root.mainloop()
