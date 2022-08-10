def f(x):
    def g(y):
        z = -x
        return f
    return g


f(2)(3)(4)(5)
