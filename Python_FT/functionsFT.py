# s = 'hello python'
# count = 0
# for _ in s:
#     count += 1
# print(count)
#
# l = [1, 2, 3, 6, 19, -34]
# l_count = 0
# for _ in l:
#     l_count += 1
# print(l_count)

# def my_len(n):
#     count = 0
#     for _ in n:
#         count += 1
#
#     return count
#
# print('hello')
# print('Good morning')

# a = my_len(s)
# print(my_len(l))
#
# print('after function call ')
# print(print(a))


# def sum_two(a, b):
#     return a + b
#
#
# print(sum_two(20, 31))

''' function to count no of vowels in any string '''


# def no_of_vowels(string):
#     count = 0
#     for i in string:
#         if i.lower() in 'aeiou':
#             count += 1
#     print('in side function' , count)
#     return count
#
#
# print(no_of_vowels('Hello'))

'''wap to search for char in a given string and return the corresponding index'''

# s = input('Enter anything : ')
# c = input('Enter a char to search in the above string : ')


# def search(string, char):
#     for i in string:
#         if char == i:
#             return string.index(i)
#
#
# print(search(s, c))

# def search(string, char):
#     temp = string.find(char)
#     if temp == -1:
#         return f'{char} not found in {string}'
#     return temp
#
#
# print(search(s, c))

''' check whether a given number is prime or not '''
# num = int(input('Enter a number : '))
#
#
# def is_prime(n):
#     for i in range(2, int(n / 2)):
#         if n % i == 0:
#             return f'{n} is not Prime'
#     else:
#         return f'{n} is a prime'
#
#
# print(is_prime(num))

# def add_two(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#     return a + b * c


# print(add_two(4, 5))
# print(add_two(4, 5, 6))

# def greet(name, category):
#     print(f'hi {name} , welcome to {category} catagory for shopping ')
#
# greet('Akash', 'shoes')
#
# greet('shoes', 'Akash')
#
# greet(category='shoes', name='Akash')

# def add_two(a, b,/, e, *, c, d):
#     print(a)
#     print(b)
#     print(c)
#     print(a + b + c + d + e)
#
# # add_two(10, 20, 30, 40)
# # add_two(c=30, b=20, a=10, d=40)
# add_two(20, 10, c=30, e=1, d=40)


# def add_two(*args, **kwargs):
#     print(kwargs)
#     print(args)
#
#
# add_two(4, 5, 6)
# print()
# add_two(10, 20)
#
# add_two()
#
# add_two(10, 20, 30, d=40, e=50, f=10)


# def add_two(a, b=0, c=0):
#     print(a + b + c)
#
# add_two(10, c=30)
# add_two(10, 20)
# add_two(10, 20, 30)
# add_two(a=1)

''' write a function to count the number of positional and keyword arguments passed to it.'''

# def my_func(*args, **kwargs):
#     count = 0
#     print(args)
#     print(kwargs)
#     for _ in args:
#         count += 1
#     for _ in kwargs:
#         count += 1
#     return count
#
#
# print(my_func(1, 2, 3, 4, 5, a=10, b=20, c=30))
#
# print(my_func(1, 2, 3, 4, b=20, c=30))

''' return the first prime number in the given range '''


# def f_prime(a, b):
#     for n in range(a, b):
#         for i in range(2, n):
#             if n % i == 0:
#                 break
#         else:
#             return n
#     else:
#         return "No prime found"
#
#
# print(f_prime(24, 28))

''' upper() in functions '''
#
# def my_upper(s):
#     res = ''
#     for char in s:
#         if 'a' <= char <= 'z':
#             res += chr(ord(char) - 32)
#         else:
#             res += char
#     return res
#
#
# def my_lower(s):
#     res = ''
#     for char in s:
#         if 'A' <= char <= 'Z':
#             res += chr(ord(char) + 32)
#         else:
#             res += char
#     return res
#
#
# def my_title(s):
#     res = ''
#     res += my_upper(s[0])
#     for i in range(len(s)-1):
#         if 'A' <= s[i] <= 'Z' or 'a' <= s[i] <= 'z':
#             res += my_lower(s[i + 1])
#         else:
#             res += my_upper(s[i + 1])
#     return res
#
#
# print(my_title('hi h@lLo h0w are yoU'))

