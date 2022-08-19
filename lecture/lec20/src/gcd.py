def gcd(n, d):
    """Return the gcd of number {n} and {d}"""
    while n != d:
        n, d = min(n, d), abs(n - d)
    return n


if __name__ == "__main__":
    print(gcd(12, 8))
