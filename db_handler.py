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
                
            return True
        

        conn.close()
