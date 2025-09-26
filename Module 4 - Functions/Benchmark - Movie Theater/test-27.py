import unittest
from unittest.mock import patch
from main import *


class TestMovieTheater(unittest.TestCase):

    def test_calculate_total(self):
        self.assertEqual(calculate_total(1), 7.50)
        self.assertEqual(calculate_total(3), 22.50)
        self.assertAlmostEqual(calculate_total(0), 0.00)

    @patch('builtins.input', side_effect=["Demon Slayer The Movie"])
    def test_get_movie_choice_valid(self, mock_input):
        result = get_movie_choice(MOVIES)
        self.assertEqual(result, "Demon Slayer The Movie")

    @patch('builtins.input', side_effect=["Invalid Movie", "Godzilla vs. Kong"])
    def test_get_movie_choice_retry(self, mock_input):
        result = get_movie_choice(MOVIES)
        self.assertEqual(result, "Godzilla vs. Kong")

    @patch('builtins.input', side_effect=["7:10 PM"])
    def test_get_show_time_valid(self, mock_input):
        result = get_show_time("Demon Slayer The Movie", ["4:05 PM", "7:10 PM"])
        self.assertEqual(result, "7:10 PM")

    @patch('builtins.input', side_effect=["5:00 PM", "4:35 PM"])
    def test_get_show_time_retry(self, mock_input):
        result = get_show_time("Godzilla vs. Kong", ["4:35 PM", "7:30 PM"])
        self.assertEqual(result, "4:35 PM")

    @patch('builtins.input', side_effect=["3"])
    def test_get_ticket_quantity_valid(self, mock_input):
        result = get_ticket_quantity()
        self.assertEqual(result, 3)

    @patch('builtins.input', side_effect=["0", "-1", "abc", "2"])
    def test_get_ticket_quantity_retry(self, mock_input):
        result = get_ticket_quantity()
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
