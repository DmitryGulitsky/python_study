print(None, type(None))

def some_function():
    print('Hello world!')

print('some_function() returns ', some_function())

print('-')

def return_2():
    return 2

print('return_2() returns ', return_2())

print('-')

def out_fun():
    def inner():
        return 'inner text'
    return inner
print('out_fun() returns ', out_fun())
print('out_fun()() returns ', out_fun()())

print('-')

def mul_x(x):
    print('Got ', x)
    def multiply(y):
        return x * y
    return multiply
print(mul_x(3))

mul_3 = mul_x(3)
print('mul_3(5) returns', mul_3(5))

print('-')

x = 5
def fun1():
    print('1x', x)

def fun2():
    x = 10
    print('2x', x)

def fun3():
    x = 15
    print('3x', x)

print('x == ', x)
print('fun1() ')
fun1()
print('fun2() ')
fun2()
print('fun3() ')
fun3()
print('x == ', x)

print('-')
x = 42
print('x == ', x)
print('fun1() ')
fun1()
print('fun2() ')
fun2()
print('fun3() ')
fun3()

print('--------------------')
print('generator')

def func():
    return 42, 'spam', 'eggs'
a = func()
print(a)

def gen():
    yield 42

g = gen()

print('g returns', g)
print('next(g) ', next(g))

print('-')

def gen():
    for i in range(4):
        yield i

g = gen()

print('list(g) == ', list(g))
print('list(g) == ', list(g))

print('--------------------')

def our_enum(seq, start=0):
    n = start
    for item in seq:
        yield n, item
        n += 1

values = range(7, 13)
g = our_enum(values, 3)

print(list(g))
print('--------------------')

def exp(x):
    return lambda y: y ** x

exp_3 = exp(3)
print('exp_3(2) returns ', exp_3(2))
print('exp_3(4) returns ', exp_3(4))

print('--------------------')
def gen():
    for i in range(10):
        print(i)
        if i > 5:
            yield i

g = gen()
print(next(g))
print(next(g))
print('-')
list(g)
