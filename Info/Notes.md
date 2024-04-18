# Notes

## issue - can't get the recipe index

Due to the insert of the listbox, I will need to create a dictionary or list to convert the indexes into the correct index.

## What to do

* Create files for database and password keys
* encrypt and decrypt database files
* create login information
* get the sqlite stuff done
* transfer data across frames.
* That's about it

## Screens

* Main menu
* Login

* update the create database to give keys

## Deconstruction 3

Major goals

* Create the UI
  * Main menu
  * Database initalizing
    * Create database screen
    * Load database screen
  * user screens
    * Create admin
    * login
    * create/edit user
    * user index
  * recipe Book
    * recipe index
    * view recipe
    * create/update recipe
* Create encrption and decreption for both user passwords and file
* Create a connection object for sqlite for easier asccess for other objects

## Notes on the Tkinter Test

The test had a few hiccups but works perfect

1. The frame holder needs all of the child frames in it in a grid pack that overlaps each other.
2. Lots of spelling errors when changing the frame due to incorrect frame names.

Other those issues it was a quick implementation.

## Notes of the Connection Test

1. Getting the table commands was incredibly annoy. Due to the files being in a different directory,  
I had to go to each of the files and add a period before the import to get it to work. I don't know  
why, but I will look for the reason.

2. The next issue was the circular imports of the files. This was because the connection test imported  
the Recipe Object and that imports the Ingredient Object which imports the Recipe Object again.  
The issue | Test -> Recipe <-> Ingredient |.  
To fix the issue I had to turn where the recipe object was used in and convert it into a integer  
variable.

3. The next set of issues where just syntax errors.
   1. It's "Create table if not exist <-Table Name->".
   2. Forgot a ",".
   3. Extra ",".
   4. Had a ";" before ")".

Here is some goals to achieve.

1. Complete separation of each object. This can only be done it the app allows it. By that I mean the app has to hold on to the data itself instead of the objects holding each other.
2. Base table object. This will streamline the creation of new table objects but this is extra.

## Oops

<https://stackoverflow.com/questions/531035/how-to-do-if-not-exists-in-sqlite>  
I didn't need the []...

## Save order

Food Category
Recipe
Ingredients