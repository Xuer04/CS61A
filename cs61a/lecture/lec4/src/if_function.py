def if_fun(c,t,f):
    """try to write a function that does the same thing as an if statement"""
    if c:
        return t
    else:
        return f


def T():
    print("It's True.")


def F():
    print("It's False.")


def C():
    return True


def fake_if_state():
    """all the function will be called before passed into the if_fun()"""
    return if_fun(C(), T(), F())


def main():
    """
    >>> if_fun(1, 2+3, 2-3)
    5
    >>> if_fun(True, 'yes', 'no')
    'yes'

    >>> fake_if_state()
    It's True.
    It's False.
    """

if __name__ == '__main__':
    main()

