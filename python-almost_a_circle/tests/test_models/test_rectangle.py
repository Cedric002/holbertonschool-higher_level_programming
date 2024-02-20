# doctest rectangle.py

import unittest

from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_setters(self):
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.width = "20"
        with self.assertRaises(ValueError):
            r.width = -10
        with self.assertRaises(TypeError):
            r.x = {}
        with self.assertRaises(ValueError):
            r.x = -5

if __name__ == '__main__':
    unittest.main()
