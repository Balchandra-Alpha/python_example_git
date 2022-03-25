''' creating a list of squares of element of specified list '''
# num = [1, 2, 3, 4, 5]
# using for loop
# square = []
# for item in num:
#     temp = item ** 2
#     square.append(temp)
# print(square)
#
# using list comprehension
# square = [item ** 2 for item in num if item % 2 ]
# print(square)

# ''' wap to return a list of names starting with vowels '''
# company = ['apple', 'google', 'Yahoo', 'facebook', 'microsoft', 'instagram', 'amazon', 'Uberrrr']
# res = []
# for item in company:
#     if item[0].lower() in 'aeiou':
#         res.append(item)
# print(res)
#
# using list comprehension
# req_list = [item for item in company if item[0].lower() in 'aeiou']
# print(req_list)

# ''' wap to return list of names not starting with vowels'''
# company = ['apple', 'google', 'Yahoo', 'facebook', 'microsoft', 'instagram', 'amazon', 'Uberrrr']
# res = []
# for item in company:
#     if item[0].lower() not in 'aeiou':
#         res.append(item)
# print(res)
#
# using list comprehension
# req_list = [item for item in company if item[0].lower() not in 'aeiou']
# print(req_list)

''' create a list by rising the index as its pow to the elements in specified tuple'''
# t = (1, 2, 3, 4, 5)
# list_ = []
# for num in t:
#     temp = num ** t.index(num)
#     list_.append(temp)
# print(list_)
#
# req_list = [num ** t.index(num) for num in t]
# print(req_list)

# t = (1, 2, 3, 4, 5, 2)
# list_ = []
# for index, num in enumerate(t):
#     temp = num ** index
#     list_.append(temp)
# print(list_)
#
# req_list = [num ** index for index, num in enumerate(t)]
# print(req_list)

''' create a list of even numbers between 1 and 50'''
# even = []
# for item in range(1, 50):
#     if item % 2 == 0:
#         even.append(item)
# print(even)
#
# req_list = [item for item in range(1, 50) if item % 2 == 0]
# print(req_list)

# ''' create a list which have remainders when elements of specified list is divided by 3'''
# var = [3, 9, 11, 16, 19, 23]#==>  [0, 0, 2, 1, 1, 2]
# res = []
# for item in var:
#     temp = item % 3
#     res.append(temp)
# print(res)
#
# req_list = [item % 3 for item in var]
# print(req_list)

# '''create a list such that if length of element is even keep it as it is, reverse if its odd'''
# company = ['apple', 'google', 'Yahoo', 'facebook', 'microsoft', 'instagram', 'amazon', 'Uberrr']
# res = []
# for item in company:
#     if len(item) % 2 == 0:
#         res.append(item)
#     else:
#         res.append(item[::-1])
# print(res)
#
# req_list = [item if len(item) % 2 == 0 else item[::-1] for item in company]
# print(req_list)

# ''' create a list with elements starting with vowels and if its len is odd reverse it else keep it as it is'''
# company = ['apple', 'google', 'Yahoo', 'facebook', 'microsoft', 'instagram', 'amazon', 'Uberrr']
# res = []
# for item in company:
#     if item[0].lower() in 'aeiou':
#         if len(item) % 2 == 0:
#             res.append(item)
#         else:
#             res.append(item[::-1])
# print(res)
#
# req_list = [item if len(item) % 2 == 0 else item[::-1] for item in company if item[0].lower() in 'aeiou']
# print(req_list)

'''create a list which should not contain any language which starting with 'p' from specified list '''
# languages = ['Python', 'Java', 'Perl', 'PHP', 'Python', 'JS', 'C++', 'Ruby']

# ''' create a list with elements only have less than 6 character in it from specified tuple'''
# company = ('apple', 'google', 'Yahoo', 'facebook', 'microsoft', 'instagram', 'amazon', 'Uber')
# req_list = [item for item in company if len(item) < 6]
# print(req_list)

# '''build a list of tuples with element and its len pair from the specified list'''
# company = ['apple', 'google', 'Yahoo', 'facebook', 'microsoft', 'instagram', 'amazon', 'Uber']
# req_list = [(item, len(item)) for item in company]
# print(req_list)

