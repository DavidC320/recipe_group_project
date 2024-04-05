"""
3/27/2024
Recipe Object
---
The Recipe Object is a object that contains the data for a recipe that can be loaded 
or saved to a SQLITE database. 
"""

class Recipe:
    def __init__(self, id:int = -1, name:str = "null", hidden = False, description:str  = "No description", food_category:int = -1, instructions:str = ""):
        self.id : int = id  # -1 means that the id hasn't been assigned yet
        self.name : str = name
        self.hidden : bool = hidden
        self.description : str = description
        self.food_category : int = food_category
        self.instructions : str = instructions

    """
    Returns the SQLite command to create the object table.
    """
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
    
    """
    Converts the table into a SQLite row command
    """
    def to_sqlite(self):
        if self.food_category < 0:
            return "The Food Category has not been saved to the table."
        
        elif self.id < 0:
            return f"""
            INSERT INTO recipes (category_id, name, hidden, description, instructions)
            VALUES ({self.food_category}, "{self.name}", {int(self.hidden == True)}, "{self.description}", "{self.instructions}");"""
        else:
            return f"""
            UPDATE recipes SET recipe_id = {self.id}, category_id = {self.food_category}, name = "{self.name}", hidden = {int(self.hidden == True)}, description = "{self.description}", instructions = "{self.instructions}"
            WHERE recipe_id = {self.id};
            """
    

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