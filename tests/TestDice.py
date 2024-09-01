import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.Dice import Dice

class TestDice(unittest.TestCase):
    def test_instance_created(self):
        dice = Dice(50)
        self.assertIsInstance(dice,Dice)

    def test_instance_not_created_too_much_dices(self):
        with self.assertRaises(Exception):
            dice = Dice(500)

    def test_throw_dice(self):
        dice = Dice(75)
        throw_result = dice.throw()
        self.assertTrue(1 <= throw_result <= 75)

if __name__ == '__main__':
    unittest.main()