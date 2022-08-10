import sys


"""
输入一个数字，获得它的质因数分解序列
"""

l = []


#  def IsPrime(n):
    #  if n <= 1:
        #  return False
    #  elif n == 2 or n == 3:
        #  return True
    #  else:
        #  for i in range(2, n // 2 + 1):
            #  if n % i == 0:
                #  return False
        #  return True


#  def Prime_Factorization(n):
    #  if n <= 1:
        #  return None
    #  else:
        #  for i in range(2, n + 1):
            #  if n % i == 0 and IsPrime(i):
                #  break
        #  l.append(i)
        #  n = n // i
        #  Prime_Factorization(n)

"""
可以优化的地方：
1. 递归可以改成迭代
2. 素数判断可以改成寻找最小素数
"""


def min_prime_factor(n):
    if n <= 1:
        return None
    else:
        k = 2
        while n % k != 0:
            k += 1
        return k


#  def Prime_Factorization(n):
    #  if n <= 1:
        #  return None
    #  else:
        #  while n > 1:
            #  num = min_prime_factor(n)
            #  l.append(num)
            #  n = n // num

"""
进一步优化，把最小素因数的函数移到函数内部
"""


def Prime_Factorization(n):
    if n <= 1:
        return None
    else:
        while n > 1:
            k = 2
            while n % k != 0:
                k += 1
            l.append(k)
            n = n // k


def main():
    if len(sys.argv) != 2:
        print("Input Error, please input a number!!")
        sys.exit(1)
    else:
        num = int(sys.argv[1])
        Prime_Factorization(num)

        if len(l) == 1:
            print(f"The num is {num}, is a prime number.\n")
        else:
            print(f"The num is {num}.\n")

        print(f"The prime factorization result of {num} is:")
        print(l)


if __name__ == '__main__':
    main()

