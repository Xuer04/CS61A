def timer(func):
    def func_wrapper(*args, **kwargs):
        from time import time
        time_start = time()
        result = func(*args, **kwargs)
        time_end = time()
        time_spend = time_end - time_start
        print('%s cost time: %.7f s' % (func.__name__, time_spend))
        return result
    return func_wrapper


@timer
def fact(n):
    """Return the factorial of n."""
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)

@timer
def fact_times(n, k):
    """Return k times n factorial."""
    if n == 0:
        return k
    else:
        return fact_times(n - 1, k * n)

if __name__ == '__main__':
    fact(20)
    fact_times(20, 1)
