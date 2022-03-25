# s = 'Hello Python'
# for char in s:
#     print(char, end='  ')

# company = ['apple', 'google', 'microsoft', 'tesla']
# for item in company:
#     print(item)

# company = ('apple', 'google', 'microsoft', 'tesla')
# for item in company:
#     print(item + '   hai')

# company = {'apple', 'google', 'microsoft', 'tesla'}
# for item in company:
#     print(item)
# print()
# d = dict.fromkeys(company, 'USA')
# d['apple'] = 100
# for key in d:
#     print(key, d[key])
# print(d)

''' printing numbers '''
# print numbers from 1 to 10:
# for num in range(1, 11):
#     print(num)

# for num in range(1, 10):
#     if num % 2 == 0:
#         print(num)

# for num in range(10):
#     print(num, end=' ')

# for item in range(1001, 1011):
#     print(item, end=' ')

# s = 'Hello Python'
# for index in range(len(s)):
#     print(s[index], index)

''' sum of n natural numbers '''
# n = int(input('Enter a number ', ))
# sum = 0
# for item in range(1, n+1):
#     sum += item
# print(sum)

''' sum of all the digits present in a number '''
# num = int(input('Enter a number :'))
# sum = 0
# for item in str(num):
#     sum += int(item)
# print(sum)

''' calculate the sum of all the numerical char present in a string '''
# msg = input('Enter any string ')
# sum = 0
# list_ = [ ]
# for char in msg:
#     if char.isnumeric():
#         sum += int(char)
#     else:
#         list_.append((char, ord(char)))
#
# print(sum)
# print(list_)

''' reversing a string '''
# msg = 'Hello Python'
# rev = ''
# for char in range(len(msg)-1, -1, -1):
#     rev += msg[char] # rev = rev + msg[char]
# print(rev)

# msg = 'Hello Python'
# rev = ''
# for char in range(len(msg)):
#     rev = msg[char] + rev
# print(rev)

''' wap to count the number of upper case char and lower case char '''
# s = 'HeLLo WorLd!'
# u_count = 0
# l_count = 0
# for char in s:
#     if char.isupper():
#         u_count += 1
#     elif char.islower():
#         l_count += 1
# print(u_count, l_count)

''' wap  to check whether a number is prime or not '''
# num = int(input('Enter a number : '))
# for item in range(2, num):
#     if num % item == 0:
#         print(f'{num} is not a prime ')
#         break
# else:
#     print(f'{num} is a prime')

# ''' first n prime numbers '''
# count = 0
# num = 2
# while count < 10:
#     for item in range(2, num):
#         if num % item == 0:
#             break
#     else:
#         print(num)
#         count += 1
#     num += 1
# print(count)

''' to get the maximum number '''
# example1 = [20, 35, 19, 17, 35.0, 30]
# max_ = 0
# for item in example1:
#     if item > max_:
#         max_ = item
# else:
#     print('loop executed')
# print(max_)

# example1 = [20, 35, 19, 17, 30]
# print(max(example1))
# print(min(example1))

# company = ['apple', 'apple', 'google', 'Yahoo', 'facebook', 'google', 'apple', 'microsoft', 'instagram', 'amazon', 'Uberrrr']
# print(max(company, key=len))
# company.sort(key=len)
# print(company)
# print(max(company))
# print(min(company, key=len))
# print(min(company))

''' create a list with only even length elements '''
# company = ['apple', 'google', 'Yahoo', 'facebook', 'google', 'apple', 'microsoft', 'instagram', 'amazon', 'Uberrrr']
# result = list()
# for item in company:
#     if item not in result: # To avoid duplicates.
#         if len(item) % 2 == 0:
#             result.append(item)
#             print(result)
#         else:
#             print(item)
#     else:
#         print('duplicate', item)
# print(result)

''' create a list where even length elements should be as it is, but odd length elements should reversed'''
# company = ['apple', 'google', 'Yahoo', 'facebook', 'google', 'apple', 'microsoft', 'instagram', 'amazon', 'Uberrrr']
# result = list()
# for element in company:
#     if len(element) % 2 == 0:
#         result.append(element)
#     else:
#         result.append(element[::-1])
# print(result)
# print(company)

''' modify the original list such that where even length elements should be as it is, but odd length elements should reversed'''
# for index in range(len(company)):
#     temp = company[index]
#     if len(temp) % 2:
#         company[index] = temp[::-1]
# print(company)

''' find sum of all the numeric data in the given list '''
# example = [10, 30.3, 'hello', 19, 30, 15, 10+5j]
# sum = 0
# for item in example:
#     if isinstance(item, (int, float, complex)):
#         sum += item
#     else:
#         print(type(item))
# print(sum)

