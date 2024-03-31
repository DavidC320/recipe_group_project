"""
3/29/2024
Ingredient Object
---
The ingredient object is an object that contains the data fro a recipe that can be loaded or saved to
a SQLite database.
"""

class Ingredient:
    def __init__(self, id:int = -1, recipe_id:int = -1, name:str = "null", amount:str = "lb"):
        self.id = id
        self.recipe_id = recipe_id
        self.name = name
        self.amount = amount
    
    """
    Returns the SQLite command to create the object table.
    """
    @staticmethod
    def get_table_string() -> str:
        create_table_string : str = """
        CREATE TABLE IF NOT EXISTS ingredients (
        ingredient_id INTEGER PRIMARY KEY,
        recipe_id INTEGER NOT NULL 
            REFERENCES recipes (recipe_id),
        name TEXT NOT NULL,
        ingredient_amount TEXT
        );"""
        return create_table_string

    """
    Converts the table into a SQLite row command
    """
    def to_sqlite(self) -> str:
        if self.recipe_id < 0:
            return "The recipe hasn't been saved to SQLite."
        if id < 0:  # If this object hasn't been added to the database
            return f"""
            INSERT INTO ingredients (recipe_id, name, ingredient_amount) 
            VALUES ({self.recipe}, "{self.name}", "{self.amount}");"""
        else:  ## If this object is in the database
            return f"""
            UPDATE ingredients SET recipe_id = {self.recipe_id}, name = "{self.name}", ingredient_amount = "{self.amount}"
            WHERE ingredient_id = {self.id};
            """

"""
References:

https://www.sqlite.org/foreignkeys.html
How to assign foreign keys

https://www.sqlitetutorial.net/sqlite-insert/
How to insert a row into a table
INSERT INTO table1 (column1,column2 ,..)
VALUES 
   (value1,value2 ,...),
   (value1,value2 ,...),
    ...
   (value1,value2 ,...);

https://www.tutorialspoint.com/sqlite/sqlite_update_query.htm
How to update a row
sqlite> UPDATE COMPANY SET ADDRESS = 'Texas' WHERE ID = 6;
"""