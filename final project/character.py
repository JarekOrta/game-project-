# character.py
# Author: Jarek And Max
# Description: defines the Character class for the zombie survival game

from typing import Dict


class Character:
    """Represents the player character in the zombie survival game.
Attributes:
name (str): the survivor name
max_hp (int): ,aximum health points
hp (int): current health points
attack (int): base damage done to zombie
level (int): Current level
ammo (int): bullets available
inventory (Dict[str, int]): Count of items ("Medkit", "Ammo Pack")"""

    def __init__(self, name: str) -> None:
        """Initialize a new Character
         Value:name (str): Survivor’s chosen name
         Returns: None
        """
        self.name = name
        self.max_hp = 100
        self.hp = self.max_hp
        self.attack = 10
        self.xp = 0
        self.ammo = 10
        self.inventory: Dict[str, int] = {"Medkit": 1, "Ammo Pack": 1}

    def attack_zombie(self, zombie) -> int:
        """ attempt to shoot a zombie. takes 1 bullet if available.
Value: zombie (Zombie): the target.
Returns: int: damage dealt (equal to self.attack) if ammo > 0, else 0.
        """
        if self.ammo > 0:
            self.ammo -= 1
            return self.attack
        else:
            return 0

    def use_item(self, item_name: str) -> bool:
        """use an item from inventory if available:
- "Medkit": restores 30 HP (max at max_hp)
- "Ammo Pack": adds 5 bullets
Values: item_name (str): name of the item to use ("Medkit" or "Ammo Pack")
Returns: bool: True if item was used; False if not
        """
        if item_name not in self.inventory or self.inventory[item_name] <= 0:
            return False

        if item_name == "Medkit":
            heal_amount = 30
            self.hp = min(self.hp + heal_amount, self.max_hp)
            self.inventory[item_name] -= 1
            return True

        elif item_name == "Ammo Pack":
            ammo_gain = 5
            self.ammo += ammo_gain
            self.inventory[item_name] -= 1
            return True

        else:
            return False


    def is_alive(self) -> bool:
        """check if character is still alive.
returns:bool: True if hp > 0; False otherwise
        """
        return self.hp > 0
