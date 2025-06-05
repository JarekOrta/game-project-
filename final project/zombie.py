# zombie.py
# Author: Max and Jarek
# Description: Defines the Zombie class.
from typing import Any


class Zombie:
#Represents a zombie enemy in the game.
# Attributes:
# name (str): Zombie type.
# hp (int): Current health points.
# attack_power (int): Damage dealt per attack.

    def __init__(self, name: str, hp: int, attack_power: int) -> None:
        """initialize a new Zombie.
values:name (str): Zombie’s name.
hp (int): Starting health points.
attack_power (int): base damage done per attack.
Returns:None
        """
        self.name  = name
        self.hp = hp
        self.attack_power = attack_power

    def take_damage(self, damage: int) -> None:
        """subtract damage from self.hp (floor at 0).
Value: damage (int): amount to subtract from hp.
Returns:None
        """
        self.hp = max(self.hp - damage, 0)

    def is_alive(self) -> bool:
        """ checks if zombie is  alive
Returns: bool: True if hp > 0; False if not.
        """
        return self.hp > 0

    def attack(self, target: Any) -> int:
        """ returns the damage the zombie does.
value: target (Any): The target being attacked (Character).
Returns: int: damage dealt (equal to self.attack_power).
        """
        return self.attack_power
