element = int(input('enter an needed element:'))


def fibonacci(n):
    if n < 0:
        return 'not a valid value'
    if n == 0:
        return 0
    if n == 1:
        return [0, 1]
   # if n == 2:
       # return [1, 1]
    index = 2
    fib_1 = 0
    fib_2 = 1
    result = [fib_1, fib_2]
    while index <= n:
        result.append(fib_1 + fib_2)
        fib_1,  fib_2 = fib_2, fib_1 + fib_2
        index = index + 1

    return result


print(fibonacci(element))

