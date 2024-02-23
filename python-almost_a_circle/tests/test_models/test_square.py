# doctest square.py

import unittest

from models.square import Square

class TestSquare(unittest.TestCase):
    def test_update(self):
        s = Square(5)
        s.update(1, 10, 2, 3)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

        s.update(x=4, y=5, id=2)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)
        self.assertEqual(s.id, 2)

        s.update(size=6, id=3)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.id, 3)

    def test_to_dictionary(self):
	    return ('id': self.id, 'size': self.__size,
                'x': self.__x, 'y': self.__y)

if __name__ == '__main__':
    unittest.main()
