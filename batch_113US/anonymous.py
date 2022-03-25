# def even_odd(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
# print(even_odd(10))
#
# def evn_odd(n):
#     return n % 2 == 0
#
# print(evn_odd(11))

# check_ = lambda n: n % 2 == 0
# print(check_(10))

''' syntax: lambda arg1, arg2, arg3..: expression '''


# add_ = lambda a, b: a + b
# print(add_(10, 20))

# l = [1, 2, 3, 4]
# square = lambda a: a ** 2
# for item in l:
#     print(square(item))

# last_ = lambda var: var[-1]
# print(last_([10, 20, 40]))
# print(last_('hello'))

# sum_3 = lambda a, b, c: a + b + c
# print(sum_3(10, 20, 30))

# var = lambda *args: sum(args)
# print(var(1, 2, 3, 4))

# exp = lambda a, b: a ** 2 + b ** 2 + 2 * a * b
# print(exp(3, 4))

# pallindrome_ = lambda a: a == a[::-1]
# print(pallindrome_('malayalam'))
# print(pallindrome_('Python'))

# l = [1, 2, 3, 4, 5]
# square = lambda item: item ** 2
# res= []
# for element in l:
#     res.append(square(element))
# print(res)

# l = [1, 2, 3, 4, 5]
# square = lambda item: item ** 2
# print(list(map(lambda item: item ** 2, l)))

''' sum of corresponding elemts of two list '''
# l = [1, 2, 3, 4, 5, 6, 7]
# new = [10, 53, 76, 45, 23, 15, 67]
# my_sum = lambda a, b: a + b
# res = map(my_sum, l, new)
# print(res, list(res))

'''considring corresponding elements using map'''
# msg1 = 'hai'
# msg2 = 'are'
# my_zip = lambda a, b: (a, b)
# res = map(my_zip, msg1, msg2)
# print(res, dict(res))


''' element ** its index using map'''
# list_1 = [1, 2, 3, 4]
# res = map(lambda a, b: a ** b, list_1, range(len(list_1)))
# print(res, list(res))

''' filtering odd numbers using filer'''
# new = [10, 53, 76, 45, 23, 15, 67]
# func = lambda a : a % 2 != 0
# res = filter(func, new)
# print(res, list(res))

''' filtering even length string using filter'''
# l = ['alex', 'peter', 'bill', 'steve', 'george']
# func = lambda a: len(a) % 2 == 0
# res = filter(func, l)
# print(tuple(res))

''' filtering only odd numbers using filter '''
# l = [1, 2, 3, 4, 5, 6, 7]
# new = [10, 53, 76, 45, 23, 15, 67]
# odd = lambda a: a % 2
# res = filter(odd, new)
# print(list(res))

''' create a dict such that key should be the string and its length as its value'''
# l = ['alex', 'peter', 'bill', 'steve', 'george']
# func = lambda a: (a, len(a))
# res = map(func, l)
# print(dict(res))

''' create a list of names which are not starting with vowels'''
# l = ['alex', 'peter', 'bill', 'steve', 'george']
# func = lambda a: a[0].lower() not in 'aeiou'
# res = filter(func, l)
# print(list(res))


''' Program to print only even numbers in the range 1-50 '''
# res = filter(lambda a: a % 2 == 0, range(1,51))
# print(tuple(res))

'''Program to print only odd numbers in the range 1-50 '''
# res = filter(lambda a: a % 2 != 0, range(1,51))
# print(tuple(res))


'''Returns the string if the string is starting from vowel character'''
# names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']
# res = filter(lambda a: a[0].lower() in 'aeiou', names)
# print(list(res))

''' Program to return only positive values in the list '''
# numbers = [-2, -1, 0, 1, 2]
# res = filter(lambda a: a >= 0, numbers)
# print(list(res))
''' Program to print prime numbers from 1-50  '''
# def is_prime(n):
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#         else:
#             return 1
#     return False
#
# res = filter(is_prime, range(-1,51))
# print(list(res))


