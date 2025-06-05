# character.py (inside Character.__init__)
self.inventory: list[str] = []
#holds names of items the player has (["Medkit", "Ammo Pack"]).

# game.py (inside Game.__init__)
self.zombies: list[Zombie] = []
#populated at game start- load_zombies("data/zombies.txt").
#used in Game.explore() to pick a random Zombie.

#helper.py (for main menu input)
menu_options: list[str] = ["explore", "inventory", "save", "quit"]
#passed to get_valid_input() when showing the main action prompt.
