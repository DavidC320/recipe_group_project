from .FoodCategoryObject import FoodCategory
from .IngredientObject import Ingredient
from .RecipeObject import Recipe
from .UserObject import User
from .SqliteConnector import SqliteConnecter

def create_full_recipe(c, category:FoodCategory, recipe:Recipe, ingredients:list[Ingredient]):
    # save food category
    c.execute(category.to_sqlite())
    category_id:int = 0
    if category.id == -1:  # checks if the category hasn't been added to the database
        c.execute("SELECT last_insert_rowid(); ")
        category_id = c.fetchone()[0]
    else: 
        category_id = category.id

    # Save recipe
    recipe.food_category = category_id
    c.execute(recipe.to_sqlite())
    recipe_id:int = 0
    if recipe.id == -1:
        c.execute("SELECT last_insert_rowid(); ")
        recipe_id = c.fetchone()[0]
    else:
        recipe_id = recipe.id

    for ingredient in ingredients:
        ingredient.recipe_id = recipe_id
        c.execute(ingredient.to_sqlite())

