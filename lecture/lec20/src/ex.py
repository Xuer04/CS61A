def repr(x):
    return type(x).__repr__(x)


class Kangaroo:
    def __init__(self):
        self.pouch_contents = []

    def put_in_pouch(self, string):
        if isinstance(string, str):
            if string not in self.pouch_contents:
                self.pouch_contents.append(string)
            else:
                print("Object already in pouch.")
                return
        else:
            print("The input must be string.")

    def __str__(self):
        if self.pouch_contents:
            print(f"The kangaroo's pouch contains {self.pouch_contents}")
        else:
            print("The kangaroo's pouch is empty.")


class A:
    pass


class B(A):
    pass


def test():
    """
    >>> b = B()
    >>> isinstance(b, B)
    True
    >>> isinstance(b, A)
    True
    >>> type(b) == B
    True
    >>> type(b) == A
    False
    """

