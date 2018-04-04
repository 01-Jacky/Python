import time


def some_function():
    i = 1
    while True:
        yield i*i
        i += 1

x = some_function()
print(next(x))
print(next(x))
print(next(x))
print(next(x))

''
def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


def fibonacci_generator():
    """Fibonacci numbers generator"""
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a


if __name__ == "__main__":

    # Fib 400000 iterative
    start = time.time()
    value = fibonacci_iterative(400000)
    end = time.time()
    print('Time for fib 400000 iteratively: {}'.format(end-start))

    # Fib 400001 iterative
    start = time.time()
    value = fibonacci_iterative(400001)
    end = time.time()
    print('Time for fib 400001 iteratively: {}'.format(end-start))


    # Fib 400000
    start = time.time()
    g = fibonacci_generator()
    for _ in range(400000):
        current_value = next(g)
    # print(current_value)

    end = time.time()
    print('Time for fib 400000 using generator: {}'.format(end-start))

    # Fib 400001
    start = time.time()
    # print(next(g))
    end = time.time()
    print('Time for fib 400001: {}'.format(end-start))