''' build a list with only even len element '''
# company = ['apple', 'google', 'Yahoo', 'facebook', 'microsoft', 'instagram', 'amazon', 'Uber']
#
# ''' reverse the item of specifed list if te item is of odd length'''
# company = ['apple', 'google', 'Yahoo', 'facebook', 'microsoft', 'instagram', 'amazon', 'Uber']
# req_list = [item[::-1] for item in company if len(item) % 2 != 0]
# print(req_list)

# ''' reverse the item of specifed list if te item is of odd length, else keep it as it '''
# company = ['apple', 'google', 'Yahoo', 'facebook', 'microsoft', 'instagram', 'amazon', 'Uber']
# req_list = [item if len(item) % 2 == 0 else item[::-1] for item in company]
# print(req_list)

# ''' create a list with elements such that if ending with vowels as it is, if ending with consonants then add 'hello' '''
# company = ['apple', 'google', 'Yahoo0', 'facebook', 'microsoft@', 'instagram', 'amazon10', 'Yahoo', 'Uber']
# # o/p ==> ['apple', 'google', 'hello', 'hello', 'Yahoo', 'hello']
# req_list = {item if item[-1].lower() in 'aeiou' else 'hello' for item in company if item[-1].isalpha()}
# print(req_list)
# print(type(req_list))

''' Dictionary Comprehension '''

# ''' create a dictionary with only repeated char of specified string as keys and its count as values '''
# s = 'Hai hello How are you gentlemen'
# d = {}
# for item in s:
#     if s.count(item) > 1:
#         d[item] = s.count(item)
# print(d)
#
# req_dict = {item: s.count(item) for item in s if s.count(item) > 1}
# print(req_dict)

# ''' create a dictionary of words as keys in the given sentence and its length as value '''
# s = 'Hai hello How are you gentlemen How come you are here'
# d = {}
# for item in s.split():
#     d[item] = len(item)
# print(d)
#
# req_dict = {item: len(item) for item in s.split()}
# print(req_dict)

# ''' flip the keys and values '''
# d = {'one': 1, 'two': 2, 'three': 3, 'ten': 10}
# req_dict = {item[-1]: item[0] for item in d.items()} #item = (key, value)
# print(req_dict)
#
# d = {'one': 1, 'two': 2, 'three': 3}
# req_dict = {value: key for key, value in d.items()} #
# print(req_dict)
#
# d = {'one': 1, 'two': 2, 'three': 3}
# new = {}
# for key, value in d.items():
#     new[value] = key
# print(new)

# ''' wap to create a dict , if the element is string then reverse it for value else put "Not str" as value'''
# a = ['hello', 10, 45.7, 'python', True, 45, 'string', '100']
# d = {}
# for item in a:
#     if isinstance(item, str):
#         d[item] = item[::-1]
#     else:
#         d[item] = 'Not str'
# print(d)
#
# req_dict = {item: item[::-1] if isinstance(item, str) else 'Not str' for item in a}
# print(req_dict)

''' create a dictionary char and its ASCII value pair '''
# s = 'abcABC'
# req_dict = {item: ord(item) for item in s}
# print(req_dict)

'''# Creating Dictionary of city and population pairs using Dict Comprehension '''
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
# d = {}
# for item in zip(cities, population):
#     d[item[0]] = item[-1]
# print(d)
#
# req = {city: count for city, count in zip(cities, population)}
# print(req)


# ''' Create a dictionary of dialcode and country from the following list '''
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
# d = {}
# for code, country in dial_codes:
#     d[code] = country
# print(d)
#
# result = {item[0]: item[1] for item in dial_codes}
# print(result)


# ''' Building a dictionary whose price value is more than 200'''
# prices = {
#     'ACME': 45.23,
#     'AAPL': 612.78,
#     'IBM': 205.55,
#     'HPQ': 37.20,
#     'FB': 10.75
# }
#
# d = {}
# for item in prices:
#     if prices[item] > 200:
#         d[item] = prices[item]
# print(d)
#
# req_dict = {item: prices[item] for item in prices if prices[item] > 200}
# print(req_dict)

s =