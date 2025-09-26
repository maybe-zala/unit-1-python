import unittest

from main import *

class TestFunctions(unittest.TestCase):

    def test_say_hello(self):
        self.assertEqual(say_hello(), 'Hello World!')

    def test_hey_you(self):
        self.assertEqual(hey_you('Alice'), 'Hello Alice!')
        self.assertEqual(hey_you('Bob'), 'Hello Bob!')
        self.assertEqual(hey_you(''), 'Hello !')  # Testing with an empty name

    def test_age_in_2050(self):
        self.assertEqual(age_in_2050(2000), 50)
        self.assertEqual(age_in_2050(1990), 60)
        self.assertEqual(age_in_2050(1985), 65)

    def test_can_i_take_your_order(self):
        self.assertEqual(can_i_take_your_order(2, 1, 3), 13.5)
        self.assertEqual(can_i_take_your_order(0, 2, 1), 4.0)
        self.assertEqual(can_i_take_your_order(1, 0, 0), 4.5)
        self.assertEqual(can_i_take_your_order(0, 0, 0), 0.0)
        self.assertEqual(can_i_take_your_order(5, 2, 4), 29.5)

if __name__ == '__main__':
    unittest.main()