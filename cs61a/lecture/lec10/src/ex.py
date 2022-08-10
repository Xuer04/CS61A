def list_sum(L):
    """Return the sum of all elements in the list L.

    >>> list_sum([1, 2, 3, 4])
    10
    >>> list_sum([1, 2, 2])
    5
    """
    if L == []:
        return 0  # base case
    else:
        return L[0] + list_sum(L[1:])  # recursively


def n_sum_rec(n):
    """Return the sum of the first n.

    >>> n_sum_rec(5)
    15
    >>> n_sum_rec(7)
    28
    """
    if n == 1:
        return 1
    else:
        return n + n_sum_rec(n - 1)


def n_sum_iter(n):
    """Return the sum of the first n.

    >>> n_sum_iter(5)
    15
    >>> n_sum_iter(7)
    28
    """
    n_sum = 0
    for i in range(0, 1 + n):
        n_sum += i
    return n_sum


def divisors(n):
    """Return the integers that evenly divide n.

    >>> divisors(1)
    [1]
    >>> divisors(4)
    [1, 2]
    >>> divisors(12)
    [1, 2, 3, 4, 6]
    >>> [n for n in range(1, 1000) if sum(divisors(n)) == n]
    [1, 6, 28, 496]
    """
    return [1] + [x for x in range(2, n) if n % x == 0]

# string can represent program.
command = 'curry = lambda f: lambda x: lambda y: f(x, y)'
exec(command)
print(curry)


def reverse(s):
    """Reverse the input string."""
    if s:
        return s[-1] + reverse(s[:-1])
    else:
        return ""


def reverse2(s):
    """Tutor's solution."""
    if len(s) == 1:
        return s
    else:
        return reverse2(s[1:]) + s[0]

# Helper function and recursion

def fact(n):
    """Return the factorial of n."""
    return fact_helper(n)


def fact_helper(n, k = 1):
    """Computes k * (k + 1) * (k + 2) * ... * n

    >>> fact_helper(4)
    24
    >>> fact_helper(5)
    120
    """
    if k == n:
        return n
    else:
        return k * fact_helper(n, k + 1)


#  def fact_helper(n, k = 1, result = 1):
    #  """Computes k * (k + 1) * (k + 2) * ... * n
    #  by accumulating the result.

    #  >>> fact_helper(4)
    #  24
    #  >>> fact_helper(5)
    #  120
    #  """
    #  if k > n:
        #  return result
    #  else:
        #  return fact_helper(n, k + 1, k * result)

