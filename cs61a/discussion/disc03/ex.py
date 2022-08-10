# Q1.1
def multiply(m, n):
    """Returns the product of two integers.
    >>> multiply(5, 3)
    15
    """
    if m == 1:
        return n
    elif n == 1:
        return m
    else:
        return m + multiply(m, n - 1)


# Q1.2
def rec(x, y):
    """Return the result of pow(x, y)
    >>> rec(3, 2)
    9
    >>> rec(2, 4)
    16
    """
    if y > 0:
        return x * rec(x, y - 1)
    else:
        return 1


# Q1.3
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return 1 + hailstone(n // 2)
        else:
            return 1 + hailstone(n * 3 + 1)


# Q1.4
def merge(n1, n2):
    """ Merges two numbers in decreasing order.
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    else:
        digit = min(n1 % 10, n2 % 10)
        if n1 % 10 == digit:
            return digit + 10 * merge(n1 // 10, n2)
        else:
            return digit + 10 * merge(n1, n2 // 10)


# Q1.5
def make_func_repeater(f, x):
    """ This function returns the result of applying f to x this number of times.
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def repeat(n):
        if n == 0:
            return x
        else:
            return f(repeat(n - 1))
    return repeat


# Q1.6
def is_prime(n):
    """Return the result of whether n is a prime number.
    >>> is_prime(12)
    False
    >>> is_prime(11)
    True
    """
    def prime_helper(n, k):
        if k >= n:
            return True
        elif k != 1 and n % k == 0:
            return False
        else:
            return prime_helper(n, k + 1)

    return prime_helper(n, 1)

