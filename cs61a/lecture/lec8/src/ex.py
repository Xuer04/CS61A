def luhn_sum_iter(n):
    """
    Return the sum of the integer n with luhn algorithm(iterative version).
    >>> luhn_sum_iter(2)
    2
    >>> luhn_sum_iter(12)
    4
    >>> luhn_sum_iter(42)
    10
    >>> luhn_sum_iter(138743)
    30
    >>> luhn_sum_iter(5105105105105100) # example Mastercard
    20
    >>> luhn_sum_iter(4012888888881881) # example Visa
    90
    >>> luhn_sum_iter(79927398713) # from Wikipedia
    70
    """
    if n < 10:
        return n
    else:
        sum_digits, count = 0, 1
        while n > 0:
            last_digit = n % 10
            if count % 2 == 0:
                last_digit *= 2
                if last_digit >= 10:
                    last_digit = last_digit // 10 + last_digit % 10
            else:
                pass
            sum_digits, count = sum_digits + last_digit, count + 1
            n = n // 10
        sum_digits += n

    return sum_digits


if __name__ == '__main__':
    print('sum:', luhn_sum_iter(5105105105105100))

