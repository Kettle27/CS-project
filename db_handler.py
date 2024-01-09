import sqlite3
import re
from tkinter import *
from extension import *

conn = sqlite3.connect("Calculator.db")
cursor = conn.cursor()  

class Login:


    @staticmethod
    def check_login(Username, Password):


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



        statement = f"""SELECT * FROM Logins
                    WHERE Username = "{Username}"; """
        

        cursor.execute(statement)


        if cursor.fetchall() == []:


            statement = f"""INSERT INTO Logins (Username, Password)
                        VALUES ("{Username}","{Password}");"""
            cursor.execute(statement)
            conn.commit()

            return True



        else:
                

            return False

        

class User_info:

    
    @staticmethod
    def Load_func(dim):
        
        if dim == "2D":

            statement1 = f"""SELECT x_val, y_val, function FROM GraphInfo
                             WHERE EXISTS (SELECT Username FROM Graphs
                                           WHERE Username = "{user}"
                                           AND Graphs.function = GraphInfo.function
                                           AND dim = "{dim}"
                                           AND z_val IS NULL) """
        

            cursor.execute(statement1)

            data = cursor.fetchall()

            for i in data:

                statement2 = f"""DELETE FROM Graphs
                         WHERE Username = "{user}"
                         AND function = "{i[2]}" """
            
                conn.execute(statement2)

                conn.commit()
    

            for i in data:

                nan = np.nan

                yield [eval(i[0]), eval(i[1]), i[2]]


        else:

            statement2 = f"""SELECT x_val, y_val, z_val, function FROM GraphInfo
                             WHERE EXISTS (SELECT Username FROM Graphs
                                           WHERE Username = "{user}"
                                           AND Graphs.function = GraphInfo.function
                                           AND dim = "{dim}")
                                           AND z_val IS NOT NULL """
            

            cursor.execute(statement2)

            data = cursor.fetchall()


            for i in data:

                statement2 = f"""DELETE FROM Graphs
                         WHERE Username = "{user}"
                         AND function = "{i[3]}" """
            
                conn.execute(statement2)

                conn.commit()


            for i in data:

                yield [eval(i[0]), eval(i[1]), i[2], i[3]]




    @staticmethod
    def Add_func(dim, function, x, y, z = None):

        statement1 = f"""INSERT INTO Graphs (Username, function, dim)
                         SELECT * FROM(VALUES ("{user}","{function}","{dim}"))
                         WHERE NOT EXISTS (SELECT * FROM Graphs
                                          WHERE Username = "{user}"
                                          AND function = "{function}"
                                          AND dim = "{dim}")"""
        

        cursor.execute(statement1)
        conn.commit()

        if dim == "2D":

            statement2 = f"""INSERT INTO GraphInfo (function, x_val, y_val)
                             SELECT * FROM(VALUES ("{function}","{x}","{y}"))
                             WHERE NOT EXISTS (SELECT * FROM GraphInfo
                                              WHERE function = "{function}"
                                              AND x_val = "{x}")"""


            cursor.execute(statement2)
            conn.commit()

        else:

            statement2 = f"""INSERT INTO GraphInfo (function, x_val, y_val, z_val)
                             SELECT * FROM(VALUES ("{function}","{x}","{y}","{z}"))
                             WHERE NOT EXISTS (SELECT * FROM GraphInfo
                                              WHERE function = "{function}"
                                              AND x_val = "{x}")"""


            cursor.execute(statement2)
            conn.commit()


        
    

    @staticmethod
    def Del_func(function, dim):
    

        statement1 = f"""DELETE FROM Graphs
                         WHERE Username = "{user}"
                         AND function = "{function}"
                         AND dim = "{dim}" """

        

        cursor.execute(statement1)

        conn.commit()

        
    @staticmethod
    def Get_func(function, dim):

        if dim == "2D":

            statement1 = f"""SELECT x_val, y_val FROM GraphInfo
                         WHERE function = "{function}" 
                         AND z_val IS NULL"""
        
            cursor.execute(statement1)

        
            data = cursor.fetchall()

            if data != []:

                nan = np.nan

                return eval(data[0][0]), eval(data[0][1])
            
            else:

                raise NameError
        


        elif dim == "3D":

            statement1 = f"""SELECT x_val, y_val, z_val FROM GraphInfo
                         WHERE function = "{function}" 
                         AND z_val IS NOT NULL"""
        
            cursor.execute(statement1)

            data = cursor.fetchall()

            if data != []:

                nan = np.nan

                return eval(data[0][0]), eval(data[0][1]), eval(data[0][2])
            
            else:

                raise NameError
        
        else:

            raise TypeError

    


