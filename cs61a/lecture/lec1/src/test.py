def read_shake():
    """
    >>> read_shake()
    980637    
    """
    file = open('shakespeare.txt')
    word = file.read().split()

    print(f"type of word: {type(word)}")
    print(f"length of text: {len(word)}")


def main():
    read_shake()


if __name__ == '__main__':
    main()

