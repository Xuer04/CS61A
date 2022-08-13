#  FIRST_101_DIGITS_OF_PI = 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
#  pi = str(FIRST_101_DIGITS_OF_PI)
#  lis = [int(item) for item in pi]
#  count_lis = [lis.count(i) for i in range(10)]
#  print(count_lis)

sum = 0
for i in range(1,7):
    for j in range(1,7):
        for k in range(1, 7):
            for m in range(1,7):
                if i == 1 or j == 1 or k == 1 or m == 1:
                    sum += 1
                else:
                    sum += (i + j + k + m)

exp = sum / (6 ** 4)
print("sum", sum)
print("exp", exp)
