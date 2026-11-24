"""Print or collect Fibonacci numbers below a limit."""


def fib(limit):
    """Print the Fibonacci series below limit."""
    print(*fib2(limit))


def fib2(limit):
    """Return the Fibonacci series below limit."""
    result = []
    a, b = 0, 1
    while a < limit:
        result.append(a)
        a, b = b, a + b
    return result


if __name__ == "__main__":
    import sys

    fib(int(sys.argv[1]))
