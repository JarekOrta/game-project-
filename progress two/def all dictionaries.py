# game.py (inside Game.__init__)
self.items: dict[str, Item] = {}
#key: item name (str)
#value:corresponding item value
#loads at start via load_items("data/items.txt").

# character.py (inside Character.__init__)
self.stats: dict[str, int] = {
    #"max_hp": 100,
    #"attack": 10
}
#Keys: stat names; Values: stat values used for HP cap and base attack.

# character.py (inventory counts alternative—pick one approach)
inventory_counts: dict[str, int] = {
    "Medkit": 1,
    "Ammo Pack": 1
}
#Key: item name; Value: how many of that item the player has.

#helper.py (temporary when loading a saved game)
saved_data: dict = {
    "player_name": "Alice",
    "hp": 70,
    "attack": 10,
    "inventory": ["Medkit", "Ammo Pack"],
    "ammo": 8,
    "stats": {"max_hp": 100, "attack": 10}
}
