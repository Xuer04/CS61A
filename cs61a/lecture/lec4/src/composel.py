def composel(f, g):
    """we don't need to define an extra function if we use the lambda expression."""
    return lambda x: f(g(x))


def square(x):
    return x*x


def add_one(x):
    return x+1


def main():
    """
    >>> f = composel(lambda x: x*x, lambda y: y+1)
    >>> result = f(12)
    >>> result
    169

    >>> f = composel(lambda x: max(10,x), lambda y: min(20,y))
    >>> result = f(12)
    >>> result
    12

    >>> result = f(25)
    >>> result
    20

    >>> f = composel(square, add_one)
    >>> result = f(10)
    >>> result
    121
    """

