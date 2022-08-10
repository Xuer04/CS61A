# Q1.1
def wears_jacket_with_if(temp, raining): 
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if temp < 60 or raining:
        return True
    else:
        return False

# AC
def wears_jacket_with_if_oneline(temp, raining):
    """
    >>> wears_jacket_with_if_oneline(90, False)
    False
    >>> wears_jacket_with_if_oneline(40, False)
    True
    >>> wears_jacket_with_if_oneline(100, True)
    True
    """
    return temp < 60 or raining


def square(x):
    print("here!")
    return x * x


def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0

# Q1.3
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    if n <= 1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True
