"""
4/4/2024
This is to test if recording works
"""
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath("tkinter_objects\\__init__.py"))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import sqlite3
from TableObjects import *

conn = sqlite3.connect("RecipeTest.db")  # Connects or creates a database file.
c = conn.cursor()  # Allows the database to be changed

categories = [
    FoodCategory(-1, "Snack"), FoodCategory(-1, "Dessert"), FoodCategory(-1, "Brunch"),  # Create test
    FoodCategory(1, "Breakfast"), FoodCategory(2, "Lunch"), FoodCategory(3, "Dinner")  # Update test
    ]
recipes = [
    Recipe(food_category= 1), Recipe(food_category= 2), Recipe(food_category= 3),  # Create test
    Recipe(2, "Munchos", food_category= 2) # Update test
    ]
ingredients = [
    Ingredient(recipe_id=1), Ingredient(recipe_id=2), Ingredient(recipe_id=3),  # Create Test
    Ingredient(1, 2, "apricots")  # Update test
]
users = [
    User(username="Admin", password="admin101"), User(admin=False),  #Create Test
    User(1, "Joamoan", "swauusa", False)
]

for category_list in (categories, recipes, ingredients, users):
    for category in category_list:
        print(category.to_sqlite())
        c.execute(category.to_sqlite())
        c.execute("SELECT last_insert_rowid(); ")
        category.id = c.fetchone()[0]

create_full_recipe(c, 
                   FoodCategory(name="Snug"), 
                   Recipe(name="bug", description="In a rug", instructions="Eating grub"), 
                   [Ingredient(name="Dirt", amount=" 2 Tons")])

for statement in ["SELECT * from food_categories;", "SELECT * from recipes;", "SELECT * from ingredients;", "SELECT * from users;"]:
    c.execute(statement)
    print(c.fetchall())

conn.commit()
conn.close()  # Closes the connection


"""
https://stackoverflow.com/questions/2127138/how-to-retrieve-the-last-autoincremented-id-from-a-sqlite-table
Found this to get the last id

https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
How to get data from the database

https://www.geeksforgeeks.org/python-ways-to-convert-boolean-values-to-integer/
How to turn a bool into an int
"""