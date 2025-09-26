import unittest
from main import before_or_after, get_grade, get_gallons, calculate_total_cost

class TestGasPumpFunctions(unittest.TestCase):

    def test_before_or_after(self):
        self.assertEqual(before_or_after("before"), "before")
        self.assertEqual(before_or_after("AFTER"), "after")
        with self.assertRaises(ValueError):
            before_or_after("now")

    def test_get_grade(self):
        self.assertEqual(get_grade("Regular"), 2.50)
        self.assertEqual(get_grade("mid-grade"), 3.00)
        self.assertEqual(get_grade("PREMIUM"), 3.50)
        with self.assertRaises(ValueError):
            get_grade("diesel")

    def test_get_gallons(self):
        self.assertEqual(get_gallons(10.0, 2.50), 4.0)
        self.assertEqual(get_gallons(15.0, 3.00), 5.0)
        with self.assertRaises(ValueError):
            get_gallons(-5, 2.50)

    def test_calculate_total_cost(self):
        self.assertEqual(calculate_total_cost(5.0, 3.00), 15.00)
        self.assertEqual(calculate_total_cost(2.0, 3.50), 7.00)
        with self.assertRaises(ValueError):
            calculate_total_cost(0, 3.00)

if __name__ == '__main__':
    unittest.main()
