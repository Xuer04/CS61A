class A:
    def __init__(self) -> None:
        print("Enter class A.")


class B:
    def __init__(self) -> None:
        print("Enter class B.")


class C(B, A):
    pass


if __name__ == "__main__":
    c = C()
