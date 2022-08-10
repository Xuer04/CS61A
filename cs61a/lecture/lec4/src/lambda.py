def f(x):
    return x + 1

g = lambda x: f
# the same as below:
# g = lambda x: lambda y: y + 1

h = lambda x: f(x)
# the same as below:
# h = lambda x: x + 1

result_g = g(2)(3)
result_h = h(3)

print(f"result_g: {result_g}")
print(f"result_h: {result_h}")

