"""
3/29/2024
Ingredient Object
---
The ingredient object is an object that contains the data fro a recipe that can be loaded or saved to
a SQLite database.
"""

from .BaseTableObject import BaseTable

class Ingredient(BaseTable):
    def __init__(self, id:int = -1, recipe_id:int = -1, name:str = "null", amount:str = "lb"):
        super().__init__(id)
        self.recipe_id : int = recipe_id
        self.name : str = name
        self.amount : str = amount
    
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

    def sqlite_insert(self) -> str:
        return f"""
            INSERT INTO ingredients (recipe_id, name, ingredient_amount) 
            VALUES ({self.recipe_id}, "{self.name}", "{self.amount}");"""

    def sqlite_update(self) -> str:
        return f"""
            UPDATE ingredients SET recipe_id = {self.recipe_id}, name = "{self.name}", ingredient_amount = "{self.amount}"
            WHERE ingredient_id = {self.id};
            """
    def to_array(self):
        return [self.recipe_id, self.name, self.amount]
    
    def assign_by_array(self, list):
        self.id = list[0]
        self.recipe_id = list[1]
        self.name = list[2]
        self.amount = list[3]
        return self

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