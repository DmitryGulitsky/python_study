a = 16
b = 42

print('for in operator')
t = (1, 2, 3, 'abc', 'spam', 'eggs')
print("t = (1, 2, 3, 'abc', 'spam', 'eggs')")
print("5 in t", 5 in t)
print("'spam' in t", 'spam' in t)
print("'abc' in t", 'abc' in t)

print("'a' in ['a', 'b', 'c'] == ", 'a' in ['a', 'b', 'c'])
print("'key' in ['key': 'value'] == ", 'key' in {'key': 'value'})
print("7 in {7, 8, 9} == ", 7 in {7, 8, 9})
print('-------------------------------------')

print('list')
lst = [0, 1, 2, 3, 4]
print("lst == ", lst)

for item in lst:
    print(item)

print("-")
for item in {5, 3, 7, 9, 11, 15}:
    print(item)

print("-")
dictionary = {'key': 'value', 'spam': 'eggs'}
print('dictionary == ', dictionary)
for key in dictionary:
    print('key == ', key)
    print('dictionary[key] == ', dictionary[key])
print('-')

print('.values() method')
print('dictionary.values() == ', dictionary.values())

print('for value in dictionary.values():', dictionary.values())
for value in dictionary.values():
    print(value)

print('-')
results = []
values = [1, 2, 3, 4, 5]
print('values == ', values)
print('results.append(value ** 2)')
for value in values:
    results.append(value ** 2)
print('results == ', results)
print('-')

line = 'abcdef'
print('line == ', line)

for c in line:
    print(c, end=' ')

string = ''
strings = ['abc', 'def', 'ghi']
print('string == ', string)
print('strings == ', strings)

for s in strings:
    string += s
    print('string == ', string)

print('-------------------------------------')

print('.join() operator')

print("''.join(strings) == ", ''.join(strings))
print("' '.join(strings) == ", ' '.join(strings))
print("', '.join(strings) == ", ', '.join(strings))

print('-------------------------------------')

print('list comprehension')
print('[val ** 2 for val in values] - ', [val ** 2 for val in values])

print('{val: val ** 2 for val in values} - ', {val: val ** 2 for val in values})

print('generator')
gen = (val ** 2 for val in values)
print("(val ** 2 for val in values)", gen)
print('next(generator) == ', next(gen))
print('next(generator) == ', next(gen))
print('next(generator) == ', next(gen))
print('list(generator) == ', list(gen))


print('-------------------------------------')

lines = ['spam', 'eggs', 'another line']
print('lines - ', lines)

for line in lines[:]:
    if len(line) > 7:
        lines.insert(0, line)
        print('lines - ', lines)

print('-')
line = 'python'
print("line = 'pyton' - ")
print("line[::2] - (each 2 element)", line[::2])

print('-')
print('values == ', values)
print("values[::3] == ", values[::3])

print('-')
print('values == ', values)
print('values[::-1] == ', values[::-1])
print('line == ', line)
print('line[::-1] == ', line[::-1])

print('------------------------')
print('list(range(10)) - ', list(range(10)))
print('list(range(7, 13)) - ', list(range(7, 13)))
print('list(range(10, 40, 3)) - ', list(range(10, 40, 3)))
print('-')