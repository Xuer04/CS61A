# Q1.1
def count_stair_ways(n):
    """Return the number of ways to go up the flight of stairs.

    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(4)
    5
    >>> count_stair_ways(6)
    13
    """
    if n == 0 or n == 1:
        return 1
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)

# Q1.2
def count_k(n, k):
    """Return the number of ways to go up the flight of stairs the the max step of k.

    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    elif k == 0 or k == 1:
        return 1
    else:
        count_sum = 0
        for i in range(1, k + 1):
            count_sum += count_k(n - i, k)
        return count_sum

# Q2.1
def test():
    """Some tests for list.

    >>> a = [1, 5, 4, [2, 3], 3]
    >>> print(a[0], a[-1])
    1 3
    >>> len(a)
    5
    >>> 2 in a
    False
    >>> 4 in a
    True
    >>> a[3][0]
    2
    """

# Q2.2
def even_weighted(s):
    """Returns a new list that keeps only the even-indexed elements of s and
    multiplies them by their corresponding index.

    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [x * s.index(x) for x in s[::2]]

# Q2.3
def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.

    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if s == []:
        return 1
    elif len(s) == 1:
        return s[0]
    else:
        return max(s[0] * max_product(s[2:]), max_product(s[1:]))

