class Base:

    val = 42

    def do_one_thing(self):
        '''Returns one thing'''
        raise  NotImplementedError

    def do_another_thing(selfself, *args, **kwargs):
        '''does something'''
        raise NotImplementedError

class AnotherType(type):
    pass

class MyClass(Base, metaclass=AnotherType):
    '''
    A simple class
    '''
    

    val = 50

    def do_one_thing(self):
        return '1 thing'

    def do_another_thing(selfself, *args, **kwargs):
        return f'{args} | {kwargs}'

m = MyClass()

m.val = 13
print('MyClass.val == ', MyClass.val, 'm.val == ', m.val)

m.do_one_thing()
m.do_another_thing()
print("m.do_another_thing(1, 2, 3, abc='qwe') returns ", m.do_another_thing(1, 2, 3, abc='qwe'))

print('m.__dir__() ', m.__dir__())

print('type(MyClass) ', type(MyClass))

print('repr(type)', repr(type))

AnotherClass = type('AnotherClass', (MyClass, ), {'val': 13})
print('AnotherClass', AnotherClass)
print('vars(AnotherClass)', vars(AnotherClass))
ac = AnotherClass
print(isinstance(ac, MyClass))
print('MyClass.__doc__', MyClass.__doc__)