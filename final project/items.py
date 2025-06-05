# item.py
# Author: Max and Jarek
# Description: Defines the Item class

from typing import Any


class Item:
    """
Represents items (Medkit or Ammo Pack)
Attributes:
name (str): Item’s name.
effect_type (str): "heal" or "ammo"
value (int): amount healed or ammo given
    """

    def __init__(self, name: str, effect_type: str, value: int) -> None:
        """
initialize a new Item
Values:
name (str): Item name
effect_type (str): "heal" or "ammo"
value (int): amount of effect
Returns:None
        """
        self.name = name
        self.effect_type = effect_type
        self.value = value

    def apply(self, character: Any) -> None:
        """apply this item’s effect to the Character
values: character (Character): the character who uses the item
Returns:None
        """
        if self.effect_type == "heal":
            character.hp = min(character.hp + self.value, character.max_hp)
        elif self.effect_type == "ammo":
            character.ammo += self.value
