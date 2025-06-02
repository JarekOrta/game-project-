# game-project-
Zombie Survivor 

Description:
a zombie survival game. The player explores a small town at night, 
battles zombies, finds supplies (ammo and medkits), and tries to survive until dawn.

files and roles:
  1. main.py — driver file. starting point to start or load the game.
  2. character.py — defines the Character class (player: hp, attack, inventory).
  3. zombie.py — defines the Zombie class (enemy hp, attack, xp_reward).
  4. item.py — defines the Item class (medkit and ammo).
  5. game.py — defines the Game class (main loop, exploring, battles, save/load).
  6. helpers.py — helper functions (input validation, file loading).
  7. data/
 zombies.txt — text file including zombie definitions.
 items.txt  — text file including item definitions.
saved_games/ — directory for saved‐game files.

Driver File:
main.py is the driver. with running python main.py, it will be used to launch the menu (start new game or load existing).

