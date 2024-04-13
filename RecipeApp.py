"""
4/1//2024
---

"""
# Tkitner
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd 
from TkinterOjects.ControllerMainObject import *

# SQLite
import sqlite3
from TableObjects import *

from cryptography.fernet import Fernet

class StartScreen(ChildFrame):
    def __init__(self, master, controller, **kwargs) -> None:
        super().__init__(master, controller, **kwargs)
        tk.Label(self, text="Main menu").pack()
        self.create_database = tk.Button(self, text="Create Database", command=lambda: controller.open_frame("create database"))
        self.create_database.pack()

        self.load_database = tk.Button(self, text="Load Database", command=lambda: controller.open_frame("load database"))
        self.load_database.pack()


class CreateDatabaseScreen(ChildFrame):
    def __init__(self, master, controller, **kwargs) -> None:
        super().__init__(master, controller, **kwargs)
        tk.Label(self, text="Create Database").pack()

        self.create_database_button = tk.Button(self, text="Select file destination", command=self.select_destination)
        self.create_database_button.pack()

        self.filepath_label = tk.Label(self, text="//filepath/?")
        self.filepath_label.pack()

        self.create_button = tk.Button(self, text="Create")
        self.create_button.pack()

        self.back_button = tk.Button(self, text="Back", command=lambda: controller.open_frame("start"))
        self.back_button.pack()
    
    def select_destination(self):
        data = fd.asksaveasfilename()
        self.filepath_label.config(text= data)


class LoadDatabaseScreen(ChildFrame):
    def __init__(self, master, controller, **kwargs) -> None:
        super().__init__(master, controller, **kwargs)
        tk.Label(self, text="load Database").pack()

        self.load_database_button = tk.Button(self, text="Select file destination", command=self.select_destination)
        self.load_database_button.pack()

        self.filepath_label = tk.Label(self, text="//filepath/?")
        self.filepath_label.pack()

        self.load_button = tk.Button(self, text="Load")
        self.load_button.pack()
        
        self.back_button = tk.Button(self, text="Back", command=lambda: controller.open_frame("start"))
        self.back_button.pack()
    
    def select_destination(self):
        data = fd.askopenfile()
        self.filepath_label.config(text= data)


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

        self.search_button = tk.Button(self, text="Search")
        self.search_button.grid(row=1, column=1)

        self.recipe_list_box = tk.Listbox(self, height=10)
        self.recipe_list_box.grid(row=2, column=0)

        self.control_frame = tk.Frame(self)
        self.control_frame.grid(row=3, column=0)

        self.create_button = tk.Button(self.control_frame, text="Create")
        self.create_button.grid(row=0, column=0)

        self.view_button = tk.Button(self.control_frame, text="View")
        self.view_button.grid(row=0, column=1)

        self.back_button = tk.Button(self.control_frame, text="Back", command=lambda: controller.open_frame("start"))
        self.back_button.grid(row=0, column=2)


