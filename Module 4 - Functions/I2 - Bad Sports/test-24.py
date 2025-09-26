import unittest
from main import *

class TestIsOnTeam(unittest.TestCase):
    
    def test_in_team(self):
        self.assertTrue(is_on_team('Nick'))
        self.assertTrue(is_on_team('Carol'))
        self.assertTrue(is_on_team('Maureen'))
        
    def test_not_in_team(self):
        self.assertFalse(is_on_team('Alice'))
        self.assertFalse(is_on_team('Bob'))
        self.assertFalse(is_on_team('David'))
        
    def test_empty_string(self):
        self.assertFalse(is_on_team(''))
        
    def test_numbers(self):
        self.assertFalse(is_on_team(123))
        
    def test_none(self):
        self.assertFalse(is_on_team(None))

class TestRickShakes(unittest.TestCase):
    
    def test_carol_win(self):
        self.assertFalse(rick_shakes('Carol', True))
        
    def test_maureen_win(self):
        self.assertFalse(rick_shakes('Maureen', True))
        
    def test_nick_loss(self):
        self.assertFalse(rick_shakes('Nick', False))
        
    def test_other_cases(self):
        self.assertTrue(rick_shakes('Nick', True))
        self.assertTrue(rick_shakes('Carol', False))
        self.assertTrue(rick_shakes('Alice', False))
        self.assertTrue(rick_shakes('David', False))


class TestJohnShakes(unittest.TestCase):
    
    def test_nick_win(self):
        self.assertFalse(john_shakes('Nick', True))
        
    def test_carol_loss(self):
        self.assertFalse(john_shakes('Carol', False))
        
    def test_maureen_loss(self):
        self.assertFalse(john_shakes('Maureen', False))
        
    def test_other_cases(self):
        self.assertTrue(john_shakes('Nick', False))
        self.assertTrue(john_shakes('Carol', True))
        self.assertTrue(john_shakes('Alice', True))
        self.assertTrue(john_shakes('David', True))


class TestJaredShakes(unittest.TestCase):
    
    def test_nick(self):
        self.assertFalse(jared_shakes('Nick', True))
        self.assertFalse(jared_shakes('Nick', False))
        
    def test_other_cases(self):
        self.assertTrue(jared_shakes('Carol', True))
        self.assertTrue(jared_shakes('Maureen', False))
        self.assertTrue(jared_shakes('Alice', True))
        self.assertTrue(jared_shakes('David', False))

if __name__ == '__main__':
    unittest.main()