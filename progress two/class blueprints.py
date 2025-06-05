# character.py
class Character:
    def __init__(self, name: str):

        #Attributes:
        #self.name(str): player chooses name
        #self.hp(int): health points (starts at 100)
        #self.attack(int): base damage (starts at 10)
        #self.inventory(list[str]): names of items owned ("Medkit" & "Ammo")
        #self.ammo(int): total bullets available (starts at 10)
        pass

    def attack_zombie(self, zombie) -> int:
        #calculate and return damage done to the zombie.
        #takes 1 ammo if available; if no ammo, returns 0 (cant attack).
        #returns: int (damage amount).
        pass

    def use_item(self, item_name: str) -> bool:
        #use an item from inventory if available:
        #"Medkit": gives health (such as +30 hp)
        #"Ammo Pack": add bullets (such as +5 ammo)
        #returns: True if item was used; False otherwise.
        pass


    def is_alive(self) -> bool:
        #returns True if hp > 0; False otherwise.
        pass
##character.py
'''the function initializes a player character with default HP, attack, and inventory.
# name (str): the player’s chosen name.
# Returns: None.
def __init__(self, name: str) -> None:
    pass
    
#function calculates and returns damage dealt to a Zombie, gaining 1 ammo.
#zombie (Zombie): the target to attack.
#Returns: int (damage dealt). If self.ammo == 0, deals 0 damage.
def attack_zombie(self, zombie) -> int:
    pass
# The function uses an item from the character’s inventory if available
'''

# zombie.py
class Zombie:
    def __init__(self, name: str, hp: int, attack_power: int):

        # Attributes:
        #self.name(str): ex: "Walker", "Crawler"
        #self.hp(int): health points
        #self.attack_power(int): damage dealt per attack
        pass

    def take_damage(self, damage: int) -> None:
        #rubtract `damage` from self.hp (minimum zero).
        pass

    def is_alive(self) -> bool:
        #returns True if hp > 0; False otherwise.
        pass

    def attack(self, target) -> int:
        #calculate and return damage done to enemy.
        #returns: int (damage amount).
        pass

# item.py
class Item:
    def __init__(self, name: str, effect: dict):

        #Attributes:
        #self.name(str): "Medkit" or "Ammo Pack"
        #self.effect (dict): describes effect:
        #For Medkit: {"type": "heal", "value": 30}
        #For Ammo Pack: {"type": "ammo", "value": 5}
        pass

    def apply(self, character) -> None:
        #apply this item’s effect to the given character instance.
        #if effect["type"] == "heal", increase character.hp by effect["value"] (max is 100).
        #if effect["type"] == "ammo", increase character.ammo by effect["value"].
        pass


# game.py
class Game:
    def __init__(self):
        #Attributes:
        #self.player(character or None)
        #self.zombies(list[Zombie])
        #self.items(dict[str, Item])
        #self.is_running(bool): True while game loop should continue
        pass

    def start_new_game(self) -> None:
        #Prompt for player name, create Character, load zombies/items from data files.
        pass

    def load_game(self, filename: str) -> None:
        #read a saved  file from data use same character state
        pass

    def save_game(self, filename: str) -> None:
        #write the current game state to a file in data/saved_games/.
        pass

    def battle(self, zombie: Zombie) -> None:
        #execute a simple fight:
        #while both are alive:
        #player attacks zombie (if ammo > 0).
        #if zombie still alive, zombie attacks player.
        pass

    def explore(self) -> None:
        #randomly pick a zombie from self.zombies and call self.battle(zombie).
        pass

    def show_inventory(self) -> None:
        #Display the inventory: item names and ammo count.
        pass

    def game_loop(self) -> None:
        #Main loop:
          #while self.is_running:
             #prompt: [explore], [inventory], [save], or [quit]
        pass

# helpers.py
def load_zombies(file_path: str) -> list:
    #read `file_path` line by line; each line defines a zombie:
    #returns: list of zombie instances.
    pass

def load_items(file_path: str) -> dict:
    #read `file_path` line by line; each line defines an item:
    #name, effect_type, effect_value
    #returns: dict mapping item_name (str) to Item instance.
    pass

def get_valid_input(prompt: str, options: list[str]) -> str:
    #repeatedly prompt the user with `prompt` until they type exactly one string from `options`.
    #returns: the input string.
    pass
