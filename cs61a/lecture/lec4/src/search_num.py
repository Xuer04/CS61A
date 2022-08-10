import math


def search(fun):
    x = 0
    while True:
        if fun(x):
            return x
        else:
            x += 1


def is_square(n):
    x = 1
    if n <= 1:
        return False
    while x < n and x*x != n:
        x += 1
    if x == n:
        return False
    else:
        return True


def is_square_of_num(num):
    def one_square(x):
        return math.sqrt(x) == num 
    return one_square


def is_sqrt_of_num(num):
    def one_sqrt(x):
        return math.sqrt(num) == x
    return one_sqrt


def main():
    """
    >>> search(is_square)
    4
    >>> search(is_square_of_num(16))
    256
    >>> search(is_sqrt_of_num(144))
    12
    """

