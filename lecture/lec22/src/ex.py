def f(x):
    return x + f.y

def g(x, f):
    f.y = 3
    return x + f.y

if __name__ == "__main__":
    #  print(f(10)) # Error

    f.y = 5
    print(f(10)) # 15
    print(g(10, f)) # 13


