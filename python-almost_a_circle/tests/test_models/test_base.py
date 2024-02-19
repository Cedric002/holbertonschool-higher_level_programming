# doctest base.py

import unittest

class TestBase(unittest.TestCase):

    def test_base_constructor(self):
        base_instance = Base(1)
        self.assertEqual(base_instance.id, 1)

        base_instance = Base()
        self.assertEqual(base_instance.id, 2)

        base_instance = Base()
        self.assertEqual(base_instance.id, 3)

if __name__ == '__main__':
    unittest.main()
