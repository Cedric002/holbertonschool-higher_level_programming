# doctest square.py

import unittest

from models.square import Square

class TestSquare(unittest.TestCase):
    def test_init(self):
        s = Square(5, 3, 4, 'S01')
        self.assertEqual(s.id, 'S01')
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_str(self):
        s = Square(5, 3, 4, 'S01')
        self.assertEqual(str(s), "[Square] (S01) 3/4 - 5")

if __name__ == '__main__':
    unittest.main()
