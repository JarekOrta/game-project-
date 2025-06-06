# helpers.py
# Author: Max and Jarek
# Description: helper functions

import json
import random
from typing import List, Tuple, Dict, Any
from zombie import Zombie
from items import *
import os


def load_zombies(file_path: str) -> List[Zombie]:
#read a text file of zombie definitions and return a list of Zombie instances.
#File format (each line): name, hp, attack_power
#alues: file_path (str): Path to zombies.txt
#Returns: List[Zombie]: list of Zombie objects loaded from file.

    zombies: List[Zombie] = []
    with open(file_path, "r") as f:
        for line in f:
            stripped = line.strip()
            if not stripped:
                continue
            parts = [p.strip() for p in stripped.split(",")]
            name, hp_str, atk_str = parts
            hp, attack_power = int(hp_str), int(atk_str)
            zombies.append(Zombie(name, hp, attack_power))
    return zombies


def load_items(file_path: str) -> Dict[str, Item]:
#read a text file of item definitions and return a dictionary mapping item names to Item instances
#file format (each line):
#name, effect_type, value
#Values:
#file_path (str): Path to items.txt
#Returns:
#Dict[str, Item]: { item_name: Item(...) }

    items: Dict[str, Item] = {}
    with open(file_path, "r") as f:
        for line in f:
            stripped = line.strip()
            if not stripped:
                continue
            parts = [p.strip() for p in stripped.split(",")]
            name, effect_type, value_str = parts
            value = int(value_str)
            items[name] = Item(name, effect_type, value)
    return items


def get_valid_input(prompt: str, options: List[str]) -> str:
#prompt the user until they type one of the allowed options (case-insensitive)
#Values:
#prompt (str): the question to display
#options (List[str]): list of valid responses (all lowercase).
#returns:str: the valid lowercased response

    while True:
        response = input(prompt).strip().lower()
        if response in options:
            return response
        else:
            print(f">> Invalid input. Please choose from {options}.")


def save_game_state(state: Dict[str, Any], filename: str) -> None:
#Save the given game state dict to a JSON file under saved_games/."""
# Ensure the 'saved_games' folder exists
    os.makedirs("saved_games", exist_ok=True)

    # Write into saved_games/<filename>
    with open(f"saved_games/{filename}", "w") as f:
        json.dump(state, f, indent=4)

def load_game_state(filename: str) -> Dict[str, Any]:
#Load game state from a JSON file under saved_games/
    with open(f"saved_games/{filename}", "r") as f:
        return json.load(f)
