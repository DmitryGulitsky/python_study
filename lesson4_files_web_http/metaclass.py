class Base:

    val = 42

    def do_one_thing(self):
        '''Returns one thing'''
        raise  NotImplementedError

    def do_another_thing(selfself, *args, **kwargs):
        '''does something'''
        raise NotImplementedError

class Meta(type):

    def __new__(cls, name, bases, attrs_dict):
        print('Class:', cls)
        print('Name:', repr(name))
        print('Bases:', bases)
        print('Attributes:', attrs_dict)
        x = super().__new__(cls, name, bases, attrs_dict)
        x.function = function
        a_list.append(x)
        return x

def function(self):
    return 42

a_list = []

def fun(self, param=None, value=1):
    if param is None:
        param = a_list
    param.append(value)
    print(value)
    print(param)
    print(self)
    return param

class MyClass(object, metaclass=Meta):

    attr = 'Attribute'
    val = 42

    another = fun

m = MyClass()
print('dir(m) ', dir(m))
print('m.function() ', m.function())
print('m.another() ', m.another())
print('a_list ', a_list)
print(m.another(param=[1, 2], value=3))
