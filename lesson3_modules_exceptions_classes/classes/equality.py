import logging

class Point(object):

    attr = 42

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, point):
        if not isinstance(point, Point):
            raise TypeError('Please provide Point instance')
        return Point(self.x + point.x, self.y + point.y)

    # `+` support
    __add__ = add
    # equal
    #def __add__(self, other):
    #    return self.add(other)

    # `+=` support
    def __iadd__(self, other):
        if not isinstance(other, Point):
            raise TypeError('Please provide Point instance')
        self.x += other.x
        self.y += other.y
        return self

    # compare '=='
    def __eq__(self, other):
        print('Called __eq__')
        if not isinstance(other, Point):
            logging.warning('Please provide Point instance for comparsion')
            return False
            #raise TypeError('Please provide Point instance')
        self.x == other.x and self.y == other.y

    # compare '>, <, >=, <='
    def __gt__(self, other):
        print('Called __gt__')
        if not isinstance(other, Point):
            raise TypeError('Please provide Point instance')
        return self.x > other.x and self.y > other.y

    #string support
    def __str__(self):
        return f'<Point {self.x}, {self.y}>'

p1 = Point(1, 2)
p2 = Point(1, 2)
print('p1 == p2 ',p1 == p2)
print('p1 is p2 ',p1 is p2)

p3 = Point(2, 3)
p4 = Point(1, 2)
print('p3 > p4 ',p3 > p4)
print('p3 < p4 ',p3 < p4)