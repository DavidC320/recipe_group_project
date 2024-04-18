"""
4/9/2024
This is to test if recording works
"""
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath("tkinter_objects\\__init__.py"))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import sqlite3
import pprint
from TableObjects import *

conn = sqlite3.connect("RecipeTest.db")  # Connects or creates a database file.
c = conn.cursor()  # Allows the database to be changed

objects : dict = {
    "food categories" : {
        "select statement" :  "SELECT * from food_categories;",
        "records" : [],
        "objects" : []
    },
    "recipes" : {
        "select statement" :  "SELECT * from recipes;",
        "records" : [],
        "objects" : []
    },
    "ingredients" : {
        "select statement" :  "SELECT * from ingredients;",
        "records" : [],
        "objects" : []
    },
    "users" : {
        "select statement" :  "SELECT * from users;",
        "records" : [],
        "objects" : []
    }
}


# get all of the records within the dictionary
for object_key in objects:
    object_dict = objects.get(object_key)
    print(object_dict)
    c.execute(object_dict["select statement"])
    object_dict["records"] = c.fetchall()

print("\ncompleted record load\n")
pprint.pprint(objects)


# create Food Category Objects 
created_object_list = []
for record in objects.get("food categories").get("records"):
    created_object_list.append(FoodCategory().assign_by_array(record))
objects.get("food categories")["objects"] = created_object_list


# create Recipe Objects
created_object_list = []
for record in objects.get("recipes").get("records"):
    created_object_list.append(Recipe().assign_by_array(record))
objects.get("recipes")["objects"] = created_object_list


# create Ingredient objects
created_object_list = []
for record in objects.get("ingredients").get("records"):
    created_object_list.append(Ingredient().assign_by_array(record))
objects.get("ingredients")["objects"] = created_object_list


# Create User objects
created_object_list = []
for record in objects.get("users").get("records"):
    created_object_list.append(User().assign_by_array(record))
objects.get("users")["objects"] = created_object_list

print("\ncompleted record to object\n")
pprint.pprint(objects)


conn.close()  # Closes the connection