# s = 'string'
# count = 0
# for _ in s:
#     count += 1
# print(count)
# # some othe code
#
#
# new = 'hi hello how are you'
# count = 0
# for _ in new:
#     count += 1
# print(count)
#
# l = [1, 2, 3, 4, 5]
# count = 0
# for _ in l:
#     count += 1
# print(count)


# def my_len(var):
#     count = 0
#     for _ in var:
#         count += 1
#     print('length of given iterable is ', count)
#
#
# new = 'hi hello how are you'
# l = [1, 2, 3, 4, 5]
# msg = 'string'
# my_len(new)
# my_len(l)
# my_len(msg)

# def greet(a):
#     print(f'Hello,{a} Welcome to our home')
#
# greet('Arjun')
# greet()


# def my_len(var):
#     count = 0
#     for _ in var:
#         count += 1
#     # print('length of given iterable is ', count)
#     return count, var
#
#
# a = my_len('hello')
# print(my_len('python'))
# print(a)
# print(id(my_len))
# print(a)

# def add(a, b):
#     c = a + b
#     return c
#
#
# _sum = add(2, 3)
# print('_sum :',_sum)
#
# print(add(10, 20))

#positional argument
# def greet(name, age):
#     print(f'hi, {name}, your age is {age}')
#
#
# greet('Sharukh', 50)
# greet(50, 'sharukh')
# greet(50, 40, 30)

#keyword argument and default arg
# def greet(age, name):
#     print(f'hi, {name}, your age is {age}')
#
#
# greet(age=48, name='Arjun')
# greet(name='', age='num')

#combination of positional and keyword
# def greet(name, age, phno, place):
#     print(f'hi, {name}, your age is {age},and {phno}')
#     print(f'You live in {place}')


# greet(10, 20, place=40, phno=30)
# greet(10, 20, name=40, phno=30)
# positional arg must present first, after that keyword arguments can be present
# greet(name=40, 20, 40, place=30)
#SyntaxError: positional argument follows keyword argument
# print('hello', 'hai', 'hello', sep="#", end='&')

# def greet(name, age,/, *, phno, place):
#     print(f'hi, {name}, your age is {age},and {phno}')
#     print(f'You live in {place}')
#
# greet('Arjun', 20, phno=1234, place='india')

# def add_(*args):
#     print(args)
#     print(sum(args))
#
#
# add_(10)
# add_(10, 20)
# add_(10, 20, 30)
# add_(10, 20, 30, 40)
# add_(1, 2, 3, 4, 5, 6)

# def add_(**kwargs):
#     print(kwargs)
#
#
# add_(p1='hello', p2='@', p3='world', p4='Good morning')
# add_(p1='hello', p2='@')

#function annotations
# def greet(name: str, age : int, phno :int, place : str) -> str:
#     print(f'hi, {name}, your age is {age},and {phno}')
#     print(f'You live in {place}')
#     return 'hello'
#
#
# print(greet('Arjun', 20, 1234, 'USA'))


# def add_(a, b):
#     print('hello')
#     return a + b, 'the sum'
#
#
# var = add_(5, 10)
# print(var)
# print(type(var))
# print(add_(10, 20))

# def my_func(a):
#     count = 0
#     for _ in a:
#         count += 1
#     print(count, ' inside function')
#     return count
#
#
# print(my_func('hello'))
# s = input("hello enter something: ")
# for i in range(len(s)):
#     print(i)


# s = 'hello world'
# var = my_func(s)
# print(my_func(s))
# for item in range(my_func(s)):
#     print(s[item])
# print(var , 'var value')


''' waf to calculate the sum of all the numbers(int, float) in an iterable'''

# def numeric_sum(var):
#     res = 0
#     if isinstance(var, str):
#         for item in var:
#             if item.isnumeric():
#                 res += int(item)
#     else:
#         for item in var:
#             if isinstance(item, (int, float)):
#                 res += item
#     return res
#
#
# l = [23, 45, 6.45, 'hello007', [1, 2, 3]]
# print(numeric_sum(l))
#
# print(numeric_sum('hello067'))


''' waf such that it should return the number of special char in a string '''
# def spl_func(s):
#     count = 0
#     for item in s:
#         if not item.isalnum():
#             count += 1
#     return count
#
#
# print(spl_func(s="hello@1342&%$"))
# print(spl_func('!@#$%^&*()Python*&^%'))

'''waf to replicate max and min inbuilt function '''
# l = ['hello', 'hai', 'how', 'are', 'Python', 'apple', 'zoogle']
# maximum = ''
# for item in l:
#     if maximum < item:
#         maximum = item
# print(maximum)
#
# l = [1, 10, 15, 67, 89, 45, 65]
# maximum = 0
# for item in l:
#     if maximum < item:
#         maximum = item
# print(maximum)

#
# def my_max(l):
#     if isinstance(l[0], (int, float)):
#         maximum = 0
#         for item in l:
#             if maximum < item:
#                 maximum = item
#         return maximum
#     elif isinstance(l[0], str):
#         maximum = ''
#         for item in l:
#             if maximum < item:
#                 maximum = item
#         return maximum
#
#
# l1 = ['hello', 'hai', 'how', 'are', 'Python', 'apple', 'zoogle']
# print(my_max(l1))
# l2 = [1, 10, 15, 67, 89, 45, 65]
# print(my_max(l2))


''' waf which takes variable number of arguments and return how many arguments were given'''

# def my_arg(*args, **kwargs):
#     count = 0
#     for item in args:
#         count += 1
#     for item in kwargs:
#         count += 1
#     return count


# print(my_arg(1, 2, 3, 4, 5))
# print(my_arg(1, 2, 3, 4, 5, a=12, b=15))
#
# def my_sum(*args):
#     sum_value = 0
#     for item in args:
#         sum_value += item
#     return sum_value
#
# print(my_sum(1, 2, 3, 4, 5))

''' waf to check whether a number is prime or not '''
# def my_prime(num):
#     for item in range(2, num):
#         if num % item == 0:
#             return 'Not prime'
#     else:
#         return 'prime'
#
#
# print(my_prime(11))
# print(my_prime(15))

'''waf to check whether a string is anagram or not '''
# def is_anagram(s1, s2):
#     temp1 = list(s1)
#     temp2 = list(s2)
#     temp1.sort()
#     temp2.sort()
#     if temp1 == temp2:
#         return 'anagram'
#     else:
#         return 'not anagram'
#
#
# print(is_anagram('cat','act'))
# print(is_anagram('night', 'thing'))

# ''' waf ro print msg 'Hai everyone' if the user input is not present '''
# def greet(*, msg='Hai everyone'):
#     print(msg)
#
#
# greet(msg='hello')
# greet(msg='hai')
# greet()

''' waf which takes variable number of positional arg as input, and returns
whether the number of arguments that are passsed are more than 5 or not.'''

# def check_(*args):
#     temp = 0
#     for _ in args:
#         temp += 1
#     if temp > 5:
#         return F'More than 5, given {temp} no of arguments'
#     else:
#         return f'Not more than 5,  given {temp} no of arguments'

# print(check_(1, 2, 3, 4))
# print(check_(10, 20, 30, 40, 50, 60))
# print(check_('1', '2', '3', '4', '5'))





























