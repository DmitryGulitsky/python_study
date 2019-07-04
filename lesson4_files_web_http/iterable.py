class MyIterable:

    def __init__(self, start, stop):
        if not stop > start:
            raise ValueError('Start has to be < than stop')
        self.start = start
        self.stop = stop
        self.reset()

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            self.current += 1
            return self.current
        raise StopIteration

    def reset(self):
        self.current = self.start - 2

it = MyIterable(1, 3)
print('next(it) ', next(it))
print('next(it) ', next(it))
print('next(it) ', next(it))
print('next(it) ', next(it))
it.reset()
print('----------------------------')

for i in it:
    print(i, end=' ')
it.reset()
print('----------------------------')

print(iter(it))
it.reset()
print('----------------------------')

iterable = iter(it)
print(next(iterable))