class ViewRecipe(ChildFrame):
    def __init__(self, master, controller, view_else_create, **kwargs) -> None:
        super().__init__(master, controller, **kwargs)
        if view_else_create:
            tk.Label(self, text="View Recipe").grid(row=0, column= 0)
        else:
            tk.Label(self, text="Create Recipe").grid(row=0, column= 0)

        self.show_hidden = tk.BooleanVar()
        self.show_hidden_check_button = tk.Checkbutton(self, text="Hide Recipe", variable=self.show_hidden)
        self.show_hidden_check_button.grid(row=1, column=0)

        self.name_label = tk.Label(self, text="<Placeholder Name>")
        self.name_label.grid(row=2, column=0)

        self.name_variable = tk.StringVar
        self.name_entry = tk.Entry(self, textvariable=self.name_variable)
        self.name_entry.grid(row = 3, column=0)

        self.category_label = tk.Label(self, text="<Category Name>")
        self.category_label.grid(row=4, column=0)
        
        self.food_category = tk.StringVar()
        self.category_combo_box = ttk.Combobox(self, textvariable=self.food_category)
        self.category_combo_box.grid(row=5, column=0)
        self.category_combo_box['values'] = ("breakfast", "lunch", "dinner")
        
        #
        # Ingredient controls
        #
        self.sub_title_frame = tk.Frame(self)
        self.sub_title_frame.grid(row=6, column=0)
        
        tk.Label(self.sub_title_frame, text="Ingredient List").grid(row=0, column= 0, columnspan=4)

        self.ingredient_name_var = tk.StringVar()
        self.ingredient_name_entry = tk.Entry(self.sub_title_frame, textvariable=self.ingredient_name_var)
        self.ingredient_name_entry.grid(row=1, column=1)

        self.amount_name_var = tk.StringVar()
        self.amount_name_entry = tk.Entry(self.sub_title_frame, textvariable=self.amount_name_var)
        self.amount_name_entry.grid(row=1, column=2)
        
        self.create_ingredient_button = tk.Button(self.sub_title_frame, text="Add Ingredient")
        self.create_ingredient_button.grid(row=1, column=3)
        #
        # Ingredient controls
        #

        self.ingredient_list_box = tk.Listbox(self, height=10)
        self.ingredient_list_box.grid(row=7, column=0)

        tk.Label(self, text="Description").grid(row=8, column= 0)
        self.description_text = tk.Text(self, width=40, height=10)
        self.description_text.grid(row=9, column=0)

        tk.Label(self, text="Instructions").grid(row=10, column= 0)
        self.instruction_text = tk.Text(self, width=40, height=10)
        self.instruction_text.grid(row=11, column=0)

        #
        # Footer
        #
        self.control_frame = tk.Frame(self)
        self.control_frame.grid(row=12)

        if view_else_create:
            self.update_button = tk.Button(self.control_frame, text="Update", command=lambda: controller.open_frame("recipe index"))
            self.update_button.grid(row= 0, column=0)
        else:
            self.update_button = tk.Button(self.control_frame, text="Create", command=lambda: controller.open_frame("recipe index"))
        self.update_button.grid(row= 0, column=0)

        self.back_button = tk.Button(self.control_frame, text="Back", command=lambda: controller.open_frame("start"))
        self.back_button.grid(row= 0, column=1)
        #
        # Footer
        #


class CreateUser(ChildFrame):
    def __init__(self, master, controller, admin_mode, create_mode, **kwargs) -> None:
        super().__init__(master, controller, **kwargs)

        label_text = ""
        if create_mode:
            label_text += "Create"
        else:
            label_text += "Update"
        if admin_mode:
            label_text += " Admin"
        else:
            label_text += " User"
        tk.Label(self, text=label_text).grid(row=0, column=0, columnspan=2)
        
        tk.Label(self, text="Username").grid(row=1, column=0)
        self.username = tk.StringVar()
        self.username_entry = tk.Entry(self, textvariable=self.username)
        self.username_entry.grid(row=1, column=1)

        tk.Label(self, text="Password").grid(row=2, column=0)
        self.password = tk.StringVar()
        self.password_entry = tk.Entry(self, textvariable=self.password)
        self.password_entry.grid(row=2, column=1)

        self.control_frame = tk.Frame(self)
        self.control_frame.grid(row=3, column=0, columnspan=2)

        
        button_text = ""
        if create_mode:
            button_text += "Create"
        else:
            button_text += "Update"

        self.create_button = tk.Button(self.control_frame, text=button_text)
        self.create_button.grid(row=0, column=0)

        self.back_button = tk.Button(self.control_frame, text="Back", command=lambda: controller.open_frame("start"))
        self.back_button.grid(row=0, column=1)


