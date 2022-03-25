''' numbers from 5 - 1'''
# looping

# for item in range(5, 0, -1):
#     print(item)

# i = 5
# while i > 0:
#     print(i)
#     i -= 1

# functions
# def num(n):
#     print(n)
#
# for item in range(5, 0, -1):
#     num(item)

# def num(n):
#     if n > 0:
#         print(n)
#         num(n-1)
#         # print(n)
#
#
# num(5)

# from sys import getrecursionlimit
# print(getrecursionlimit())

# from sys import setrecursionlimit
# setrecursionlimit(500)
#
# print(getrecursionlimit())

# def num(n):
#     if n > 0:
#         print(n)
#         return num(n-1)
#     new = [item for item in range(5, 0, -1)]
#     return new
#
#
# print(num(5))

''' write a recurssive function to find the factorial of a number '''
#
# def factorial_(num):
#     if num < 0:
#         return 'CAN NOT FIND FACTORIAL'
#     elif num == 1 or num == 0:
#         return 1
#     else:
#         return num * factorial_(num-1)


# print(factorial_(5))
# print(factorial_(4))
# print(factorial_(3))
# print(factorial_(-5))
# print(factorial_(0))
# print(factorial_(5))

''' write a recursion function to calculate the sum of first n numbers '''
# def first_sum(n):
#     if n == 0:
#         return 0
#     return n + first_sum(n-1)
#
# print(first_sum(5))

''' write a recursion function to print countdown from 10 to 1 '''
# def count_down(n):
#     if n <= 0:
#         return 0
#     print(n)
#     time.sleep(1)
#     count_down(n-1)
#
#
# import time
# count_down(10)


''' write a recursion function to find the sum of all the numbers in a (Homogeneous)list/tuple'''
# def sum_iterable(a):
#     if not a:
#         print(a)
#         return 0
#     print(a)
#     return a[0] + sum_iterable(a[1::])
# print(sum_iterable([1,2, 3, 4, 5]))
#
# #or
# def sum_iterable2(a):
#     if len(a) == 1:
#         print(a)
#         return a[0]
#     print(a)
#     return a[0] + sum_iterable2(a[1::])
# print(sum_iterable2([1,2, 3, 4, 5]))

''' write a recursion function to find the sum of all the digits in a number'''
# n = int(input('Enter any number ,'))
#
# def digit_sum(num):
#     if num == 0:
#         return 0
#     return num % 10 + digit_sum(num // 10)
#
#
# print(digit_sum(n))
''' WARF to reverse a string '''

# def reverse_1(string):
#     if not string:
#         return ''
#     print(string)
#     return string[-1] + reverse_1(string[:-1])
#
# def reverse_2(string):
#     if not string:
#         return ''
#     print(string)
#     return reverse_2(string[1:]) + string[0]
#
# print(reverse_2('hello'))
# print()
# print(reverse_1('python'))

''' warf to find number of digits in a given number '''

# def total_digits(n):
#     b = str(n)
#     if len(b) == 1:
#         return 1
#     else:
#         a = int(b[1:])
#         return 1 + total_digits(a)
#
#
# print(total_digits(12345))
