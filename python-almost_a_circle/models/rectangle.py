#!/usr/bin/python3
"""
Define a class Rectangle.
Update: adding the public method def area(self):
returns the area value of the Rectangle instance.
Update: adding the public method def display(self): prints Rectangle instance
with the character '#'.
Update: overriding the __str__ method so that it
returns [Rectangle] (<id>) <x>/<y> - <width>/<height>.
Update: improving the public method def display(self): print Rectangle instance
with the character '#' by taking care of x and y.
"""


from .base import Base


class Rectangle(Base):
    """
    Classe Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def area(self):
        """
        Public method that returns the area value of the Rectangle instance
        """
        return self.width * self.height

    def display(self):
        """
        Public that prints the character # by taking care of x and y
        """
        print(' ' * self.x, end='')
        for _ in range(self.height):
            print("#" * self.width)
        print()

    def __str__(self):
        """
        Overriding the __str__ method for returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
