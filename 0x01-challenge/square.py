#!/usr/bin/python3
""" Square class """


class Square():
    """ Square class """
    width = 0

    def __init__(self, *args, **kwargs):
        """ Constructor """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Perimeter of the square """
        return (self.width * 4)

    def __str__(self):
        """ Print the square """
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
