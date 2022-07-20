def fibonacci(n):
    """
    The Fibonacci sequence is a type series where each number is the sum of the two that precede it.
    It starts from 0 and 1 usually.
    The Fibonacci sequence is given by 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on.
     - https://byjus.com/maths/fibonacci-sequence/
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

    if __name__ == '__main__':
        num = int(input('>'))
        print(fibonacci(n))


def lucas(n):
    """
    The Lucas series has the same recursive relationship as the Fibonacci sequence, where each
    term is the sum of the two previous terms, but with different starting values.
    https://en.wikipedia.org/wiki/Lucas_number
    """

    if n == 0:
        return 2
    if n == 1:
        return 1

    return lucas(n - 1) + lucas(n - 2)

    if __name__ == '__main__':
        num = int(input('>'))
        print(lucas(n))

def sum_series(n):

    if n < 0:
        return n
    if n == 1:
        return 2
    if n == 2:
        return 2

    return fibonacci(n-2) + fibonacci(n-1) + lucas(n-2) + lucas(n-1)

if __name__ == '__main__':
    n = int(input('> '))
    print(f'The {n} th  fibonacci number  is {fibonacci(int(n))}, th lucas number is {lucas(int(n))} the sum of those two is {sum_series(int(n))}')


