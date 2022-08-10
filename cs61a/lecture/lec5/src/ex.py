def repeat(f, x):
    while f(x) != x:
        x = f(x)
    return x


def g(y):
    return (y + 5) // 3


def square(x):
    return x * x


def call_in_function(x):
    def h(z):
        return x + z
    a = h(2)
    print(a)

result = repeat(g, 5)


def coffee(grounds):
    x = 4
    return grounds(x)

x = 6
f = lambda x: x + 2
coffee(f)

