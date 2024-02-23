#!/usr/bin/python3
"""
unittest Base class
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
    test from Base class
    """

    def test_id_assignment(self):
        base = Base(id=1)
        self.assertEqual(base.id, 1)

    def test_id_auto_increment(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")

        self.assertEqual(Base.to_json_string([]), "[]")

        dictionaries = [{"x": 2, "width": 10, "id": 12, "height": 7, "y": 8}]
        self.assertEqual(Base.to_json_string(dictionaries),
                '[{"x": 2, "width": 10, "id": 12, "height": 7, "y": 8}]')

    def test_save_to_file(self):
        r1 = Rectangle(10,  7,  2,  8)
        r2 = Rectangle(2,  4)
        Base.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertIn('{"id": 1, "x": 2, "y": 8, "width": 10,
                    "height": 7}', content)
            self.assertIn('{"id": 2, "x": 0, "y": 0, "width": 2,
                    "height": 4}', content)

if __name__ == '__main__':
    unittest.main()
