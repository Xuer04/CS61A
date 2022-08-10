def repeat(k):
    """
    >>> f = repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
    7
    1
    5
    1
    """
    return detector(lambda j: False)(k)


def detector(have_seen):
    def g(i):
        if have_seen(i):   # f function tells us whether we have seen i before.
            print(i)
        new_have_seen = lambda j: j == 1 or have_seen(j)
        return detector(new_have_seen)
    return g

