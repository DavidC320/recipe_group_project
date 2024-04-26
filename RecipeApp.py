"""
4/1//2024
---

"""
# Tkitner
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd 
from tkinter_objects import *
# SQLite
import sqlite3
from TableObjects import *
# Encryption
from cryptography.fernet import Fernet
#
from Screens import *

class RecipeApp(FrameController):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.sqlite_connector = None
        self.title("Recipe Book")
    
    def connect_to_file(self, path:str, create_mode = False):
        self.close_connection()
        self.sqlite_connector = SqliteConnecter(path)

        tables = [
            FoodCategory.get_table_string(), 
            Recipe.get_table_string(), 
            Ingredient.get_table_string(),
            User.get_table_string()
            ]
        
        categories = [
            FoodCategory(-1, "Breakfast"), FoodCategory(-1, "Lunch"), FoodCategory(-1, "Dinner")
            ]

        # Runs each of the commands in the tables.
        for table_command in tables:
            self.sqlite_connector.c.execute(table_command)
        
        # creates the food categories
        if create_mode:
            for category in categories:
                self.sqlite_connector.c.execute(category.to_sqlite())
        
        self.sqlite_connector.conn.commit()
    
    def close_connection(self):
        if isinstance(self.sqlite_connector, sqlite3.Connection):
            self.sqlite_connector.c.close()
    
    def get_connector(self):
        if not self.sqlite_connector:
            raise ValueError("A connection has not been created")
        else:
            return self.sqlite_connector
    


conn = SqliteConnecter("RecipeTest.db")
root = RecipeApp(screenName= "Recipe Book")

root.add_frame_direct("start", StartScreen(root.frame_holder, root))
root.add_frame_direct("create database", CreateDatabaseScreen(root.frame_holder, root))
root.add_frame_direct("load database", LoadDatabaseScreen(root.frame_holder, root))
root.add_frame_direct("recipe index", RecipeIndex(root.frame_holder, root))
root.add_frame_direct("view recipe", ViewRecipe(root.frame_holder, root, True))
root.add_frame_direct("create recipe", ViewRecipe(root.frame_holder, root, False))
root.add_frame_direct("create admin", CreateAdmin(root.frame_holder, root))
root.add_frame_direct("create user", CreateUser(root.frame_holder, root, False))
root.add_frame_direct("Update user", CreateUser(root.frame_holder, root, False))
root.add_frame_direct("login", Login(root.frame_holder, root))
root.add_frame_direct("user index", UserIndex(root.frame_holder, root))
root.add_frame_direct("main menu", MainMenu(root.frame_holder, root))


root.open_frame("login")
root.mainloop()

"""
Resources:

https://stackoverflow.com/questions/2395431/using-tkinter-in-python-to-edit-the-title-bar
How to add a title

https://docs.python.org/3/library/dialog.html
How to create a file dialog

https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/
How to encrypt and decrypt

https://tkdocs.com/tutorial/widgets.html#checkbutton
How to use basic widgets

https://www.geeksforgeeks.org/combobox-widget-in-tkinter-python/
How to put values into a list

https://victoria.dev/blog/do-i-raise-or-return-errors-in-python/
How to raise an error

https://stackoverflow.com/questions/31732177/tkinter-tclerror-bad-file-type-using-askopenfilename
use lists [] not arrays ()

https://www.tutorialspoint.com/python/tk_listbox.htm
how to insert into a listbox

https://www.sqlitetutorial.net/sqlite-where/
How to use where

https://youtu.be/IkjAkTMHrUw?si=fVK7FpRhiCdlq_Ia
How to use the text widgit

https://stackoverflow.com/questions/43860088/deselecting-from-a-listbox-in-tkinter
How to deselect items in a list box
"""