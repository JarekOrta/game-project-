# tests/test_zombie.py
# Author: Max and Jarek
# Unit tests for zombie.py

import unittest
from zombie import Zombie


class TestZombie(unittest.TestCase):
    def setUp(self) -> None:
        self.zombie = Zombie("Walker", 50, 8)

    def test_initial_attributes(self):
        #test that a new Zombie has correct default stats.
        self.assertEqual(self.zombie.name, "Walker")
        self.assertEqual(self.zombie.hp, 50)
        self.assertEqual(self.zombie.attack_power, 8)

    def test_take_damage(self):
        #test that take_damage reduces HP appropriately and floors at 0.
        self.zombie.take_damage(10)
        self.assertEqual(self.zombie.hp, 40)
        self.zombie.take_damage(50)
        self.assertEqual(self.zombie.hp, 0)

    def test_is_alive(self):
        #test is_alive returns correct boolean
        self.assertTrue(self.zombie.is_alive())
        self.zombie.hp = 0
        self.assertFalse(self.zombie.is_alive())

    def test_attack_damage(self):
        #test attack() returns correct damage value
        damage = self.zombie.attack(None)
        self.assertEqual(damage, 8)


if __name__ == "__main__":
    unittest.main()
