import unittest
import sys
import os
import random
from array import array

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.DiceCollection import DiceCollection
from src.Dice import Dice

class TestDiceCollection(unittest.TestCase):
    def test_instance_created(self):
        dc = DiceCollection()
        self.assertIsInstance(dc,DiceCollection)

    def test_instance_created_with_list(self):
        dc = DiceCollection([1,2,3,4,5])
        self.assertIsInstance(dc,DiceCollection)
    
    def test_instance_not_created_too_much_dices(self):
        with self.assertRaises(Exception):
            dc = DiceCollection([1,2,3,4,5,6])
    
    def test_append_dice(self):
        dc = DiceCollection()
        [dc.append_dice(Dice(random.randint(1,100))) for _ in range(4)]
        self.assertEqual(len(dc),4)

    def test_append_dice_error(self):
        dc = DiceCollection()
        with self.assertRaises(Exception):
            [dc.append_dice(Dice(random.randint(1,100))) for _ in range(6)]
    
    def test_throw_dice(self):
        dc = DiceCollection()
        [dc.append_dice(Dice(50)) for _ in range(4)]
        throw_result = dc.throw_dice(0)
        self.assertTrue(1 <= throw_result <= 50)
    
    def test_throw_dice_error(self):
        dc = DiceCollection()
        with self.assertRaises(Exception):
            dc.throw_dice(0)
    
    def test_last_100_throws(self):
        dc = DiceCollection()
        [dc.append_dice(Dice(50)) for _ in range(4)]
        throw_result_list = array('i',[dc.throw_dice(0) for _ in range(250)])
        last_100_throws = dc.last_100_throws()
        self.assertListEqual(list(throw_result_list[-100:]),list(last_100_throws))

if __name__ == '__main__':
    unittest.main()
