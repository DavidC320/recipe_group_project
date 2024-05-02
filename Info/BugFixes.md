# Bug fixes

## Syntax

AA BB ERROR ##  

AA - Inital of location of error  
BB - Cause of Error  
ERROR - error type  
\## - id

## LSWSLOGIC04 - Login screen bringing the user to the start screen instead of the main menu

## Cause

The back button in the login screen brings the user back to the start instead of the main menu making it so that the user has to connect into the database.

## Solution

Changed the open frame in the login screen to 'main menu' instead of 'start'.

## VRAILOGIC03 - Editing an Ingredient will Sometimes add a Duplicate

### Cause

In the Add Ingredient function, when a new ingredient is added, the ingredient is given the id -1 as a placeholder. This is to check if it is in the database or not. if it is -1, it will be added into the list of ingredients made for the recipe but will not be saved into the database, at which it will be given a new id. This issue causes the program to add the recipe into the list even though it is already in the list due to the -1 id.

## Solution

Added a check if the Ingredient object is already inside of the list.

## RISELOGIC02 - The Search Would not work if the Show Hidden was Enabled

### Cause

The search was separating two select statements based off of if the user had enabled show hidden and if not, see if the user entered something into the search entry. Due to the separation, if the hidden was enabled, then it will never go to the search query.

### Solution

There is now a initial statement.

~~~ SQLITE
SELECT * FROM recipes
WHERE hidden = {1 if self.show_hidden.get() else 0}
~~~

This automatily addes the if hidden into the start of the search.
then it would add "AND name LIKE '{self.search_query.get()}%';"

~~~ SQLITE
SELECT * FROM recipes
WHERE hidden = {1 if self.show_hidden.get() else 0}
AND name LIKE '{self.search_query.get()}%'; <-- name search
~~~

Otherwise,  end the stament with ';'

~~~ SQLITE
SELECT * FROM recipes
WHERE hidden = {1 if self.show_hidden.get() else 0};
~~~

## VRCRVALUE01 - The Category won't Show or Incorrect Category will Show

### Cause

For the empty category slot, it was due to an invalid recipe id due to the "SELECT last_insert_rowid(); " statment grabbing the id of the last ingredient added. This also caused the incorrect category. The main reason is that the predesignated category wheren't fully tested in the create_full_recipe function in the Table Objects module.

### Solution

The Create Full Recipe function will now check if the category already has an id. This will go the same as the recipe.