class Login(ChildFrame):
    def __init__(self, master, controller, **kwargs) -> None:
        super().__init__(master, controller, **kwargs)
        tk.Label(self, text="Login").grid(row=0, column=0, columnspan=2)

        tk.Label(self, text="Username").grid(row=1, column=0)
        self.username = tk.StringVar()
        self.username_entry = tk.Entry(self, textvariable=self.username)
        self.username_entry.grid(row=1, column=1)

        tk.Label(self, text="Password").grid(row=2, column=0)
        self.password = tk.StringVar()
        self.password_entry = tk.Entry(self, textvariable=self.password)
        self.password_entry.grid(row=2, column=1)

        self.control_frame = tk.Frame(self)
        self.control_frame.grid(row=3, column=0, columnspan=2)

        self.create_button = tk.Button(self.control_frame, text="Login")
        self.create_button.grid(row=0, column=0)

        self.back_button = tk.Button(self.control_frame, text="Back", command=lambda: controller.open_frame("start"))
        self.back_button.grid(row=0, column=1)


class UserIndex(ChildFrame):
    def __init__(self, master, controller, **kwargs) -> None:
        super().__init__(master, controller, **kwargs)
        tk.Label(self, text="User Index").grid(row=0, column= 0)

        self.control_frame = tk.Frame(self)
        self.control_frame.grid(row=1, column=0)

        self.search_query = tk.StringVar()
        self.search_entry = tk.Entry(self.control_frame, textvariable=self.search_query)
        self.search_entry.grid(row=0, column=0)

        self.search_button = tk.Button(self.control_frame, text="Search")
        self.search_button.grid(row=0, column=1)

        self.recipe_list_box = tk.Listbox(self, height=10)
        self.recipe_list_box.grid(row=2, column=0)

        self.control_frame = tk.Frame(self)
        self.control_frame.grid(row=3, column=0)

        self.create_button = tk.Button(self.control_frame, text="Create User")
        self.create_button.grid(row=0, column=0)

        self.create_button = tk.Button(self.control_frame, text="Create Admin")
        self.create_button.grid(row=0, column=1)

        self.view_button = tk.Button(self.control_frame, text="View")
        self.view_button.grid(row=0, column=2)

        self.back_button = tk.Button(self.control_frame, text="Back", command=lambda: controller.open_frame("start"))
        self.back_button.grid(row=0, column=3)


class SqliteConnecter():
    def __init__(self) -> None:
        pass


conn = sqlite3.connect("RecipeTest.db")  # Connects or creates a database file.
c = conn.cursor()  # Allows the database to be changed

root = FrameController(screenName= "Recipe Book")
root.title("Recipe Book")

root.add_frame_direct("start", StartScreen(root.frame_holder, root))
root.add_frame_direct("create database", CreateDatabaseScreen(root.frame_holder, root))
root.add_frame_direct("load database", LoadDatabaseScreen(root.frame_holder, root))
root.add_frame_direct("recipe index", RecipeIndex(root.frame_holder, root))
root.add_frame_direct("view recipe", ViewRecipe(root.frame_holder, root, True))
root.add_frame_direct("create recipe", ViewRecipe(root.frame_holder, root, False))
root.add_frame_direct("create admin", CreateUser(root.frame_holder, root, True, True))
root.add_frame_direct("create user", CreateUser(root.frame_holder, root, False, True))
root.add_frame_direct("Update user", CreateUser(root.frame_holder, root, False, False))
root.add_frame_direct("login", Login(root.frame_holder, root))
root.add_frame_direct("user index", UserIndex(root.frame_holder, root))


root.open_frame("recipe index")
root.mainloop()

"""
Resources:

https://stackoverflow.com/questions/2395431/using-tkinter-in-python-to-edit-the-title-bar
How to add a title

https://docs.python.org/3/library/dialog.html
How to create a file dialog

https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/
How to encrypt and decrypt

https://tkdocs.com/tutorial/widgets.html#checkbutton
How to use basic widgets

https://www.geeksforgeeks.org/combobox-widget-in-tkinter-python/
How to put values into a list
"""