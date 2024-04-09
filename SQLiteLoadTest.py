"""
4/9/2024
This is to test if recording works
"""
import sqlite3
import pprint
from TableObjects import *
from TableObjects import *

conn = sqlite3.connect("RecipeTest.db")  # Connects or creates a database file.
c = conn.cursor()  # Allows the database to be changed

objects : dict = {
    "food categories" : {
        "select statement" :  "SELECT * from food_category;",
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
    record_id = record[0]
    record_name = record[1]
    created_object_list.append(Food_Category(record_id, record_name))
objects.get("food categories")["objects"] = created_object_list


# create Recipe Objects
created_object_list = []
for record in objects.get("recipes").get("records"):
    record_id = record[0]
    record_category_id = record[1]
    record_name = record[2]
    record_hidden = record[3]
    record_description = record[4]
    record_instructions = record[5]
    created_object_list.append(Recipe(record_id, record_name, record_hidden, record_description, record_category_id, record_instructions))
objects.get("recipes")["objects"] = created_object_list


# create Ingredient objects
created_object_list = []
for record in objects.get("ingredients").get("records"):
    record_id = record[0]
    record_category_id = record[1]
    record_name = record[2]
    record_amount = record[3]
    created_object_list.append(Ingredient(record_id, record_category_id, record_name, record_amount))
objects.get("ingredients")["objects"] = created_object_list


# Create User objects
created_object_list = []
for record in objects.get("users").get("records"):
    record_id = record[0]
    record_name = record[1]
    record_password = record[2]
    record_type = record[3]
    created_object_list.append(User(record_id, record_name, record_password, record_type))
objects.get("users")["objects"] = created_object_list

print("\ncompleted record to object\n")
pprint.pprint(objects)


conn.close()  # Closes the connection