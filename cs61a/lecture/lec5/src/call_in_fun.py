def call_in_fun(x):
    def h(z):
        print("Inside h function now.")
        return x + z

    print(h(2))

