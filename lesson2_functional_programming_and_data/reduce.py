from functools import reduce
print('reduce - ', reduce)

to_mul = range(1, 7)
product = reduce(lambda x, y: x * y, to_mul)
print(product)

print('-------------------------------------')

to_mul = range(1, 7)
product = reduce(lambda x, y: x * y, to_mul, 10)
print(product)