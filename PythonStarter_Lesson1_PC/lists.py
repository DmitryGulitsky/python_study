array = [1, 2, 3, 4, 5]

print('array == ', array)
print('len(array) == ', len(array))
print('array[1] == ', array[1])
print('array[2, 4] == ', array[2:4])
print('array[3:] == ', array[3:])
print('array[3:4] == ', array[3:4])

array[0] = 10
print('array[0] = 10')
print('array == ', array)

array[:2] = [6, 7, 8]
print('array[:2] = [6, 7, 8]')
print('array == ', array)
print('len(array) == ', len(array))

tpl = (7 , 6, 5)
print('tpl = (7 , 6, 5)')
print('type(array) == ', type(array))
print('type(tpl) == ', type(tpl))

print('tpl[:2] == ', tpl[:2])

array.append(11)
print('array.append(11)')
print('array == ', array)

array.insert(0, 4)
print('array.insert(0, 4)')
print('array == ', array)

array += [2]
print('array += [2]')
print('array == ', array)

print('array.pop() == ', array.pop())
array.pop()
print('array == ', array)

print('array.pop(1) == ', array.pop(1))
array.pop(1)
print('array == ', array)

dictionary = {'key': 'value'}
print('dictionary == ', dictionary)
print('type(dictionary) == ', type(dictionary))

dictionary['spam'] = 'eggs'
print('dictionary == ', dictionary)

print('dictionary.keys() == ', dictionary.keys())
print('dictionary.values() == ', dictionary.values())
print('dictionary.items() == ', dictionary.items())

dictionary['spam'] = dictionary['spam'] * 2
print('dictionary[spam] = dictionary[spam] * 2')
print('dictionary == ', dictionary)

set_ = {1, 2, 3}
print('set == ', set)
print('type(set_) == ', type(set_))

print('array.append(set_)')
array.append(set_)
print('array == ', array)

set_.add(5)
print('set_.add(5)')
print('set_ == ', set_)
print('array == ', array)

array[-1].add(6)
print('array[-1].add(6)')
print('set_ == ', set_)
print('array == ', array)

print('some text: ' + str(42))
print('our list: %s' % array)
print('our list: %s %%s' % array)
print('a: %s, b: %s' % (42, 'spam'))

print('repr(spam) - ', repr('spam'))
print('repr: %r' % 'spam')

print('our set: {}qwerty'.format(set_))

print('our list: {{ {}'.format(array))

print('{} and {}'.format('eggs', 'spam'))
print('{1} and {0}'.format('eggs', 'spam'))
print('{1} and {0} and {1}'.format('eggs', 'spam'))
print('{value} and {key} and {value}'.format(value = 'eggs', key = 'spam'))

#number rounding
print('number rounding')
print('value: %.2f' % 12.34545)
print('value: {:.2f}'.format(12.34545))

#f-strings
print(f'value: {array}')

value = 123.456
a_line = 'spam and eggs'
text = (
    'first line'
    f'\na value {value:.2f}\n'
    f'a line {a_line}'
)
print(text)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print('matrix - ', matrix)
print('matrix[1] == ', matrix[1])
print('matrix[1][2] == ', matrix[1][2])

#if else
print('if-else')
a = 5
b = 6
if a > b:
    value = a * 2
else:
    value = b // 2
print('Value is ', value)

value = a * 2 if a > b else b // 2
print('Value is ', value)