'''write a function to print msg "hai everyone" if the user input is not present '''


# def my_func(msg="hai Everyone"):
#     print(msg)
#
#
# my_func()

''' replicating max inbilt function '''


# def temp(msg):
#     return msg
#
#
# def my_max(var, func=temp):
#     for item in var:
#         maximum = item
#         break
#     for item in var:
#         if func(maximum) < func(item):
#             maximum = item
#     return maximum
#
#
# l = {10, 20, 34, 32, 45, 67, 81, 37}
# d = dict.fromkeys(l)
# s = 'hai hello how arre you how are you doing'
# print(my_max(l))
# print(my_max(d))
# print()
# print(my_max(s.split(), func=len))
# print(max(s.split(), key=len))


# def add(a: int, b: int) -> int:
#     return a + b
#
#
# print(add(10, 5))
# print(add(10.5, 3.5))
# print(add('hai', 'hello'))

''' numbers from 5 to 1 '''
# for i in range(5, 0, -1):
#     print(i)

# i = 5
# while i > 0:
#     print(i)
#     i -= 1

# def num(n):
#     print(n)


# for i in range(5, 0, -1):
#     num(i)
#
# def num(n):
#     if n == 1:
#         print(n)
#     else:
#         print(n)
#         num(n-1)
#         print(n)
# #
# # num(5)
#
# from sys import getrecursionlimit, setrecursionlimit
# print(getrecursionlimit())
# setrecursionlimit(100)
# print(getrecursionlimit())
# num(5)

''' write a recurssive function to calculate factorial of a given number .'''

# def my_fact(n):
#     if n < 0:
#         return 'Enter valid number'
#     elif n == 1 or n == 0:
#         return 1
#     else:
#         return n * my_fact(n-1)
#
#
# print(my_fact(5))
# print(my_fact(4))

''' calculate the sum of first n numbers '''
# def n_sum(n):
#     if n < 0:
#         return 'Enter valid number'
#     elif n == 0:
#         return 0
#     else:
#         return n + n_sum(n-1)
#
#
# print(n_sum(5))
# print(n_sum(10))

''' countdown from 10 to 1 '''
# from time import sleep
# def countdown(n):
#     if n <= 0:
#         print('Enter a valid number : ')
#     elif n == 1:
#         print(1)
#     else:
#         print(n)
#         sleep(0.5)
#         countdown(n-1)
#
#
# countdown(10)

''' find the sum of all the numbers in a list/tuple '''

# def ele_sum(var):
#     if len(var) == 1:
#         return var[0]
#     else:
#         return var[0] + ele_sum(var[1:])
#
#
# print(ele_sum([1, 2, 3, 4, 5]))

''' sum of all the digits in a numbers '''


# def digit_sum(n):
#     if n == 0:
#         return 0
#     return (n % 10) + digit_sum(n // 10)
#
#
# print(digit_sum(12345))

''' wap to reverse a given string'''

# def reverse_1(s):
#     if s:
#         return s[-1] + reverse_1(s[:-1])
#     else:
#         return ''
#
# def reverse_2(s):
#     if s:
#         return reverse_2(s[1:]) + s[0]
#     else:
#         return ''

# print(reverse_1('hello'))

''' fibonacci series '''
''' 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,..'''
# l = [0, 1]
# for i in range(10):
#     l.append(l[i]+l[i+1])
# print(l)

# i = 0
# n1 = 0
# n2 = 1
# while i < 10:
#     num = n1 + n2
#     print(num)
#     n1 = n2
#     n2 = num
#     i += 1
















