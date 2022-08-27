def f(ls):
    for item in ls:
        yield item


if __name__ == "__main__":
    l = [1, 2, 3, 4]
    ls = f(l)
    for item in ls:
        print(item)
