#!/usr/bin/python3
"""
unittest Base class
"""

import unittest
from base import Base

class TestBase(unittest.TestCase):
    """
    test from Base class
    """

    def test_base_with_id(self):
        base_instance = Base(id=5)
        self.assertEqual(base_instance.id, 5)

    def test_base_without_id(self):
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)

    def test_base_multiple_instances(self):
        base_instance1 = Base()
        base_instance2 = Base()
        self.assertEqual(base_instance1.id, 1)
        self.assertEqual(base_instance2.id, 2)

if __name__ == '__main__':
    unittest.main()
