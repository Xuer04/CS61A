#  high_lambda = lambda f: lambda x: f(x)

# turn the lambda expression into def function
def high_lambda(f):
    def anon(x):
        return f(x)
    return anon

g = lambda x: x * x
f = lambda x: x + 2

high1 = high_lambda(g)(3)
high2 = high_lambda(f)(3)

