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

        r1 = Rectangle(2, 3, 2, 2)
        r1.display()

        sys.stdout = sys.__stdout__

        expected_output = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

        captured_output = StringIO()
        sys.stdout = captured_output

        r2 = Rectangle(3, 2, 1, 0)
        r2.display()

        sys.stdout = sys.__stdout__

        expected_output = " ###\n ###\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        expected_output = "[Rectangle] ({}) 1/0 - 5/5".format(r2.id)
        self.assertEqual(str(r2), expected_output)

    def setUp(self):
        self.r1 = Rectangle(10, 10, 10, 10)

    def test_update_args(self):
        self.r1.update(89, 2, 3, 4, 5)
        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.x, 4)
        self.assertEqual(self.r1.y, 5)

    def test_update_kwargs(self):
        self.r1.update(id=89, width=2, height=3, x=4, y=5)
        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.x, 4)
        self.assertEqual(self.r1.y, 5)

     def test_to_dictionary(self):
	    return ('id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y)

if __name__ == '__main__':
    unittest.main()
