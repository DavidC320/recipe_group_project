"""
3/30/2024
Food Category Object
---

"""
from .BaseTableObject import BaseTable

class FoodCategory(BaseTable):
    def __init__(self, id:int = -1, name:str = "null"):
        super().__init__(id)
        self.name = name
    
    
    @staticmethod
    def get_table_string() -> str:
        create_table_string: str = """
        CREATE TABLE IF NOT EXISTS food_categories (
        food_category_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL);"""
        return create_table_string
    
    def to_array(self) -> list:
        return [self.id, self.name]
        
    def sqlite_insert(self) -> str:
        return f"""
            INSERT INTO food_categories (name)
            VALUES ("{self.name}");"""

    def sqlite_update(self) -> str:
        return f"""
            UPDATE food_categories SET food_category_id = {self.id}, name = "{self.name}"
            WHERE food_category_id = {self.id};
            """
    
    def assign_by_array(self, list):
        self.id = list[0]
        self.name = list[1]
        return self