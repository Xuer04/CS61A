import sys

l = []


def f_re(n):
    l.append(n)
    if n == 1:
        return None
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    f_re(n)


def f_it(n):
    l.append(n)
    if n == 1:
        return None
    while n != 1:
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2
        l.append(n)
    return


def main():
    if len(sys.argv) != 3:
        print('Input Error, please input one number!!!')
        sys.exit(1)

    num = sys.argv[1]
    print(f'The num you input is {num}\n')
    flag = int(sys.argv[2])

    if flag == 1:
        print("This is the recursion method.\n")
        f_re(int(sys.argv[1]))
    else:
        print("This is the iteration method.\n")
        f_it(int(sys.argv[1]))

    print(f'hailstone list: \n{l}')
    print(f'\nthe length of list is {len(l)}')

if __name__ == '__main__':
    main()

