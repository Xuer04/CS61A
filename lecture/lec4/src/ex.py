def summation(begin,end,term):
    """
    pass the function as the argument value
    summation from begin number to end number with the method of term
    """
    assert end > begin, "The end number must greater than begin number!!"
    total, k = 0, begin
    while k <= end:
        total, k = total + term(k), k + 1
    return total


def cube(k):
    return pow(k, 3)


def square(k):
    return pow(k, 2)


def pi_term(k):
    return 8 / ((4 * k - 3) * (4 * k - 1))


def main():
    """
    >>> summation(1, 5, cube)
    225

    >>> summation(3, 5, cube)
    216

    >>> summation(1, 5, square)
    55

    >>> summation(3, 5, square)
    50

    >>> summation(1, 1000000, pi_term)
    3.141592153589902
    """
    pass


if __name__ == '__main__':
    main()

