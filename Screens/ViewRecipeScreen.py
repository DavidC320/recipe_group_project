import tkinter as tk
from tkinter import ttk
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath("tkinter_objects\\__init__.py"))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from tkinter_objects.ControllerMainObject import *
from TableObjects import *

class ViewRecipe(ChildFrame):
    def __init__(self, master, controller, view_else_create, **kwargs) -> None:
        super().__init__(master, controller, **kwargs)
        # Variables
        self.recipe:Recipe
        self.category_dictionary = {}
        self.show_hidden = tk.BooleanVar()
        self.name_variable = tk.StringVar()
        self.food_category = tk.StringVar()
        
        # Widgits
        if view_else_create:
            tk.Label(self, text="View Recipe").grid(row=0, column= 0)
        else:
            tk.Label(self, text="Create Recipe").grid(row=0, column= 0)

        self.show_hidden_check_button = tk.Checkbutton(self, text="Hide Recipe", variable=self.show_hidden)
        self.show_hidden_check_button.grid(row=1, column=0)

        self.name_label = tk.Label(self, text="Name")
        self.name_label.grid(row=2, column=0)

        self.name_entry = tk.Entry(self, textvariable=self.name_variable)
        self.name_entry.grid(row = 3, column=0)

        self.category_label = tk.Label(self, text="<Category Name>")
        self.category_label.grid(row=4, column=0)
        
        self.category_combo_box = ttk.Combobox(self, textvariable=self.food_category)
        self.category_combo_box.grid(row=5, column=0)
        
        #################################################################################################
        ###################################### Ingredient controls ######################################
        #################################################################################################
        # variables
        self.ingredient = Ingredient()
        self.ingredients = []
        self.ingredients_to_delete = []
        self.amount_name_var = tk.StringVar()
        self.ingredient_name_var = tk.StringVar()

        # Widgits
        self.ingredient_control_frame = tk.Frame(self)
        self.ingredient_control_frame.grid(row=6, column=0)
        
        tk.Label(self.ingredient_control_frame, text="Ingredient List").grid(row=0, column= 0, columnspan=4)
        
        tk.Label(self.ingredient_control_frame, text="Ingredient").grid(row=1, column=0)
        tk.Label(self.ingredient_control_frame, text="Amount").grid(row=1, column=1)
        
        self.ingredient_name_entry = tk.Entry(self.ingredient_control_frame, textvariable=self.ingredient_name_var)
        self.ingredient_name_entry.grid(row=2, column=0)
        
        self.amount_name_entry = tk.Entry(self.ingredient_control_frame, textvariable=self.amount_name_var)
        self.amount_name_entry.grid(row=2, column=1)
        
        self.create_ingredient_button = tk.Button(self.ingredient_control_frame, text="Add Ingredient", command=self.save_ingredient)
        self.create_ingredient_button.grid(row=2, column=2)

        self.ingredient_list_box = tk.Listbox(self.ingredient_control_frame, height=10)
        self.ingredient_list_box.grid(row=3, column=0, columnspan=4)

        ## sub controls
        self.sub_ingredient_control_frame = tk.Frame(self)
        self.sub_ingredient_control_frame.grid(row=7, column=0)

        self.edit_ingredient_button = tk.Button(self.sub_ingredient_control_frame, text="Edit", command=self.edit_ingredient)
        self.edit_ingredient_button.grid(row=0, column=0)

        self.deselect_ingredient_button = tk.Button(self.sub_ingredient_control_frame, text="Deselect", command=self.deselect_ingredient)
        self.deselect_ingredient_button.grid(row=0, column=1)

        self.delete_ingredient_button = tk.Button(self.sub_ingredient_control_frame, text="Delete", command=self.delete_ingredient)
        self.delete_ingredient_button.grid(row=0, column=2)
        #################################################################################################
        ###################################### Ingredient controls ######################################
        #################################################################################################

        tk.Label(self, text="Description").grid(row=9, column= 0)
        self.description_text = tk.Text(self, width=40, height=10)
        self.description_text.grid(row=10, column=0)

        tk.Label(self, text="Instructions").grid(row=11, column= 0)
        self.instruction_text = tk.Text(self, width=40, height=10)
        self.instruction_text.grid(row=12, column=0)

        ##########
        # Footer
        ##########
        self.control_frame = tk.Frame(self)
        self.control_frame.grid(row=13)

        button_text = ""
        if view_else_create:
            button_text= "Update"
        else:
            button_text= "Create"
        self.update_button = tk.Button(self.control_frame, text=button_text, command= self.save_recipe)
        self.update_button.grid(row= 0, column=0)

        self.back_button = tk.Button(self.control_frame, text="Back", command=lambda: controller.open_frame("recipe index"))
        self.back_button.grid(row= 0, column=1)
        ##########
        # Footer #
        ##########
    

    def get_food_categories(self):
        '''
        Grabs all of the categories from the database then creates a list of category names and and creates a dictionary of using the name of the category
        and the id of the category.
        {
        "Name of Category" : 1
        }
        '''
        connection : SqliteConnecter = self.controller.get_connector()
        connection.c.execute("""SELECT * FROM food_categories;""")
        list_of_food_categories = connection.c.fetchall()

        list_of_category_names = []
        dictionary_of_categories = {}
        for category in list_of_food_categories:
            list_of_category_names.append(category[1])
            dictionary_of_categories[category[1]] = FoodCategory().assign_by_array(category)
        
        self.category_combo_box["values"] = list_of_category_names
        self.category_dictionary = dictionary_of_categories
        self.food_category.set("")


    def set_new(self):
        '''
        Resets the screen.
        '''
        self.recipe = Recipe()
        self.show_hidden.set(False)
        self.name_variable.set("")
        self.category_dictionary = {}

        self.get_food_categories()
        
        self.ingredient = Ingredient()
        self.ingredients = []
        self.ingredients_to_delete = []
        self.ingredient_name_var.set("")
        self.amount_name_var.set("")
        self.ingredient_list_box.delete(0, 'end')

        self.description_text.delete(0.0, 'end')
        self.instruction_text.delete(0.0, 'end')

        self.ingredient_list_box.select_clear(0, 'end')


    def set_recipe(self, recipe:Recipe):
        '''
        sets the recipe screen to the selected recipe form the recipe index menu.
        '''
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
        category  = connection.c.fetchone()
        print(category)
        food_category = FoodCategory().assign_by_array(category)
        self.food_category.set(food_category.name)

        # ingredients
        self.ingredient_name_var.set("")
        self.amount_name_var.set("")
        print("\nid: ", recipe.id)
        connection.c.execute(f"""SELECT * FROM ingredients
                             WHERE recipe_id = {recipe.id}""")
        list_of_ingredients = connection.c.fetchall()
        for ingredient in list_of_ingredients:
            text = ingredient[2] + " " + ingredient[3]
            self.ingredient_list_box.insert(ingredient[0], text)
            self.ingredients.append(Ingredient().assign_by_array(ingredient))
    

    def save_check(self):
        if len(self.name_variable.get().strip()):
            return "Please enter a name."
        elif len(self.food_category.get().strip()):
            return "Food category not selected."
        elif len(self.description_text.get('1.0', 'end').strip()):
            return "please enter a description."
        elif len(self.instruction_text.get('1.0', 'end').strip()):
            return "please enter a instruction."


    def save_recipe(self):
        '''
        Get's the user entered data and inserts it into the recipe
        '''
        connection : SqliteConnecter = self.controller.get_connector()

        self.recipe.name = self.name_variable.get()
        self.recipe.hidden = self.show_hidden.get()
        food_category = self.category_dictionary.get(self.food_category.get())
        print(self.category_dictionary, " ", self.food_category.get(), ' ', food_category, ' ', food_category.id)
        self.recipe.description = self.description_text.get('1.0', 'end')
        self.recipe.instructions = self.instruction_text.get('1.0', 'end')
        # print(self.save_check())

        print(self.recipe.to_sqlite())
        create_full_recipe(connection.c, food_category, self.recipe, self.ingredients)
        print(self.recipe.to_sqlite())

        for ingredient in self.ingredients_to_delete:
            connection.c.execute(f"""DELETE FROM ingredients
                                 WHERE ingredient_id = {ingredient.id}""")
        connection.conn.commit()
        self.controller.open_frame("recipe index")

    
    ### Ingredient controls
    def save_ingredient(self):
        '''
        saves the ingredient.
        '''
        self.ingredient.name = self.ingredient_name_var.get()
        self.ingredient.amount = self.amount_name_var.get()
        if self.ingredient.id == -1 and self.ingredient not in self.ingredients:
            self.ingredients.append(self.ingredient)
        self.update_ingredients()

    def edit_ingredient(self):
        '''
        Gets the selected ingredient and sets it to be editable
        '''
        if self.ingredient_list_box.curselection():
            selected_ingredient:Ingredient = self.ingredients[self.ingredient_list_box.curselection()[0]]
            self.ingredient_name_var.set(selected_ingredient.name)
            self.amount_name_var.set(selected_ingredient.amount)
            self.ingredient = selected_ingredient

    def deselect_ingredient(self):
        '''
        deselects the ingredient and deselecting the ingredient in the listbox
        '''
        self.ingredient = Ingredient()
        self.ingredient_name_var.set("")
        self.amount_name_var.set("")
        self.ingredient_list_box.select_clear(0, 'end')

    def delete_ingredient(self):
        '''
        Deletes the ingredient from the list
        '''
        if self.ingredient_list_box.curselection():
            self.ingredients_to_delete.append(self.ingredients.pop(self.ingredient_list_box.curselection()[0]))
            self.update_ingredients()
    
    
    def update_ingredients(self):
        '''
        updates the ingredient
        '''

        self.deselect_ingredient()
        self.ingredient_list_box.delete(0, 'end')
        for ingredient in self.ingredients:
                text = ingredient.name + " " + ingredient.amount
                self.ingredient_list_box.insert('end', text)