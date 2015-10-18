__author__ = 'pather'


# def halve(n):
#     half = n / 2
#     return half
#
#
# def log2(n):
#     m = 0
#     while n > m:
#         n = halve(n)
#         m = m + 1
#         # print(m)
#         # print(n)
#     # print(n)
#     return m
#
#
# def main():
#     m = log2(1000)
#     print(m)
#
# main()


# def perfect(n):
#     count = 0
#     sum = 0
#     while count < n:
#         count = count + 1
#         sum = sum + count
#     return sum
#
#
# def perfect_sum(n):
#     count = 0
#     sum = 0
#     while count < n:
#         count = count + 1
#         sum = sum + perfect(count)
#     return sum
#
#
# def main():
#     sum = perfect_sum(5)
#     print(sum)
#
# main()


# def fibo(n):
#     first = 1
#     second = 1
#     next = 0
#     counter = 0
#     while counter < n:
#         counter = counter + 1
#         next = first + second
#         first = second
#         second = next
#         print(next)
# fibo(5)

#
# def fibo_2(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fibo_2(n - 1) + fibo_2(n - 2)
#
#
# def loop(n):
#     counter = 0
#     while counter < n:
#         counter = counter + 1
#         print(fibo_2(counter))
#
# loop(6)
