# Function Description


def likes(n):
    """Returns whether George Boole likes the integer n"""
    return n % 2 == 0


def mystery1(n):
    k = 1
    while k < n:
        if likes(n):
            print(k)
        k += 2


def mystery2(n):
    i, j, k = 0, None, None
    while i < n:
        if likes(n):
            if j is not None and (k is None or i - j < k):
                k = i - j
            j = i
        i += 1
    return k


def remove(n, digit):
    """
    >>> remove(231, 3)
    21
    >>> remove(243132, 2)
    4313
    """
    kept, digits = 0, 0
    while n > 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept, digits = kept / 10 + last, digits + 1
    return round(kept * 10 ** (digits - 1))

