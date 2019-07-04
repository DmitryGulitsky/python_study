class Vehicle:
    speed = 0
    age = 0

    def move(self):
        return f'Moving with speed {self.speed}'

class Car(Vehicle):

    def __init__(self):
        self.speed = 10

    def move(self):
        s = super().move()
        print('Previous:', s)
        #return f'Driving car with speed {self.speed}'
        s += ' [it is a car]'
        return s

class Ship(Vehicle):

    def __init__(self):
        self.tubes = 3

    def sound(self):
        return f'Tu tu from {self.tubes} tubes'

class SportCar(Car):
    speed = 50

    def __init__(self):
        print('Current speed is', self.speed)
        super().__init__()
        print('And now current speed is', self.speed)
        self.speed = 70

class ECar(Car):
    charge = 50

    def state(self):
        return 'Needs charge' if self.charge < 10 else 'OK'

class PlaybackError(Exception):
    pass

class MorePlayErrors(PlaybackError):
    pass

class SportECar(SportCar, ECar):

    def play(self):
        print('Trying to play')
        raise PlaybackError

    def play2(self):
        raise MorePlayErrors

v = Vehicle()
car = Car()
ship = Ship()
s_car = SportCar()
e_car = ECar()
se_car = SportECar()

print('Car == ', Car, 'Car.__bases__ == ', Car.__bases__)
print('car.__class__ == ', car.__class__)
print('v.speed == ', v.speed)
print('car.speed == ', car.speed)
print('v.move() returns ', v.move())
print('car.move() returns ', car.move())
print('ship.tubes == ', ship.tubes)
print('ship.sound() returns ', ship.sound())
print('s_car.move() returns ', s_car.move())
print('e_car.state() returns', e_car.state())

e_car.charge = 7
print('e_car.state() returns', e_car.state())
print('se_car.speed == ', se_car.speed, 'se_car.charge == ', se_car.charge)
print('se_car.__class__ == ', se_car.__class__)
print('isinstance(se_car, SportECar) == ', isinstance(se_car, SportECar))
print('isinstance(se_car, Car) == ', isinstance(se_car, Car))

try:
    se_car.play()
except Exception:
    print('No play')

try:
    se_car.play2()
except MorePlayErrors:
    print('No play 2')
except PlaybackError:
    print('No play 1')
