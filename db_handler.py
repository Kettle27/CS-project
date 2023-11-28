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

        statement1 = f"""SELECT function FROM GraphInfo
                        WHERE EXISTS (SELECT Username FROM Graphs
                                      WHERE Username = "{user}"
                                      AND Graphs.function = GraphInfo.function) """
        

        cursor.execute(statement1)

        data = cursor.fetchall()

        for i in data:

            statement2 = f"""DELETE FROM Graphs
                         WHERE Username = "{user}"
                         AND function = "{i[0]}" """
            
            conn.execute(statement2)

            conn.commit()
        

        conn.close()

        for i in data:

            yield i[0]



    @staticmethod
    def Add_func(objectID, function, x, y):

        conn = sqlite3.connect("Calculator.db")
        cursor = conn.cursor()


        statement1 = f"""INSERT INTO Graphs (Username, function, object)
                        SELECT * FROM(VALUES ("{user}","{function}","{objectID}"))
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


        statement2 = f"""SELECT object FROM Graphs
                         WHERE Username = "{user}"
                         AND function = "{function}" """
        

        cursor.execute(statement2)

        data = cursor.fetchall()


        cursor.execute(statement1)

        conn.commit()

        conn.close()

        if data == []:

            return None
        
        else:

            return data[0][0]
        



user = "test1"

for fx in User_info.Load_func():

    print(fx)
