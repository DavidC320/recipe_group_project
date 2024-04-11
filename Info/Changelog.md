# Changelog

## 2.2.1

* The SQLite load test food category select statement has been changed to food_categories to match the new table name
* All files that had the Food_Category object name has been changed to FoodCategory to match the new object name
* assign_by_array has been added to the Base Table Object to make loading recipes from SQLite databases easier
  * All Children of the base class now uses assign_by_array

## 2.1.0

* Created a test to demonstrate the on open function of the child frame class

## 2.0.1

* changed the default value for name in the food category object from "Null" to "null"

## 2.0.0

* Created the Base Table object
  * Created insert & update functions
  * Created to array function
  * All Table objects inherit from the Base Table
  * All Tables now use the insert & update functions instead of to_sqlite
* User admin & Recipe hidden now use integers instead of booleans to keep parity between python and SQLite statements
* Created __init__ file in the Tkinter Objects directory
* Added Doc strings to the Controller Main Object
  * The open_frame function now checks if the current frame can be closed
* Added Doc strings into the child frame Object
  * on open has been split into can_open & on_close functions
* Updated the record test to save records so we can have test records for the load test
* Created the load test

## 1.1.1

* Create the User table.
* User table added to Table Object __init__
* User test now available in both the table and record test.

## 1.1.0

* Created a SQlite Record Test to view issues that could come up.
* Created an init file to turn the Table directory into a module.
  * created a method that can update a recipe without worrying about order called create_full_recipe.
* Bugs
  * All tables id check has been changed to self.id due to conflicts with another variable.
  * The insert command for all tables has had the self.id removed so that -1 can't be an id and to allow auto increment.
* The Recipe book as had many changes
  * The self.id variable had a bug where the self.id wasn't assigned "self.id : id" -> "self.id : int = id"
  * The self.hidden variable has been added.

## 1.0.0

* Created Frame Controller Object
* Created Frame child object
* Created a test file for the frame controller and child.

## 0.1.0

* Moved all of the table objects into the TableObjects directory
* Create a SQLite create table Test - Successful

## 0.0.4

* Create Table Objects (Needs Testing)
  * Food Category
  * Recipes
  * Ingredients
* Created Child Frame Objects (Unfinished)
