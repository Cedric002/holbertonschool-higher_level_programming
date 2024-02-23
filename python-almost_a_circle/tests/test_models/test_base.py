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

if __name__ == '__main__':
    unittest.main()
