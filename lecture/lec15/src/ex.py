def f(x, y=[]):
    y.append(x)
    print(id(y))


if __name__ == "__main__":
    f(1)
    f(3)
    f(5)
    f(7, [1])
