# doctest rectangle.py

import unittest

from models.rectangle import Rectangle
from io import StringIO
import sys

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

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        r = Rectangle(4, 6)
        r.display()

        sys.stdout = sys.__stdout__

        expected_output = "####\n" * 6
        self.assertEqual(captured_output.getvalue(), expected_output)

        captured_output = StringIO()
        sys.stdout = captured_output

        r = Rectangle(2, 2)
        r.display()

        sys.stdout = sys.__stdout__

        expected_output = "##\n" * 2
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
