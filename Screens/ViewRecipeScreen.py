import tkinter as tk
from tkinter import ttk
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath("tkinter_objects\__init__.py"))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from tkinter_objects.ControllerMainObject import *
from TableObjects import *

class ViewRecipe(ChildFrame):
    def __init__(self, master, controller, view_else_create, **kwargs) -> None:
        # info
        self.recipe:Recipe
        self.category_dictionary = {}
        
        super().__init__(master, controller, **kwargs)
        if view_else_create:
            tk.Label(self, text="View Recipe").grid(row=0, column= 0)
        else:
            tk.Label(self, text="Create Recipe").grid(row=0, column= 0)

        self.show_hidden = tk.BooleanVar()
        self.show_hidden_check_button = tk.Checkbutton(self, text="Hide Recipe", variable=self.show_hidden)
        self.show_hidden_check_button.grid(row=1, column=0)

        self.name_label = tk.Label(self, text="Name")
        self.name_label.grid(row=2, column=0)

        self.name_variable = tk.StringVar()
        self.name_entry = tk.Entry(self, textvariable=self.name_variable)
        self.name_entry.grid(row = 3, column=0)

        self.category_label = tk.Label(self, text="<Category Name>")
        self.category_label.grid(row=4, column=0)
        
        self.food_category = tk.StringVar()
        self.category_combo_box = ttk.Combobox(self, textvariable=self.food_category)
        self.category_combo_box.grid(row=5, column=0)
        
        #################################################################################################
        ###################################### Ingredient controls ######################################
        #################################################################################################
        self.ingredient = Ingredient()
        self.ingredients = []

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

        self.ingredient_list_box = tk.Listbox(self, height=10)
        self.ingredient_list_box.grid(row=7, column=0, columnspan=4)

        self.ingredient_control_frame = tk.Frame(self)
        self.ingredient_control_frame.grid(row=8, column=0)

        self.edit_ingredient_button = tk.Button(self.ingredient_control_frame, text="edit", command=self.edit_ingredient)
        self.edit_ingredient_button.grid(row=0, column=0)

        self.deselect_ingredient_button = tk.Button(self.ingredient_control_frame, text="deselect", command=self.deselect_ingredient)
        self.deselect_ingredient_button.grid(row=0, column=1)

        self.delete_ingredient_button = tk.Button(self.ingredient_control_frame, text="delete ingredient")
        self.delete_ingredient_button.grid(row=0, column=2)
        #################################################################################################
        ###################################### Ingredient controls ######################################
        #################################################################################################

        tk.Label(self, text="Description").grid(row=9, column= 0)
        self.description_text = tk.Text(self, width=40, height=10)
        self.description_text.grid(row=9, column=0)

        tk.Label(self, text="Instructions").grid(row=10, column= 0)
        self.instruction_text = tk.Text(self, width=40, height=10)
        self.instruction_text.grid(row=11, column=0)

        ##########
        # Footer
        ##########
        self.control_frame = tk.Frame(self)
        self.control_frame.grid(row=12)

        if view_else_create:
            self.update_button = tk.Button(self.control_frame, text="Update", command=lambda: controller.open_frame("recipe index"))
            self.update_button.grid(row= 0, column=0)
        else:
            self.update_button = tk.Button(self.control_frame, text="Create", command=lambda: controller.open_frame("recipe index"))
        self.update_button.grid(row= 0, column=0)

        self.back_button = tk.Button(self.control_frame, text="Back", command=lambda: controller.open_frame("recipe index"))
        self.back_button.grid(row= 0, column=1)
        ##########
        # Footer #
        ##########
    
    def get_food_categories(self):
        connection : SqliteConnecter = self.controller.get_connector()
        connection.c.execute("""SELECT * FROM food_categories;""")
        list_of_food_categories = connection.c.fetchall()

        list_of_category_names = []
        dictionary_of_categories = {}
        for category in list_of_food_categories:
            list_of_category_names.append(category[1])
            dictionary_of_categories[category[1]] = category[0]
        
        self.category_combo_box["values"] = list_of_category_names
        self.category_dictionary = dictionary_of_categories
        self.food_category.set("")

    def set_new(self): 
        self.recipe = Recipe()
        self.show_hidden.set(False)
        self.name_variable.set("")

        self.get_food_categories()
        
        self.ingredient = Ingredient()
        self.ingredients = []
        self.ingredient_name_var.set("")
        self.amount_name_var.set("")
        self.ingredient_list_box.delete(0, 'end')

        self.description_text.delete(0.0, 'end')
        self.instruction_text.delete(0.0, 'end')

        self.ingredient_list_box.select_clear(0, 'end')
    
    def set_recipe(self, recipe:Recipe):
        self.set_new()
        connection : SqliteConnecter = self.controller.get_connector()

        self.recipe = recipe
        # Recipe specific
        self.name_variable.set(recipe.name)
        self.show_hidden.set(True if recipe.hidden == 1 else False)
        self.description_text.insert(0.0, recipe.description)
        self.instruction_text.insert(0.0, recipe.instructions)

        # food category
        connection.c.execute(f"""SELECT * FROM food_categories
                             WHERE food_category_id = {recipe.food_category}""")
        food_category = FoodCategory().assign_by_array(connection.c.fetchone())
        self.food_category.set(food_category.name)

        # ingredients
        self.ingredient_name_var.set("")
        self.amount_name_var.set("")
        connection.c.execute(f"""SELECT * FROM ingredients
                             WHERE recipe_id = {recipe.id}""")
        list_of_ingredients = connection.c.fetchall()
        for ingredient in list_of_ingredients:
            text = ingredient[2] + " " + ingredient[3]
            self.ingredient_list_box.insert(ingredient[0], text)
            self.ingredients.append(Ingredient().assign_by_array(ingredient))
    
    def save_recipe(self):
        pass

    def save_ingredient(self):
        pass

    def edit_ingredient(self):
        if self.ingredient_list_box.curselection():
            print(self.ingredients[self.ingredient_list_box.curselection()[0]])

    def deselect_ingredient(self):
        self.ingredient = Ingredient()
        self.ingredient_list_box.select_clear(0, 'end')

    def delete_ingredient(self):
        pass