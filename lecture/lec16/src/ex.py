t = [1, 2, 3]
t[1:3] = [t]
print(t)


def f(x):
    def g(y):
        # print(x + 1)  # Get error: the local variable referenced before
        # assignment.
        x = y
        print(x + 1)
    return g


f(1)(4)
