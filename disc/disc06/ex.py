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
def test1():
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


counts = [1, 2, 3]

# use for loop
for i in counts:
    print(i)

# the same complete with while loop
iterator = iter(iterable)
try:
    while True:
        elem = next(iterator)
        # do something
except StopIteration:
    pass

# Q3.1
def test2():
    """What would Python display?
    >>> s = [[1, 2]]
    >>> i = iter(s)
    >>> j = iter(next(i))
    >>> next(j)
    1
    >>> s.append(3)
    >>> next(i)
    3
    >>> next(j)
    2
    >>> next(i)
    Error: StopIteration
    """

# Q4.1
def filter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter(range(5), is_even)) # a list of the values yielded from the call to filter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for item in iterable:
        if fn(item):
            yield item

# Q4.2
def merge(a, b):
    """
    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    item_a = next(a)
    item_b = next(b)
    while True:
        yield min(item_a, item_b)
        if item_a < item_b:
            item_a = next(a)
        elif item_a > item_b:
            item_b = next(b)
        else:
            item_a = next(a)
            item_b = next(b)

