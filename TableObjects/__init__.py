from .FoodCategoryObject import FoodCategory
from .IngredientObject import Ingredient
from .RecipeObject import Recipe
from .UserObject import User
from .SqliteConnector import SqliteConnecter

def create_full_recipe(c, category:FoodCategory, recipe:Recipe, ingredients:list[Ingredient]):
    # save food category
    c.execute(category.to_sqlite())
    c.execute("SELECT last_insert_rowid(); ")
    category_id:int = c.fetchone()[0]

    # Save recipe
    recipe.food_category = category_id
    c.execute(recipe.to_sqlite())
    c.execute("SELECT last_insert_rowid(); ")
    recipe_id:int = c.fetchone()[0]

    for ingredient in ingredients:
        ingredient.recipe_id = recipe_id
        c.execute(ingredient.to_sqlite())

