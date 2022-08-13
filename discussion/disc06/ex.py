# Q1.1
def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def f(g):
        nonlocal n
        n = g(n)
        return n
    return f

# Q2.1
def test():
    """What would Python display?
    >>> s1 = [1, 2, 3]
    >>> s2 = s1
    >>> s1 is s2
    True
    >>> s2.extend([5, 6])
    >>> s1[4]
    6
    >>> s1.append([-1, 0, 1])
    >>> s2[5]
    [-1, 0, 1]
    >>> s3 = s2[:]
    >>> s3.insert(3, s2.pop(3))
    >>> len(s1)
    5
    >>> s1[4] is s3[6]
    True
    >>> s3[s2[4][1]]
    1
    >>> s1[:3] is s2[:3]
    False
    >>> s1[:3] == s2[:3]
    True
    """

# Q2.2
def mystery(p, q):
    p[1].extend([2, 3])
    q.append(p[1:])

p = [2, 3]
q = [4, [p]]
mystery(q, p)

# Q2.3
def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for elm in s:
        key = fn(elm)
        if key in grouped:
            grouped[key].append(elm)
        else:
            grouped[key] = [elm]
    return grouped

# Q2.4
def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs
    in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 2, 2]
    """
    for _ in range(x):
        s.append(el)


