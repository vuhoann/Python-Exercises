# Dragon Ball 
Nguyen Vu Hoang

---
## Game idea

This game idea is inspired by Dragon Ball.
There are 7 Dragon Balls (DB) in different locations, and the player has to find and collect all 7 DB to win.
The gameplay has the following flow:
In the beginning, the player has 3 lives, each life has 10 HP, the player starts in Kame House.
The player can choose go north, south, west or east. Everytime he/she moves to another location, he/she randomly gains or loses between -3 and +1 his/her HP (facing enemies or finding food). When the player goes to the location that has DB, he/she can see and choose to collecte it. When s DB is collected, the player receives 1-4 HP (permanently added until the game is over) 
When HP = 0, the player dies (loses 1 life) and return to the starting location (Kame House), but his/her inventory does not change. Afer 3 lives are lost, the game is over.

---
## Structure

The project is split into separate modules:

project/
|__main.py                  # maincode: game loop , functions
|__classes/
|          |__player.py     # Player class
|          |__item.py       # Item class
|          |__room.py       # Room class
|__readme.md                # Documentation
|__file_handling.py         # To handle the game save/ load
|__save.json                # Write/store the players information

---
## Player actions
collect - collect DB if the player see it
go north/ south/ west or east - move to a different location to find DB
quit - enter lopeta to quit the game




