# game.py
# Author: Max and Jarek
# Description: Defines the Game class (main loop, battle, save/load)
import os
import random
from typing import Dict, Any, List
from character import Character
from zombie import Zombie
from items import Item
from helpers import load_zombies, load_items, get_valid_input, save_game_state, load_game_state


class Game:
    """
 all game logic: starting a new game, exploring, battling, saving/loading.
    """

    def __init__(self) -> None:
        """
initialize the Game:
- Prompt for [new] or [load].
- Load zombies/items from data files.
- create or reconstruct Character.
        """
        print("=== Welcome to our zombie game!! ===\n")
        choice = get_valid_input("Do you want to [new] game or [load] game? ", ["new", "load"])
        self.player: Character
        self.zombies: List[Zombie]
        self.items: Dict[str, Item]

        # Load zombies/items from data files
        self.zombies = load_zombies("zombies.txt")
        self.items = load_items("items.txt")

        if choice == "new":
            name = input("Enter survivor name!: ").strip() or "Survivor"
            self.player = Character(name)
        else:
            saves = os.listdir("saved_games")
            if not saves:
                print(">> No saved games found. Start a new game.\n")
                name = input("Enter surivor name!: ").strip() or "Survivor"
                self.player = Character(name)
            else:
                print(f"Saved game found: {saves}")
                filename = input("Enter filename to load: ").strip()
                state = load_game_state(filename)
                # Rebuild Character
                self.player = Character(state["name"])
                self.player.max_hp = state["max_hp"]
                self.player.hp = state["hp"]
                self.player.attack = state["attack"]
                self.player.ammo = state["ammo"]
                self.player.inventory = state["inventory"]

        print(f"\nHello, {self.player.name}. "
              f"HP: {self.player.hp}/{self.player.max_hp}, "
              f"Ammo: {self.player.ammo}, "
              f"Medkits: {self.player.inventory.get('Medkit',0)}, "
              f"Ammo Packs: {self.player.inventory.get('Ammo Pack',0)}.\n")

    def game_loop(self) -> None:
        """Main game loop:
while player is alive: prompt for [explore], [inventory], [status], [save], or [quit]
call corresponding choice.
        """
        while True:
            if not self.player.is_alive():
                print("\n>> You have been killed :( Game Over LOL.\n")
                break

            choice = get_valid_input("Choose an action: [explore], [inventory], [status], [save], [quit]  ",
                                      ["explore", "inventory", "status", "save", "quit"])
            if choice == "explore":
                self.explore()
            elif choice == "inventory":
                self.show_inventory()
            elif choice == "status":
                self.show_status()
            elif choice == "save":
                self.save_game()
            elif choice == "quit":
                print("\n>> You chose to quit. bye!\n")
                break

    def explore(self) -> None:
        """
        Randomly select a zombie and enter battle.
        """
        zombie_template = random.choice(self.zombies)
        enemy = Zombie(zombie_template.name,
                       zombie_template.hp,
                       zombie_template.attack_power)
        print(f"\n>> A {enemy.name} appeared! Get ready to fight!\n")
        self.battle(enemy)

    def battle(self, zombie: Zombie) -> None:
        """execute a turn-based fight between the player and zombie
in each turn:
Display both HP.
Prompt player for [attack], [use item], or [run].
run player action, then zombie’s turn if still alive.
after zombie is defeated, award loot- post_battle_loot().
        """
        while zombie.is_alive() and self.player.is_alive():
            print(f"--- BATTLE ---\n"
                  f"{self.player.name}: HP {self.player.hp}/{self.player.max_hp}, Ammo {self.player.ammo}\n"
                  f"{zombie.name}: HP {zombie.hp}\n")
            action = get_valid_input("Actions: [attack], [use item], [run]  ",
                                     ["attack", "use item", "run"])

            if action == "attack":
                damage = self.player.attack_zombie(zombie)
                if damage > 0:
                    zombie.take_damage(damage)
                    print(f">> You shot the {zombie.name} for {damage} damage.")
                else:
                    print(">> No ammo! Can't attack.Sucks!!")

                if not zombie.is_alive():
                    print(f"\n*** You defeated the {zombie.name}! ***")
                    self.post_battle_loot()
                    return

                # Zombie’s turn
                z_damage = zombie.attack(self.player)
                self.player.hp = max(self.player.hp - z_damage, 0)
                print(f">> The {zombie.name} hit you for {z_damage} damage.\n")

            elif action == "use item":
                self.show_inventory()
                choice = get_valid_input("Use [Medkit] or [Ammo Pack]?  ", ["medkit", "ammo pack"])
                used = self.player.use_item(choice.title())
                if used:
                    print(f">> You used a {choice.title()}.")
                else:
                    print(">> You don’t have that item.")

                # Zombie attacks after you use or fail to use an item
                if zombie.is_alive():
                    z_damage = zombie.attack(self.player)
                    self.player.hp = max(self.player.hp - z_damage, 0)
                    print(f">> The {zombie.name} hits you for {z_damage} damage.\n")

            elif action == "run":
                if random.random() < 0.5:
                    print(f">> You tried to run. but the {zombie.name} didn't give up! it's Chasing you")
                    z_damage = zombie.attack(self.player)
                    self.player.hp = max(self.player.hp - z_damage, 0)
                    print(f">> You took {z_damage} damage while running.\n")
                    if not self.player.is_alive():
                        return
                else:
                    print(f">> You successfully ran from the {zombie.name}!\n")
                    return

    def post_battle_loot(self) -> None:
        """ after defeating a zombie, randomly grant loot:
40% chance for a Medkit
40% chance for an Ammo Pack
20% chance for nothing
        """
        roll = random.random()
        if roll < 0.4:
            self.player.inventory["Medkit"] = self.player.inventory.get("Medkit", 0) + 1
            print(">> The zombie dropped a Medkit! You pick it up.")
        elif roll < 0.8:
            self.player.inventory["Ammo Pack"] = self.player.inventory.get("Ammo Pack", 0) + 1
            print(">> The zombie dropped an Ammo Pack! You pick it up.")
        else:
            print(">> The zombie dropped nothing. Bummer")
        print()

    def show_inventory(self) -> None:
        """
        Display current inventory counts and ammo.
        """
        print("\n--- Inventory ---")
        print(f"Medkits   : {self.player.inventory.get('Medkit', 0)}")
        print(f"Ammo Packs: {self.player.inventory.get('Ammo Pack', 0)}")
        print(f"Ammo      : {self.player.ammo}")
        print("-----------------\n")

    def show_status(self) -> None:
        """
        Display current HP and ammo count.
        """
        print("\n--- Status ---")
        print(f"Name : {self.player.name}")
        print(f"HP   : {self.player.hp}/{self.player.max_hp}")
        print(f"Ammo : {self.player.ammo}")
        print("---------------\n")

    def save_game(self) -> None:
        """
        Prompt for a save filename and write current game state to JSON.
        """
        filename = input("Enter a name for your save file (example: my_game.json): ").strip()
        state: Dict[str, Any] = {
            "name": self.player.name,
            "max_hp": self.player.max_hp,
            "hp": self.player.hp,
            "attack": self.player.attack,
            "ammo": self.player.ammo,
            "inventory": self.player.inventory
        }
        save_game_state(state, filename)
        print(f">> Game saved as {filename}.\n")
