def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

print('fib(5)', fib(5))
print('fib(5)', fib(10))
print('fib(5)', fib(15))
print('fib(5)', fib(100))

def recur_fib(n):
    if n <= 1:
        return n
    return recur_fib(n - 1) + recur_fib(n - 2)

print('recur_fib(10) - ', recur_fib(10))