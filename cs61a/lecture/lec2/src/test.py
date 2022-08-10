x = 12
z = 7


def f(y):
    x = 3
    print(f"local x: {x}, y: {y}, z:{z}")

f(5)
print(f"global x: {x}")
