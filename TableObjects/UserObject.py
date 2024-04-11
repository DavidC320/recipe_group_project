"""
3/30/2024
User category Object
"""
from .BaseTableObject import BaseTable

class User(BaseTable):
    def __init__(self, id:int = -1, username:str = "", password:str = "", admin:int = 1):
        super().__init__(id)
        self.username: str = username
        self.password: str = password
        self.admin: int = admin
    
    @staticmethod
    def get_table_string() -> str:
        return """
        CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        admin INTEGER NOT NULL
        );"""
    
    def sqlite_insert(self) -> str:
         return f"""
            INSERT INTO users (username, password, admin)
            VALUES ("{self.username}", "{self.password}", {self.admin});"""

    def sqlite_update(self) -> str:
        return f""" UPDATE users SET username = "{self.username}", password = "{self.password}", admin = {self.admin} 
            WHERE user_id = {self.id}
            """

    def to_array(self):
        return [self.id, self.username, self.password, self.admin]
    
    def assign_by_array(self, list):
        self.id = list[0]
        self.username = list[1]
        self.password = list[2]
        self.admin = list[3]
        return self
"""
Warning:

The introduction of a user table will cause some issues
1. The user will need to create an admin account to set up the recipe book, this will mean a slight delay between acquisition and operation of the main functionality of the software.
2. The user will need to log in every time they close the software.
3. There is a chance that the user could lock themselves out of the recipe book making it unaccessible either by forgetting their password or changing the only admin user to a standard user.
4. There will need to be an encryption for the passwords so that if a person where to steal the database, though this will not protect the recipes but only the user passwords.
"""