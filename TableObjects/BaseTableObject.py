"""
4/9/2024
Base Table Object
---
This is the framework that all SQLtables use.
"""

class BaseTable:
    '''
    The base for all tables, stores data for records and their associated table.
    '''
    def __init__(self, id:int = -1) -> None:
        self.id = id
    
    @staticmethod
    def get_table_string() -> str:
        '''
        Returns the SQLite statement to create the table
        '''
    
    def assign_by_array(self, list):
        """
        Assigns the the variables in a list into the object
        and returns self
        """
    
    def to_array(self) -> list:
        '''
        Returns the array of variables used in this current record.
        '''

    def sqlite_insert(self) -> str:
        '''
        Returns the SQLite statement to insert a record into a table.
        '''

    def sqlite_update(self) -> str:
        '''
        Returns the SQLite statement to update a record into a table.
        '''
    
    def to_sqlite(self) -> str:
        '''
        Returns the appropriate SQLite statement to add or update the record.
        '''
        if self.id < 0: # If this object hasn't been added to the database
            return self.sqlite_insert()
        else:  # If this object is in the database
            return self.sqlite_update()


"""
References:

https://www.tutorialspoint.com/sqlite/sqlite_syntax.htm
The commands in sqlite are called statements
"""