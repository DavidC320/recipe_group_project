import tkinter as tk
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath("tkinter_objects\\__init__.py"))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from tkinter_objects.ControllerMainObject import *
from TableObjects import *

class RecipeIndex(ChildFrame):
    def __init__(self, master, controller, **kwargs) -> None:
        super().__init__(master, controller, **kwargs)
        tk.Label(self, text="Recipe Index").grid(row=0, column= 0)

        self.search_query = tk.StringVar()
        self.search_entry = tk.Entry(self, textvariable=self.search_query)
        self.search_entry.grid(row=1, column=0)

        self.show_hidden = tk.BooleanVar()
        self.show_hidden_check_button = tk.Checkbutton(self, text="Show Hidden", variable=self.show_hidden)
        self.show_hidden_check_button.grid(row=1, column=2)

        self.search_button = tk.Button(self, text="Search", command=self.search)
        self.search_button.grid(row=1, column=1)

        self.list_of_recipes = []
        self.recipe_list_box = tk.Listbox(self, height=10)
        self.recipe_list_box.grid(row=2, column=0)

        self.control_frame = tk.Frame(self)
        self.control_frame.grid(row=3, column=0)

        self.create_button = tk.Button(self.control_frame, text="Create", command=self.create_recipe)
        self.create_button.grid(row=0, column=0)

        self.view_button = tk.Button(self.control_frame, text="View", command=self.view_recipe)
        self.view_button.grid(row=0, column=1)

        self.back_button = tk.Button(self.control_frame, text="Back", command=lambda: controller.open_frame("main menu"))
        self.back_button.grid(row=0, column=2)
    
    def on_close(self):
        self.clean_list()
        self.show_hidden.set(False)
        self.search_query.set('')
    
    def on_open(self):
        connection : SqliteConnecter = self.controller.get_connector()
        connection.c.execute("""
                             SELECT * FROM recipes
                             WHERE hidden = 0;
                             """)
        self.add_into_list_of_recipes(connection.c.fetchall())
        
    
    def create_recipe(self):
        self.controller.open_frame("create recipe").set_new()

    
    def view_recipe(self):
        if self.recipe_list_box.curselection():
            recipe = self.list_of_recipes[self.recipe_list_box.curselection()[0]]
            self.controller.open_frame("view recipe").set_recipe(recipe)
    
    def add_into_list_of_recipes(self, list_of_recipes:list):
        self.clean_list()
        for recipe in list_of_recipes:
            self.recipe_list_box.insert(recipe[0], recipe[2])
            self.list_of_recipes.append(Recipe().assign_by_array(recipe))

    
    def search(self):
        connection : SqliteConnecter = self.controller.get_connector()
        search_statement = f"""
                            SELECT * FROM recipes
                            WHERE hidden = {1 if self.show_hidden.get() else 0}
                            """
        
        if self.search_query.get() != "":
            search_statement += f" AND name LIKE '{self.search_query.get()}%';"
        else:
            search_statement += ';'
        
        connection.c.execute(search_statement)
        self.add_into_list_of_recipes(connection.c.fetchall())

    def clean_list(self):
        self.recipe_list_box.delete(0, self.recipe_list_box.size())
        self.list_of_recipes = []