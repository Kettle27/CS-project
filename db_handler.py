# Add all needed Libraries
import sqlite3
from extension import *
# Open a connection with the database
conn = sqlite3.connect("Calculator.db")
cursor = conn.cursor()  
# Login class handles all of the Users usernames and passwords
class Login:
    # Staticmethod check_login checks to see if the username and password exists and is correct
    @staticmethod
    def check_login(Username, Password):
        # SQL statement for checking username and password
        statement = f"""SELECT * FROM Logins
                        WHERE Username = "{Username}" AND Password = "{Password}" """
        # Execute the statement
        cursor.execute(statement)
        # If output is empty
        if cursor.fetchall() == []:    
            # Output is empty
            return False
        # Output is not empty
        else:
            # User has successfully logged in
            global user
            user = Username
            return True
    # Staticmethod create_login adds logins to the database
    @staticmethod
    def create_login(Username, Password):
        # SQL statement is used to check if the username has not been used already
        statement = f"""SELECT * FROM Logins
                        WHERE Username = "{Username}"; """
        # Execute the statement
        cursor.execute(statement)
        # If empty that means username has not been used
        if cursor.fetchall() == []:
            # empty
            # SQL statement adds the username and password into the database
            statement = f"""INSERT INTO Logins (Username, Password)
                        VALUES ("{Username}","{Password}");"""
            # Execute and commit the statement
            cursor.execute(statement)
            conn.commit()
            return True
        # Username already in use
        else:
            return False
# User_info class deals with all the users graphs
class User_info:
    # Staticmethod Load_func gets all of the users graphs
    @staticmethod
    def Load_func(dim):
        # If dimension is 2D
        if dim == "2D":
            # SQL statement checks which graphs the user has saved and gets the x, y values and the function
            statement1 = f"""SELECT x_val, y_val, function FROM GraphInfo
                             WHERE EXISTS (SELECT Username FROM Graphs
                                           WHERE Username = "{user}"
                                           AND Graphs.function = GraphInfo.function
                                           AND dim = "{dim}"
                                           AND z_val IS NULL) """
            # Execute statement
            cursor.execute(statement1)
            data = cursor.fetchall()
            # Iterate through data and yield data
            for i in data:
                # nan is the same as a Null type
                nan = np.nan
                # eval() function treats the input as a statement
                # yield creates a generator object
                yield [eval(i[0]), eval(i[1]), i[2]]
        # Dimension is 3D
        else:
            # SQL statement checks which graphs the user has saved and gets the x, y, z values and the function
            statement2 = f"""SELECT x_val, y_val, function FROM GraphInfo
                             WHERE EXISTS (SELECT Username FROM Graphs
                                           WHERE Username = "{user}"
                                           AND Graphs.function = GraphInfo.function
                                           AND dim = "{dim}")
                                           AND z_val IS NOT NULL """
            # Execute statement
            cursor.execute(statement2)
            data = cursor.fetchall()
            # Iterate through data and yield data
            for i in data:
                # nan is the same as a Null type
                nan = np.nan
                # eval() function treats the input as a statement
                # yield creates a generator object
                yield [eval(i[0]), eval(i[1]), i[2]]
    # Staticmethod Add_function Adds functions and their data to the database under a users name
    @staticmethod
    def Add_func(dim, function, x, y, z = None):
        # Add the users graph where it doesn't exist
        statement1 = f"""INSERT INTO Graphs (Username, function, dim)
                         SELECT * FROM(VALUES ("{user}","{function}","{dim}"))
                         WHERE NOT EXISTS (SELECT * FROM Graphs
                                          WHERE Username = "{user}"
                                          AND function = "{function}"
                                          AND dim = "{dim}")"""
        # Execute and commit the statement
        cursor.execute(statement1)
        conn.commit()
        # if dimension is 2D
        if dim == "2D":
            # Add the data for that certain graph if it doesn't exist
            statement2 = f"""INSERT INTO GraphInfo (function, x_val, y_val)
                             SELECT * FROM(VALUES ("{function}","{x}","{y}"))
                             WHERE NOT EXISTS (SELECT * FROM GraphInfo
                                              WHERE function = "{function}"
                                              AND x_val = "{x}")"""
            # Execute and commit the statement
            cursor.execute(statement2)
            conn.commit()
        else:
            # Add the data for that certain graph if it doesn't exist
            statement2 = f"""INSERT INTO GraphInfo (function, x_val, y_val, z_val)
                             SELECT * FROM(VALUES ("{function}","{x}","{y}","{z}"))
                             WHERE NOT EXISTS (SELECT * FROM GraphInfo
                                              WHERE function = "{function}"
                                              AND x_val = "{x}")"""
            # Execute and commit the statement
            cursor.execute(statement2)
            conn.commit()
    # Staticmethod Del_func Deletes the function from the database under the users username
    @staticmethod
    def Del_func(function, dim):
        statement1 = f"""DELETE FROM Graphs
                         WHERE Username = "{user}"
                         AND function = "{function}"
                         AND dim = "{dim}" """
        cursor.execute(statement1)
        conn.commit()
    # Staticmethod Get_func Gets the x, y and z values from a function from the database depending what dimension its in
    @staticmethod
    def Get_func(function, dim):
        # If dimension is 2D
        if dim == "2D":
            # Get x and y values from database
            statement1 = f"""SELECT x_val, y_val FROM GraphInfo
                         WHERE function = "{function}"
                         AND z_val IS NULL"""
            # Execute statement
            cursor.execute(statement1)
            data = cursor.fetchall()
            # If not empty
            if data != []:
                # Not empty
                # nan is the same as a Null type
                nan = np.nan
                # eval() function treats the input as a statement
                return eval(data[0][0]), eval(data[0][1])
            # Empty
            else:
                # Raise an error for exception handling
                raise NameError
        # dimension is 3D
        else:
            # Get x, y and z values from database
            statement1 = f"""SELECT x_val, y_val FROM GraphInfo
                         WHERE function = "{function}"
                         AND z_val IS NOT NULL"""
            # Execute statement
            cursor.execute(statement1)
            data = cursor.fetchall()
            # If not empty
            if data != []:
                # Not empty
                # nan is the same as a Null type
                nan = np.nan
                # eval() function treats the input as a statement
                return eval(data[0][0]), eval(data[0][1])
            else:
                # Raise an error for exception handling
                raise NameError
