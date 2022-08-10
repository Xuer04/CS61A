def make_adder(x):
    def adder(y):
        return x+y
    return adder


def main():
    """
    >>> f_add_one = make_adder(1)
    >>> f_add_one(3)
    4

    >>> f_add_three = make_adder(3)
    >>> f_add_three(4)
    7

    >>> make_adder(2)(3)
    5
    """

