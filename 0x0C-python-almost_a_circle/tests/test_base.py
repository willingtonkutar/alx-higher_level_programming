import unittest
from base import *

class BaseTestCase(unittest.TestCase):
    def test_addition(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = subtract(5, 2)
        self.assertEqual(result, 3)

    def test_multiplication(self):
        result = multiply(4, 6)
        self.assertEqual(result, 24)

    def test_division(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()