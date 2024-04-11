"""
3/27/2024
Recipe Object
---
The Recipe Object is a object that contains the data for a recipe that can be loaded 
or saved to a SQLITE database. 
"""
from .BaseTableObject import BaseTable

class Recipe(BaseTable):
    def __init__(self, id:int = -1, name:str = "null", hidden:int = 0, description:str  = "No description", food_category:int = -1, instructions:str = ""):
        super().__init__(id)
        self.name : str = name
        self.hidden : int = hidden
        self.description : str = description
        self.food_category : int = food_category
        self.instructions : str = instructions

    @staticmethod
    def get_table_string() -> str:
        create_table_string : str = """
        CREATE TABLE IF NOT EXISTS recipes (
        recipe_id INTEGER PRIMARY KEY,
        category_id INTEGER NOT NULL 
            REFERENCES food_categories (category_id),
        name TEXT NOT NULL,
        hidden Integer NOT NULL,
        description TEXT NOT NULL,
        instructions TEXT
        );"""
        return create_table_string

    def sqlite_insert(self) -> str:
        return f"""
            INSERT INTO recipes (category_id, name, hidden, description, instructions)
            VALUES ({self.food_category}, "{self.name}", {self.hidden}, "{self.description}", "{self.instructions}");"""

    def sqlite_update(self) -> str:
        return f"""
            UPDATE recipes SET category_id = {self.food_category}, name = "{self.name}", hidden = {self.hidden}, description = "{self.description}", instructions = "{self.instructions}"
            WHERE recipe_id = {self.id};
            """
    
    def to_array(self) -> list:
        return [self.name, self.hidden, self.description, self.food_category, self.instructions]
    
    def assign_by_array(self, list):
        self.id = list[0]
        self.food_category = list[1]
        self.name = list[2]
        self.hidden = list[3]
        self.description = list[4]
        self.instructions = list[5]
        return self


"""
References:

https://www.w3schools.com/python/python_classes.asp
I forgot how to make objects.

https://stackoverflow.com/questions/3933197/how-to-declare-variable-type-c-style-in-python
How to declare a variable because Godot got me addicted to it.
var : data type = ?

https://stackoverflow.com/questions/45268794/calling-a-class-function-without-triggering-the-init
Wanted to make sure that I could make a method without initializing the object
@staticmethod
def method()

https://www.sqlitetutorial.net/sqlite-create-table/
I needed to see an example of how to make a table

https://www.toppr.com/guides/python/python-introduction/variables-constants-literals/python-variables-constants-and-literals/
So constants is just name scheme on python
MIKE = "Mike"
"""