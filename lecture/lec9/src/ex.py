def inverse_cascade(n):
    """Write a function that prints an inverse cascade
    >>> inverse_cascade(1234)
    1
    12
    123
    1234
    123
    12
    1
    """
    grow(n)
    print(n)
    shrink(n)


def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)


def grow(n):
    return f_then_g(grow, print, n // 10)


def shrink(n):
    return f_then_g(print, shrink, n // 10)


def inverse_cascade2(n):
    """Write a function that prints an inverse cascade(rewrited)
    >>> inverse_cascade2(1234)
    1
    12
    123
    1234
    123
    12
    1
    """
    def grow(n):
        if n < 10:
            print(n)
        else:
            grow(n // 10)
            print(n)

    def shrink(n):
        if n < 10:
            print(n)
        else:
            print(n)
            shrink(n // 10)

    grow(n // 10)
    print(n)
    shrink(n // 10)


if __name__ == '__main__':
    #  inverse_cascade(12345)
    inverse_cascade2(12345)

