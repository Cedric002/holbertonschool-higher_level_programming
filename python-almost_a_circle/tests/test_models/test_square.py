# doctest square.py

import unittest

from models.square import Square

class TestSquare(unittest.TestCase):
    def test_size_getter_and_setter(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        s.size = 10
        self.assertEqual(s.size, 10)
        with self.assertRaises(Exception):
            s.size = "9"

if __name__ == '__main__':
    unittest.main()
