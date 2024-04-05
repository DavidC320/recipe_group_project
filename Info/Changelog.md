# Changelog

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
