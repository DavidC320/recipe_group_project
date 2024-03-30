"""
3/30/2024
Food Category Object
---

"""
class Food_Category:
    def __init__(self, id:int = -1, name:str = "Null"):
        self.id = id
        self.name = name
    
    @staticmethod
    def get_table_string() -> str:
        create_table_string: str = """
        CREATE TABLE food_category [If NOT EXISTS](
        food_category_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL);"""
        return create_table_string
    
    def to_sqlite(self):
        if id < 0:
            return f"""
            INSERT INTO food_category (food_category_id, name)
            VALUES ({self.id}, "{self.name}");"""
        else:
            return f"""
            UPDATE food_category SET food_category_id = {self.id}, name = "{self.name}"
            WHERE food_category_id = {self.id};
            """