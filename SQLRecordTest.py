"""
4/4/2024
This is to test if recording works
"""
import sqlite3
from TableObjects import Food_Category, Ingredient, Recipe, create_full_recipe

conn = sqlite3.connect("RecipeTest.db")  # Connects or creates a database file.
c = conn.cursor()  # Allows the database to be changed

categories = [
    Food_Category(-1, "Snack"), Food_Category(-1, "Dessert"), Food_Category(-1, "Brunch"),  # Create test
    Food_Category(1, "Breakfast"), Food_Category(2, "Lunch"), Food_Category(3, "Dinner")  # Update test
    ]
recipes = [
    Recipe(food_category= 1), Recipe(food_category= 2), Recipe(food_category= 3),  # Create test
    Recipe(2, "Munchos", food_category= 2) # Update test
    ]
ingredients = [
    Ingredient(recipe_id=1), Ingredient(recipe_id=2), Ingredient(recipe_id=3),  # Create Test
    Ingredient(1, 2, "apricots")  # Update test
]

for category_list in (categories, recipes, ingredients):
    for category in category_list:
        print(category.to_sqlite())
        c.execute(category.to_sqlite())
        c.execute("SELECT last_insert_rowid(); ")
        category.id = c.fetchone()[0]

create_full_recipe(c, 
                   Food_Category(name="Snug"), 
                   Recipe(name="bug", description="In a rug", instructions="Eating grub"), 
                   [Ingredient(name="Dirt", amount=" 2 Tons")])

c.execute("SELECT * from food_category;")
print(c.fetchall())
c.execute("SELECT * from recipes;")
print(c.fetchall())
c.execute("SELECT * from ingredients;")
print(c.fetchall())
"""
https://stackoverflow.com/questions/2127138/how-to-retrieve-the-last-autoincremented-id-from-a-sqlite-table
Found this to get the last id

https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
How to get data from the database

https://www.geeksforgeeks.org/python-ways-to-convert-boolean-values-to-integer/
How to turn a bool into an int
"""