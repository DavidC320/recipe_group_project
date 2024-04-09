"""
3/30/2024
Food Category Object
---

"""
from .BaseTableObject import BaseTable

class Food_Category(BaseTable):
    def __init__(self, id:int = -1, name:str = "Null"):
        super().__init__(id)
        self.id = id
        self.name = name
    
    
    @staticmethod
    def get_table_string() -> str:
        create_table_string: str = """
        CREATE TABLE IF NOT EXISTS food_category (
        food_category_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL);"""
        return create_table_string
    
    def to_array(self) -> list:
        return [self.id, self.name]
        
    def sqlite_insert(self) -> str:
        return f"""
            INSERT INTO food_category (name)
            VALUES ("{self.name}");"""

    def sqlite_update(self) -> str:
        return f"""
            UPDATE food_category SET food_category_id = {self.id}, name = "{self.name}"
            WHERE food_category_id = {self.id};
            """