''' Write a Python program to convert negative numbers in a given list to positive numbers.'''
# numbers = [-2, -1, 0, 1, 2]
# res = map(abs, numbers)
# print(list(res))

'''Write a Python program to calculate the sum of the elements in the list and its index value'''
# new = [10, 53, 76, 45, 23, 15, 67]
# func = lambda a: a + new.index(a)
# res = map(func, new)
# print(list(res))

# new = [10, 53, 76, 45, 23, 10, 15, 67]
# func = lambda a: a[0] + a[1]
# res = map(func, enumerate(new))
# print(list(res))
# print(list(enumerate(new)))


''' write a program to get the element and negative index of the element in a tuple'''
# new = [10, 53, 76, 45, 23, 10, 15, 67]
# names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']
#
# res1 = map(lambda a: (a[0]-len(new), a[1]), enumerate(new))
# res2 = map(lambda a: (a[0]-len(names), a[1]), enumerate(names))
# print(list(res1), list(res2), sep='\n')

''' write a program to get the non duplicate elements only from the given list '''
# l = [10, 20, 10, 25, 67, 34, 20, 25, 78, 67, 89, 54]
# res = filter(lambda a: l.count(a) == 1, l)
# print(list(res))

s = 'TRACXN'
# print(s[::2], s[1::2])
# #'RCN' ,,, #'TAX'
# res = filter(lambda a: s.index(a) % 2 == 0, s)
# print(''.join(res))
# res_odd = filter(lambda a: s.index(a) % 2 != 0, s)
# print(''.join(res_odd))

# l = [10, 25, 4, 3, 8, 7]
# l.sort()
# print(l)

# names = ['alex', 'peter', 'jack', 'bob', 'bill']
# temp = names.copy()
# temp.sort()
# print(names)
# print(temp)

# names = ['alex', 'peter', 'jack', 'bob', 'bill']
# temp = sorted(names)
# print(temp, type(temp))
# print(names, type(names))

# names = ['alex', 'peter', 'jack', 'bob', 'bill']
# result = sorted(names, key=len, reverse=True)
# temp = sorted(names)
# print(names)
# print(temp)
# print(result)

''' sort based on length by defining your own function for length.'''
# names = ['apple', 'google', 'microsoft', 'facebook', 'instagram', 'yahoo', 'amazon']
# def length(iterable):
#     count = 0
#     for _ in iterable:
#         count += 1
#     return count
#
# result = sorted(names, key=length)
# print(result)

''' sort the list according to last char of each element '''
names = ['google', 'microsoft', 'facebook','apple', 'instagram', 'yahoo', 'amazon']
#
# def last_char(word):
#     return word[-1]
#
# result = sorted(names, key=last_char)
# print(result)

# result = sorted(names, key=lambda item: item[-1])
# print(result)

''' sort according to the temperature '''
# temperatures = [('Newyork', 12), ('Nashville', 10), ('LA', 25), ('Miami', 21)]
# result = sorted(temperatures, key=lambda item: item[-1])
# print(result)

''' sort according to the length of keys and get that as sorted dictionary '''
# temperatures = dict([('Newyork', 12), ('Nashville', 10), ('LA', 25), ('Miami', 21)])
# result = sorted(temperatures.items(), key=lambda a: len(a[0]))
# print(dict(result))

''' sort according to length of values '''
# new = dict([('Newyork', 'beautiful'), ('Nashville', 'awesome'), ('LA', 'wondeful'), ('Miami', 'great')])
# result = sorted(new.items(), key=lambda a: len(a[-1]))
# print(dict(result))

'''sort on the basing of values '''
# prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
# result = sorted(prices.items(), key=lambda a: a[-1], reverse=True)
# print(dict(result))

''' sort according to nearest value to 100'''
# prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
# result = sorted(prices.items(), key=lambda a: abs(100 - a[-1]))
# print(dict(result))

''' sort according to first char of key , and get it in the form of sorted dictionary'''
# prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
# result = sorted(prices.items(), key=lambda a: a[0][0])
# print(dict(result))










