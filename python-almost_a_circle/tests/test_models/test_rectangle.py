# doctest rectangle.py

import unittest

from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        r = Rectangle(10,  2)
        self.assertEqual(r.width,  10)
        self.assertEqual(r.height,  2)
        self.assertEqual(r.x,  0)
        self.assertEqual(r.y,  0)

    def test_setters(self):
        r = Rectangle(10,  2)
        r.width =  20
        r.height =  4
        r.x =  5
        r.y =  6
        self.assertEqual(r.width,  20)
        self.assertEqual(r.height,  4)
        self.assertEqual(r.x,  5)
        self.assertEqual(r.y,  6)

if __name__ == '__main__':
    unittest.main()
