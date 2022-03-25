# def func(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
# def func2(n):
#     return n % 2 == 0
#
#
# new_func = lambda n: n % 2 == 0
# print(new_func(5))

# sum_ = lambda a, b: a + b
# print(sum_(10, 20))

# square = lambda a: a * a
# for i in range(1, 11):
#     print(square(i))

''' syntax: lambda arg1, arg2, ...: expression '''

# reverse_ = lambda i: i[::-1]
# print(reverse_('hello'))

# exp = lambda a, b: a ** 2 + b ** 2 + 2 * a * b
# print(exp(3, 4))

# palindrome_ = lambda s: s == s[::-1]
# print(palindrome_('hello'))
# print(palindrome_('mom'))

# l = {10, 32, 47, 11, 7, 5, 17, 23}
# res = []
# square = lambda a: a * a
# for i in l:
#     res.append(square(i))
# print(res)

# square = lambda a, b: a * b
# res = map(lambda a, b: a + b, l, range(1))
# print(list(res))

# def square(a):
#     print(a)
#     return a * a
#
# res =  map(square, l)
# print(list(res))

''' sum of corresponding elements of two lists '''
# l = [1,2 , 3, 4, 5]
# m = [11, 12, 13, 14, 15]
# res = map(lambda a, b: a + b, l, m)
# print(list(res))

''' create map object which is similar to zip object '''
# res = map(lambda a, b: (a, b), [1, 2, 3, 4, 5], 'hello')
# print(list(res))
#
# res = map(lambda *args: [*args], [1, 2, 3, 4, 5], 'hello', 'hai')
# print(list(res))
#[[1, 'h', 'h'], [2, 'e', 'a'], [3, 'l', 'i']]

''' element ** index , using map '''
# l = [1, 2, 3, 2, 4, 2, 5, 3]
# res = map(lambda a, b: a ** b, l, range(len(l)))
# print(list(res))
#
# res = map(lambda a, b: a ** b[0], l, enumerate(l))
# print(list(res))
#
# res = map(lambda a: a[-1] ** a[0], enumerate(l))
# print(list(res))

''' filter all the even numbers'''
# l = [10, 53, 76, 45, 23, 15, 67]
# res = [i for i in l if i % 2 != 0]
# print(res)

# res = filter(lambda a: a % 2 != 0, l)
# print(list(res))

''' filter even length word in the below string'''
# s = 'python is a programming language and programs are always interesting'
# res = filter(lambda i: len(i) % 2 != 0, s.split())
# print(list(res))

'''create a dictionary such that key should be the word and its len should be its value'''
# s = 'python is a programming language and programs are always interesting'
# res = map(lambda a: (a, len(a)), s.split())
# print(dict(res))

''' create a list of names which are not starting with vowels '''
# s = 'python is a programming language and programs are always interesting'
# res = filter(lambda a: a[0].lower() not in 'aeiou', s.split())
# print(list(res))

''' create a list of words, such that if len is even the keep it as its is, else reverse it.'''
# s = 'python is a programming language and programs are always interesting'
# res = map(lambda a: a if len(a) % 2 == 0 else a[::-1], s.split())
# print(list(res))

''' wap to get the element and the negatve index of that element in a tuple '''
# l = [10, 23, 43, 56, 21, 77, 41, 10]
# res = map(lambda a: (a[1], a[0] - len(l)), enumerate(l))
# print(list(res))

''' wap to get only the non duplicate values from given list '''
# l = [10, 23, 43, 56, 21, 77, 41, 10, 43, 77, 81]
# res = filter(lambda a: l.count(a) == 1, l)
# print(list(res))

''' s = TRACXN , get output as 'TAX' and 'RCN' .'''
# s = "TRACXN"
# res = filter(lambda a: s.find(a) % 2 == 0, s)
# print(''.join(res))
# res_o = filter(lambda a: s.find(a) % 2 != 0, s)
# print(''.join(res_o))


###################
# l = (10, 23, 41, 56, 71, 35, 28)
# # l1 = l[:]
# # l1.sort()
# # print(l)
# print(sorted(l))
# print(l)
#
# s = 'python is a programming language'
# print(sorted(s))

# d = dict.fromkeys(s.split(), 'value')
# print(d)
# print(sorted(d, key=len))

'''sort based on len by defining ur own function for length '''
# company = ['apple', 'google', 'microsoft', 'tesla', 'netflix', 'amazon']
#
#
# def len_(a):
#     count = 0
#     for _ in a:
#         count += 1
#     return count
#
#
# print(sorted(company, key=len_))

# ''' sort based on last char of element '''
# company = ['apple', 'google', 'microsoft', 'tesla', 'netflix', 'amazon']

# def last_(a):
#     return a[-1]


# print(sorted(company, key=lambda a: a[-1]))

''' sort the below list based on temeperatures'''
# temperatures = [('banagalore', 28), ('mysore', 32), ('chennai', 37), ('munnar', 22)]

# print(sorted(temperatures, key=lambda a: a[-1]))

'''sort the below list according to their sum of numbers inside them'''
# l = [[1, 2, 3], [2, 7], [2, 5, 1], [3, 8], [2, 10], [1, 3, 5]]
#
# print(sorted(l, key=lambda a: sum(a)))

''' sort based on len of keys '''
# d = {'banagalore': 28, 'mysore': 32, 'chennai': 37, 'munnar': 22}

# res = sorted(d.items(), key=lambda a: len(a[0]))
# print(dict(res))

# new = {'banagalore': 'beautiful', 'mysore': 'marvolus', 'chennai': 'super', 'munnar': 'cool'}
# res = sorted(new.items(), key=lambda a: len(a[1]))
# print(dict(res))
# res2 = sorted(new.items(), key=lambda a: a[-1][-1])
# print(dict(res2))

# shares = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'TATAMOTORS': 400.51, 'HP': 10.75}
# res = sorted(shares.items(), key=lambda a: abs(100 - a[-1]))
# print(dict(res))

a = 20
company = ['apple', 'google', 'microsoft', 'tesla', 'netflix', 'amazon']
print('in lambda file')
















