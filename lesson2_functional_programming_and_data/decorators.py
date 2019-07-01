def a_func():
    print('Hello from func!')

print('a_func()')
a_func()

def decorator(func):
    def wrapper():
        print('some text')
        func()
    return wrapper

print('--------------------------')
print('a_func = decorator(a_func)')
a_func = decorator(a_func)

print('--------------------------')

@decorator
def another_func():
    print('another func')

another_func()

print('--------------------------')

def decorator(func):
    def wrapper(*args):
        print('args == ', args)
        return func(*args)
    return wrapper

@decorator
def count(a, b):
    return a + b

count(3, 4)
print('count(3, 4) returns ', count(3, 4))

print('--------------------------')
print('key word arguments')

def decorator(func):
    def wrapper(*args, **kwargs):
        print('args == ',args)
        print('kwargs == ', kwargs)
        return func(*kwargs)
    return wrapper

@decorator
def count(a, b):
    return a + b

count(a=7, b=6)
print('count(a=7, b=6) returns ', count(a=7, b=6))

print('--------------------------')

def decorator(func):
    def wrapper(*args, **kwargs):
        print('args == ',args)
        print('kwargs == ', kwargs)
        return func(*args, **kwargs)
    return wrapper

@decorator
def count(a, b):
    return a + b

count(3, 4)
print('count(3, 4) returns ', count(3, 4))

print('--------------------------')

def decorator(func):
    def wrapper(*args, **kwargs):
        print('args == ',args)
        print('kwargs == ', kwargs)
        return func(*args, **kwargs)
    return wrapper

@decorator
def count(a, b):
    return a + b

count(3, b=6)
print('count(3, b=6) returns ', count(3, b=6))

print('--------------------------')

def decorator(func):
    def wrapper(*args, **kwargs):
        print('args == ',args)
        print('kwargs == ', kwargs)
        return func(*args, **kwargs)
    return wrapper

@decorator
def count(a, b):
    return a + b

count(a=7, b=6)
print('count(3, b=6) returns ', count(3, b=6))

print('--------------------------')
print('decorator generation')

from functools import wraps

def gen_dec(x):
    print('In a gen dec')
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(args, kwargs)
            return x * func(*args, **kwargs)
        print('Generated a wrapper')
        return wrapper
    print('Generated a decorator')
    return decorator

@gen_dec(3)
def mul(a, b):
    return a * b

print('mul(3, 4) - ', mul(3, 4))
print('mul - ', mul)

print('--------------------------')

from contextlib import contextmanager

@contextmanager
def managed_res(*args, **kwargs):
    print(args, kwargs)
    yield map(lambda x: x * 2, args)
    print('Closed', args)

with managed_res(1, 2, 3) as g:
    print(list(g))
    print('Leaving')

print('Left')