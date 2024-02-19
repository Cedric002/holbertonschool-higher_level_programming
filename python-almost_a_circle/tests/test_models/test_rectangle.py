# doctest rectangle.py

import unittest

from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(5, 10, 1, 2, 'rectangle')

    def test_width(self):
        self.assertEqual(self.rectangle.width, 5)
        self.rectangle.width = 15
        self.assertEqual(self.rectangle.width, 15)

    def test_height(self):
        self.assertEqual(self.rectangle.height, 10)
        self.rectangle.height = 20
        self.assertEqual(self.rectangle.height, 20)

    def test_x(self):
        self.assertEqual(self.rectangle.x, 1)
        self.rectangle.x = 3
        self.assertEqual(self.rectangle.x, 3)

    def test_y(self):
        self.assertEqual(self.rectangle.y, 2)
        self.rectangle.y = 4
        self.assertEqual(self.rectangle.y, 4)

    def test_id(self):
        self.assertEqual(self.rectangle.id, 'rectangle')

if __name__ == '__main__':
    unittest.main()
