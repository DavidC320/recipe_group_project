# Notes

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