import sqlite3
import re
from tkinter import *


class Login:


    @staticmethod
    def check_login(Username, Password):


        conn = sqlite3.connect("Calculator.db")
        cursor = conn.cursor()


        statement = f"""SELECT * FROM Logins
                    WHERE Username = "{Username}" AND Password = "{Password}" """
        


        cursor.execute(statement)


        if cursor.fetchall() == []:    

            return False


        else:

            global user
            user = Username

            return True
    

    @staticmethod
    def create_login(Username, Password):


        conn = sqlite3.connect("Calculator.db")
        cursor = conn.cursor()


        statement = f"""SELECT * FROM Logins
                    WHERE Username = "{Username}"; """
        

        cursor.execute(statement)


        if cursor.fetchall() == []:


            statement = f"""INSERT INTO Logins (Username, Password)
                        VALUES ("{Username}","{Password}");"""
            cursor.execute(statement)
            conn.commit()

            conn.close()


        else:
                
            conn.close()

            return True

        

class User_info:

    
    @staticmethod
    def Load_func():
        
        pass


    @staticmethod
    def Add_func(function, x, y):

        conn = sqlite3.connect("Calculator.db")
        cursor = conn.cursor()


        statement = f"""INSERT INTO Graphs (Username, function)
                    VALUES ("{user}","{function}");"""
        

        cursor.execute(statement)
        conn.commit()

        for i in range(2001):


            statement = f"""INSERT INTO GraphInfo (function, x_val, y_val)
                        VALUES ("{function}","{x[i]}","{y[i]}");"""


            cursor.execute(statement)
            conn.commit()
        
        conn.close()
    

    @staticmethod
    def Del_func(function):

        pass
