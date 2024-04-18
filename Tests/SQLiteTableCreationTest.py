"""
3/31/2024
SQLite test
This is to test creating tables from the objects
"""
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath("tkinter_objects\\__init__.py"))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import sqlite3
from TableObjects import *

conn = sqlite3.connect("RecipeTest.db")  # Connects or creates a database file.
c = conn.cursor()  # Allows the database to be changed

# Gets the commands to create the tables for the Database
tables = [
    FoodCategory.get_table_string(), 
    Recipe.get_table_string(), 
    Ingredient.get_table_string(),
    User.get_table_string()
    ]

# Runs each of the commands in the tables.
for table_command in tables:
    print(table_command)
    c.execute(table_command)

conn.commit()  # Saves the changes
conn.close()  # Closes the connection

"""
References:

https://youtu.be/pd-0G0MigUA?si=UvIUqwzjywTLGiHb
This video shows how to use SQLite
"""