''' create a list of elements where all the elements contain even number of vowels '''
# company = ['apple', 'google', 'Yahoo', 'facebook', 'google', 'apple', 'microsoft', 'instagram', 'amazon', 'Uberrrr']
# result_even = list()
# result_odd = list()
# for element in company:
#     count = 0
#     for item in element:
#         if item.lower() in 'aeiou':
#             count += 1
#     if count % 2 == 0:
#         result_even.append(element)
#     else:
#         result_odd.insert(0, element)
#         print(result_odd)
# print(result_odd)
# print(result_even)

''' create a dictionary with elements as key its length as value '''
# company = ['apple', 'google', 'Yahoo', 'facebook', 'google', 'apple', 'microsoft', 'instagram', 'amazon', 'Uberrrr']
# d = {}
# for item in company:
#     d[item] = len(item)
# print(d)

''' create a dictionary, elements as values and its position as key'''
# company = ['apple', 'google', 'Yahoo', 'facebook', 'google', 'apple', 'microsoft', 'instagram', 'amazon', 'Uberrrr']
# d = {}
# for index, item in enumerate(company):
#     d[index] = item
# print(d)

''' create a dict, elements as key and all its position as value in  a list'''
# company = ['apple', 'google', 'Yahoo', 'facebook', 'google', 'apple', 'microsoft', 'instagram', 'amazon', 'Uberrrr']
# d = {}
# for index, item in enumerate(company):
#     if item not in d:
#         d[item] = [index]
#         print(d)
#     else:
#         d[item] += [item]
#         print(d)
# print(d)

# s = 'hello'
# print(enumerate(s))
# print(list(enumerate(company)))
# print(list(enumerate(s)))
# for x, y in enumerate(s):
#     print(y, x)

#zip()
# words = ['one', 'two', 'three']
# num = [1, 2 , 3]
# zip_obj = zip(words, num)
# print(zip_obj)
# print(list(zip_obj))
# print(dict(list(zip_obj)))

# s = "hello"
# obj = zip(range(len(s)), s, range(len(s)))
# print(list(obj))

# words = ['one', 'two', 'three']
# num = [1, 2 , 3, 4]
# zip_obj = zip(num, words)
# print(zip_obj)
# print(list(zip_obj))

# from itertools import zip_longest
# zip_long = zip_longest(num, words, fillvalue='Python')
# print(zip_long)
# print(list(zip_long))

# files = ['youtube.txt', 'gmail.txt', 'gmail.pdf', 'amazon.pdf', 'apple.doc', 'flipkart.txt']
# print all the file name:
# for item in files:
#     temp = item.split('.')
#     print(temp[0])

# print only files with extension txt:
# for item in files:
#     temp = item.split('.')
#     print(temp)
#     if temp[1] in 'txt':
#         print(temp[0])

''' count the number of words in a sentence, using get method '''
# sentence = 'hello world welcome to python programming session hello world'
# var = sentence.split()
# d = dict.fromkeys(var, 1)
# count = 0
# for item in d:
#     if d.get(item):
#         count += 1
# print(count)

# d = {}
# var = sentence.split()
# for item in var:
#     d[item] = var.count(item)
# print(d)

# s = 'abracadabra'
# d = {}
# for item in s:
#     d[item] = s.count(item)
# print(d)

# for item in s:
#     if item not in d:
#         d[item] = 1
#     else:
#         d[item] += 1
# print(d)

# l1 = [1, 2, 3, 4]
# l2 = [10, 20, 30, 40]
# for item in zip(l1, l2):
#     print(item[0] * item[1])

# for first, second in zip(l1, l2):
#     print(first * second)

# sentence = 'python is a programming language programs are always interesting'
# d = {} # {'p' : ['python', 'programming', 'programs'], 'i':['is', 'interesting], ...}
# temp = sentence.split()
# for item in temp:
#     if item[0] not in d:
#         d[item[0]] = [item]
#     else:
#         d[item[0]] += [item]
# print(d)

# default dict
# from collections import defaultdict
# sentence = 'python is a programming language programs are always interesting'
# d = defaultdict(list)
# temp = sentence.split()
# for item in temp:
#     d[item[0]] += [item]
# print(d)


# sentence = 'python is a, programming language programs are always interesting'
# d = defaultdict(int)
# temp = sentence.split()
# for item in temp:
#     print(item)
#     d[item[0]] += 1
# print(d)


# str_ = "malayalam"
# # print(str_.index("a"))
# # print(str_.index("a", 2))
# # print(str_.index("a", 5))
# # print(str_.index("a", 7))
# for i in enumerate(str_):
#     # print(i)
#     if i[1] == "a":
#         print(i)

# a = "hello python"
# for i in a:
#     if i == "aeiou":
#         print(i)

# def func(a):
#     l = []
#     for i in a:
#         if i in "aeiou":
#             l.append(i)
#             print(l)
# func("hello python")

