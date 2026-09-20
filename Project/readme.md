# Name of the game
Nguyen Vu Hoang

30-08: Project assignment 1
-Create a folder project for the game. 
-Create a program that asks for the player's name and age.

06-09: Project assignment 2
-Updated the program to check age requirements: if the user's age is under 12, the program informs them that they do not meet the minimum age requirement. Otherwise, the program greets the user and displays the main menu.
-Create a loop menu and add a few commands. After a command, display the menu again until the user enters "lopeta".

13-09: Project assignment 3
-Modify the main menu, now the user can add items (they can select a weapon, armor, potion or accessory), print the items list, remove an item or check items amount .
-Create a function for each main menu option: add, show, remove and check function.

20-09: Project assignment 4
-Create new classes in gameclasses.py file.
+Class Player includes player name, list of items and their current location. Class player also includes move and collect item method.
+Class Item includes its name and weight.
+Class Room includes its name and possibly an item.
-Updated the main menu loop, allowing the player to collect an item in the current room, move to another room, check their inventory or quit. 
-When the program starts, a player and a few items(weapon, armor, potion, ring) and rooms(great_hall, chamber, dungeon, armoury, chapel) are created. All rooms contain an item except the chamber room. The player starts in the great hall.
+When the player collects an item in the room, the item will be removed from the room. 
+When the player chooses to move to another room, a room selection menu is displayed by the move function.
