class MyClass:
    pass

print('MyClass == ', MyClass, 'type(MyClass) == ', type(MyClass), 'MyClass.__bases__ == ', MyClass.__bases__)

m = MyClass()
m.attr = '123'

print('m == ', m, 'type(m) == ', type(m), 'm.__class__ == ', m.__class__)
print('m is m == ', m is m)

n = MyClass()
print('m is n == ', m is n)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

list1.append(4)

print('list1 == ', list1)
print('list2 == ', list2)
print('list3 == ', list3)
print('list1 == list2 == ', list1 == list2)
print('list1 is list2 == ', list1 is list2)
print('list1 is list3 == ', list1 is list3)

print('------------------')

class Human:
    pass

h = Human()
h.name = 'John'
h.age = 42

def print_human(human):
    print('Human == ', Human)
    print('human.name == ', human.name, 'human.age == ', human.age)

print_human(h)

print('------------------')

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

    #string support
    def __str__(self):
        return f'<Point {self.x}, {self.y}>'

p = Point(2, 3)
p2 = Point(5, 7)


h = Human()
print('isinstance(p, Point) == ', isinstance(p, Point))
#check if isinstance Point OR Human
print('isinstance(p, (Point, Human) == ', isinstance(p, (Point, Human)))

print('p.x == ', p.x, 'p.y == ', p.y, 'p.attr == ', p.attr)
p.attr = 50
print('p.x == ', p.x, 'p.y == ', p.y, 'p.attr == ', p.attr)


print('p.add(p2) returns ', p.add(p2))
p3 = p + p2
print('p3 returns ', p3)
# equal p3 = p.__add__(p2)

p3 += Point(1, 2)
# equal p3 = p3.__iadd__(Point(1, 2))
print('p3 returns ', p3)






