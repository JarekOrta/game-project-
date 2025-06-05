# tests/test_character.py
# Author: Max and Jarek
# Unit tests for character.py

import unittest
from character import Character


class TestCharacter(unittest.TestCase):
    def setUp(self) -> None:
        self.char = Character("Tester")

    def test_initial_attributes(self):
        """test that a new character has correct default stats."""
        self.assertEqual(self.char.name, "max")
        self.assertEqual(self.char.max_hp, 100)
        self.assertEqual(self.char.hp, 100)
        self.assertEqual(self.char.attack, 10)
        self.assertEqual(self.char.ammo, 10)
        self.assertDictEqual(self.char.inventory, {"Medkit": 1, "Ammo Pack": 1})

    def test_attack_zombie_w_ammo(self):
        """test attack_zombie returns damage and takes ammo."""
        starting_ammo = self.char.ammo
        damage = self.char.attack_zombie(None)
        self.assertEqual(damage, 10)
        self.assertEqual(self.char.ammo, starting_ammo - 1)

    def test_attack_zombie_no_ammo(self):
        """test attack_zombie returns 0 when no ammo left."""
        self.char.ammo = 0
        damage = self.char.attack_zombie(None)
        self.assertEqual(damage, 0)
        self.assertEqual(self.char.ammo, 0)

    def test_use_item_medkit(self):
        """test using a Medkit restores HP up to max."""
        self.char.hp = 50
        used = self.char.use_item("Medkit")
        self.assertTrue(used)
        self.assertEqual(self.char.hp, 30)  # 50 + 30 = 80
        self.assertEqual(self.char.inventory["Medkit"], 0)

    def test_use_item_medkit_max(self):
        """test Medkit does not exceed max_hp."""
        self.char.hp = 90
        used = self.char.use_item("Medkit")
        self.assertTrue(used)
        self.assertEqual(self.char.hp, 100)
        self.assertEqual(self.char.inventory["Medkit"], 0)

    def test_use_item_ammo_pack(self):
        """test using an Ammo Pack increases ammo."""
        self.char.ammo = 2
        used = self.char.use_item("Ammo Pack")
        self.assertTrue(used)
        self.assertEqual(self.char.ammo, 7)  # 2 + 5 = 7
        self.assertEqual(self.char.inventory["Ammo Pack"], 0)

    def test_use_item_not_available(self):
        """test using a nonexistent or zero-count item fails."""
        self.char.inventory["Medkit"] = 0
        used = self.char.use_item("Medkit")
        self.assertFalse(used)

        used2 = self.char.use_item("Nonexistent")
        self.assertFalse(used2)

    def test_is_alive(self):
        """Test is_alive returns correct boolean."""
        self.char.hp = 0
        self.assertFalse(self.char.is_alive())
        self.char.hp = 10
        self.assertTrue(self.char.is_alive())


if __name__ == "__main__":
    unittest.main()
