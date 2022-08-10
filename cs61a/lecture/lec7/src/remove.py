import sys


# zcx's method
def remove1(n, digit):
    """
    >>> remove1(231, 3)
    21
    >>> remove1(243132, 2)
    4313
    """
    kept, count = 0, 0
    while n != 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept = kept + last * (10 ** count)
            count = count + 1
    return kept

# tutor's method
def remove2(n, digit):
    """
    >>> remove2(231, 3)
    21
    >>> remove2(243132, 2)
    4313
    """
    kept, count = 0, 0
    while n > 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept = kept / 10 + last
            count = count + 1
    return round(kept * 10 ** (count - 1))

# xzq's method
def remove3(num1, num2):
    """
    >>> remove3(231, 3)
    21
    >>> remove3(243132, 2)
    4313
    """
    num_list = [x for x in num1]
    while num2 in num_list:
        num_list.remove(num2)
    result = int(''.join(num_list))
    return result


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("The input is invalid.")
    else:
        num1 = sys.argv[1]
        num2 = sys.argv[2]

        # test method
        result = remove1(int(num1), int(num2))
        #  result = remove2(int(num1), int(num2))
        #  result = remove3(num1, num2)

        print(f"The result after removing is {result}.")

