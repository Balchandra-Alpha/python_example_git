# l = [1, 2, 3, 4, 5]
# s = 'hello'
# d = {}.fromkeys(s)
# print(d)
# for i in reversed(d):
#     print(i)

# l = [1, 2, 3, 4, 5]
# new = [i ** 2 for i in l]
# print(new)

''' create a list which starts from vowels'''
# company = ['apple', 'google', 'microsoft', 'google', 'apple', 'amazon', 'netflix', 'apple', 'google']
# new = [item for item in company if item[0].lower() in 'aeiou']
# print(new)

''' create list which consists of elements whose len is more than 5'''
# company = ['apple', 'google', 'microsoft', 'google', 'apple', 'amazon', 'netflix', 'apple', 'google']
# new = [item for item in company if len(item) > 5]
# print(new)

''' '''
# s = input('Enter a word')
# if len(s) % 2 == 0:
#     print(s)
# else:
#     print(s[::-1])
# print(s) if len(s) % 2 == 0 else print(s[::-1])

'''create a ;list such that even length element should be as it is, odd length element
should be reversed .'''
# company = ['apple', 'google', 'microsoft', 'google', 'apple', 'amazon', 'netflix', 'apple', 'google']
# new = [item if len(item) % 2 == 0 else item[::-1] for item in company]
# print(new)
#
# even = [i for i in range(1, 51) if i % 2 == 0]
# print(even)

''' create a list which have remainders when elements of specified list is divisible by 3'''
# l = [3, 9, 11, 16, 19, 23]
# new = [item % 3 for item in l ]
# print(new)

'''create a list with elements whose last digit is divisible by 3'''
# nums = [1234, 3421, 1423, 1756, 7869, 4576]
# new = [item for item in nums if (item % 10) % 3 == 0]
# print(new)

'''create a list with elements starting with alphabet p '''
# language = ['python', 'PHP', 'Java', 'C++', 'Python', 'perl', 'JS']
# new = [i for i in language if i.startswith('p') or i.startswith('P')]
# print(new)

''' create list of tuples with element and its length pair using given list'''
# company = ['apple', 'google', 'microsoft', 'google', 'apple', 'amazon', 'netflix', 'apple', 'google']
# new = [(i, len(i)) if len(i) % 2 == 0 else False for i in company if i[0].lower() not in 'aeiou']
# print(new)

# new = [int(str(i) + str(j)) for i in range(1, 4) for j in range(1, 4) if i != j]
# print(new)

'''create a list with elements such that if ending with vowels add as it is, if ending with consonants then add 'hello' '''
# company = ['apple', 'google', 'microsoft@', 'google0', 'apple', 'amazon', 'netflix', 'apple2', 'google']
# new = [i if i[-1].lower() in 'aeiou' else 'hello' for i in company if i.isalpha()]
# print(new)
# s = {(i,) if i[-1].lower() in 'aeiou' else 'hello' for i in company if i.isalpha()}
# print(s)

company = ['apple', 'google', 'microsoft', 'google', 'apple', 'amazon', 'netflix', 'apple', 'google']
# l = []
# for i in company:
#     if i in l:
#         continue
#     else:
#         l += [i]
# print(l)

# new = [i for i in company if not company.count(i) > 1]
# print(new)

# s = {i for i in company}
# print(s)

# l = [1, 2, 3, 4, 5, 3, 4]
# d = {}
# for x, y in enumerate(l):
#     d[x] = y
# print(d)
#
# new = {i[0]: i[-1] for i in enumerate(l)}
# print(new)

''' create a dictionary with only repeated char of specified string as key, and iits count as value'''
# s = 'Hai Hello How are you gentlemen'
# d = {}
# for i in s:
#     if s.count(i) > 1:
#         d[i] = s.count(i)
# print(d)
#
# new = {i: s.count(i) for i in s if s.count(i) > 1}
# print(new)

''' create dictionary of words as its key and its length as its value '''
# s = 'Hai Hello How are you gentlemen how come you are here'
# d = {}
# for i in s.split():
#     d[i] = len(i)
# print(d)
#
# new = {i: len(i) for i in s.split()}
# print(new)

''' flip the keys and values '''
# d = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# d1 = {}
# for i in d.items():
#     d1[i[1]] = i[0]
# print(d1)
#
# new = {i[1]: i[0] for i in d.items()}
# print(new)

'''wap to create a dict, if the element is string then reverse it for the value , else put
'not string' as value'''
# l = ['hello', 10, 45.7, 'python', True, 45, 'string', 1, 100]
# d = {}
# for i in l:
#     if isinstance(i, str):
#         d[i] = i[::-1]
#     else:
#         d[i] = 'Not String'
# print(d)
#
# new = {i: i[::-1] if isinstance(i, str) else 'Not string' for i in l}
# print(new)

# s = 'hello@123'
# d = {i: ord(i) for i in s}
# # print(d)
#
# '''Creating Dictionary of city and population pairs using Dict Comprehension '''
# cities = ['Tokyo',
#           'Delhi',
#           'Shanghai',
#           'Sao Paulo',
#           'Mumbai'
#           ]
# population = ['38,001,000',
#               '25,703,168',
#               '23,740,778',
#               '21,066,245',
#               '21,042,538'
#               ]
# d = {city: ppl for city, ppl in zip(cities, population)}
# print(d)

''' Create a dictionary of dialcode and country from the following list '''
# dial_codes = [
#     (86, 'China'),
#     (91, 'India'),
#     (1, 'United States'),
#     (62, 'Indonesia'),
#     (55, 'Brazil'),
#     (92, 'Pakistan'),
#     (880, 'Bangladesh'),
#     (234, 'Nigeria'),
#     (7, 'Russia'),
#     (81, 'Japan')
#     ]
# print(dict(dial_codes))

''' Building a dictionary whose price value is more than 200'''
# prices = {
#     'ACME': 45.23,
#     'AAPL': 612.78,
#     'IBM': 205.55,
#     'HPQ': 37.20,
#     'FB': 10.75
# }
#
# d = {x: y for x, y in prices.items() if y > 200}
# print(d)

s = 'python is a programming language programs are always interesting'
# {(python, programming, programs): 'p', (is, interesting):'i', ..}

# d = {}
# for i in s.split():
#     if i[0] not in d:
#         d[i[0]] = (i,)
#     else:
#         d[i[0]] += (i,)
# print(d)




