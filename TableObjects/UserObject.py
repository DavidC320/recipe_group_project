"""
3/30/2024
User category Object
"""

class User:
    def __init__(self, id:int = -1, username:str = "", password:str = "", admin:bool = True):
        self.id = id
        self.username = username
        self.password = password
        self.admin = admin
    
    @staticmethod
    def get_table_string() -> str:
        return """
        CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        admin INTEGER NOT NULL
        );"""
    
    def to_sqlite(self):
        if self.id <0:
            return f"""
            INSERT INTO users (username, password, admin)
            VALUES ("{self.username}", "{self.password}", {self.admin});"""
        else:
            return f""" UPDATE users SET username = "{self.username}", password = "{self.password}", admin = {int(self.admin == True)} 
            WHERE user_id = {self.id}
            """
"""
Warning:

The introduction of a user table will cause some issues
1. The user will need to create an admin account to set up the recipe book, this will mean a slight delay between acquisition and operation of the main functionality of the software.
2. The user will need to log in every time they close the software.
3. There is a chance that the user could lock themselves out of the recipe book making it unaccessible either by forgetting their password or changing the only admin user to a standard user.
4. There will need to be an encryption for the passwords so that if a person where to steal the database, though this will not protect the recipes but only the user passwords.
"""