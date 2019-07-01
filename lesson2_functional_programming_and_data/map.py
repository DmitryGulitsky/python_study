values = range(7, 13)

mapped = map(lambda x: x + 3, values)
print(list(mapped))

print('-------------------------')

a = 3

def exp(x):
    return lambda y: y ** x

funcs = (exp(x) for x in range(2, 8))

print(list(map(lambda f: f(a), funcs)))