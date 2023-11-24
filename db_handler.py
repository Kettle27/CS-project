import sqlite3
import re
from tkinter import *
from extension import *


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


        if cursor.fetchone() == []:


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
        
        conn = sqlite3.connect("Calculator.db")
        cursor = conn.cursor()

        statement1 = f"""SELECT x_val, y_val, function FROM GraphInfo
                        WHERE EXISTS (SELECT Username FROM Graphs
                                      WHERE Username = "{user}"
                                      AND Graphs.function = GraphInfo.function) """
        
        cursor.execute(statement1)

        data = cursor.fetchall()


        return User_info.Read_data(data)

        conn.close()


    @staticmethod
    def Add_func(object, function, x, y):

        conn = sqlite3.connect("Calculator.db")
        cursor = conn.cursor()


        statement1 = f"""INSERT INTO Graphs (Username, function, object)
                        SELECT * FROM(VALUES ("{user}","{function}","{object}"))
                        WHERE NOT EXISTS (SELECT * FROM Graphs
                                          WHERE Username = "{user}"
                                          AND function = "{function}")"""
        

        cursor.execute(statement1)
        conn.commit()


        statement2 = f"""INSERT INTO GraphInfo (function, x_val, y_val)
                            SELECT * FROM(VALUES ("{function}","{x}","{y}"))
                            WHERE NOT EXISTS (SELECT * FROM GraphInfo
                                              WHERE function = "{function}"
                                              AND x_val = "{x}")"""


        cursor.execute(statement2)
        conn.commit()
        
        conn.close()
    

    @staticmethod
    def Del_func(function):

        conn = sqlite3.connect("Calculator.db")
        cursor = conn.cursor()       

        statement1 = f"""DELETE FROM Graphs
                         WHERE Username = "{user}"
                         AND function = "{function}" """


        cursor.execute(statement1)

        conn.commit()


        conn.close()
    

    @staticmethod
    def Read_data(function):

        for i in function:

            yield [eval(i[0]),eval(i[1]), i[2]]

