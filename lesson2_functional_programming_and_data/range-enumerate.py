print('list(range(10)) - ', list(range(10)))
print('list(range(7, 13)) - ', list(range(7, 13)))
print('list(range(10, 40, 3)) - ', list(range(10, 40, 3)))
print('-')

for i in range(5):
    print(i)
print('-')

for i in range(1, 5):
    print (i, '^2 == ', i**2)

print('-')
values = list (range(7, 13))
print('values == ', values)

for i in range(len(values)):
    print(i , values[i])

print('-')
a = 16
b = 42
print("a == ", a, " b == ", b)
a, b = b, a
print("a, b = b, a")
print("a == ", a, " b == ", b)

print('---------------')
print('enumerate(range(10) == ', enumerate(range(10)))

e = enumerate(values)
print('e = enumerate(values) == ', e)

print('---------------')
print('for i, val in enumerate(values)')
for i, val in enumerate(values):
    print(i, val)
print('-')
print('for i, val in enumerate(values, 1)')
for i, val in enumerate(values, 1):
    print(i, val)

print('---------------')
print('next(e) == ', next(e))
print('next(e) == ', next(e))
print('list(e) == ', list(e))

print('---------------')
print('for in else')
for i in range(5):
    print(i)
else:
    print('else!')

print('---------------')
print('for in break else')
for i in range(10, 100, 5):
    print(i)
    if i >=30:
        break
else:
    print('else!')

print('-')
for i in range(3):
    print(i)
    break