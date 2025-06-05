# tests/test_item.py
# Author: Max and Jarek
# Unit tests for items.py

import unittest
from items import Item
from character import Character


class TestItem(unittest.TestCase):
    def setUp(self) -> None:
        self.char = Character("MAX")

    def test_apply_heal(self):
        """test that a Medkit restores HP up to max."""
        medkit = Item("Medkit", "heal", 30)
        self.char.hp = 50
        medkit.apply(self.char)
        self.assertEqual(self.char.hp, 80)

    def test_apply_heal_cap(self):
        """test that heal does not exceed max_hp."""
        medkit = Item("Medkit", "heal", 30)
        self.char.hp = 90
        medkit.apply(self.char)
        self.assertEqual(self.char.hp, 100)

    def test_apply_ammo(self):
        """test that an Ammo Pack adds bullets."""
        ammo_item = Item("Ammo Pack", "ammo", 5)
        self.char.ammo = 2
        ammo_item.apply(self.char)
        self.assertEqual(self.char.ammo, 7)

    def test_no_effect_for_invalid_type(self):
        """Test that invalid effect_type does nothing."""
        noeffect = Item("noeffect", "invalid", 999)
        self.char.hp = 50
        self.char.ammo = 0
        noeffect.apply(self.char)
        self.assertEqual(self.char.hp, 50)
        self.assertEqual(self.char.ammo, 0)


if __name__ == "__main__":
    unittest.main()

