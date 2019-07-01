print('while break')

while True:
    print('Once')
    break

print('-')
i = 0
while True:
    print(i)
    i += 1
    if i > 3:
        break

print('-')
print('while else')
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print('else')

print('-')
for i in range(1 , 5):
    print(i, end=' is ')
    if i % 2 == 0:
        print('even')
    else:
        print('odd')

print('-')
print('for continue')
for i in range(1, 8):
    print(i, end=' ')
    if i % 2 == 0:
        print('is even')
        continue
        print('never printed')
    print('is odd')