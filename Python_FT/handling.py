
''' open, read, write, close '''

# file = open('fastrack.txt')
# print(file.writable())
#
# print(file.closed)
# file.close()
# print(file.closed)

# with open('fastrack.txt') as f:
#     for line in f:
#         print(line)
#     print(f.closed)
# print('outside')
# print(f.closed)

''' file_obj = open(file_name/file_path, mode)

with open(file_name/file_path, mode) as file_obj:
    pass
    '''
# company = ['apple', 'google', 'microsoft', 'tesla', 'netflix', 'amazon']

# with open('fastrack.txt', 'a') as file:
#     print(file.write("hi hello how are you\nHow are you doing?\nwhere are you from?"))
#     file.write('hello\n')
#     print(file.writelines({'hello\n', '10'}))


f_sample = r"C:\Users\HP\PycharmProjects\project_new\my_reference\files\sample.txt"
f_sample2 = r"C:\Users\HP\PycharmProjects\project_new\my_reference\files\sample2.txt"
#
# ''' count the number of words in the file '''
# with open(f_sample) as file:
#     count = 0
#     for line in file:
#         if line.strip():
#             count += 1
#
#     print(count)

''' count no of lines in sample.txt '''
# with open(f_sample) as file:
#     l = file.readlines()
#     count = 0
#     for i in l:
#         if i not in '\n':
#             count += 1
#     print(count)

''' print both line number as well as line '''
# with open(f_sample) as file:
#     line_no = 1
#     for line in file:
#         if line.strip():
#             print(line_no, line, end='')
#         line_no += 1

# with open(f_sample) as file:
#     for line_no, line in enumerate(file, start=1):
#         print(line_no, line, end='')

'''print the lines in reversed order '''
# with open(f_sample) as file:
#     for line in reversed(list(file)):
#         print(line, end='')
#
# print(dir(file))
# print(dir(list))

# with open(f_sample) as file:
#     count = 0
#     for line_no, line in enumerate(file, start=1):
#         if count < 10:
#             if line.strip():
#                 for i in line.split():
#                     if i in 'hello':
#                         print(line_no)
#                         count += 1
#                         if count == 10:
#                             break
#         else:
#             break
#
#     print(file.tell())

'''extract ip adresses from access-log.txt file'''
f_path = r"C:\Users\HP\PycharmProjects\project_new\my_reference\files\access-log.txt"
# with open(f_path) as f:
#     l = []
#     for line in f:
#         if line.strip():
#             if line.split()[0] not in l:
#                 l.append(line.split()[0])
#
# print(l)

''' create a dictioanary such that key as ip adress and its count as its value '''
# with open(f_path) as f:
#     d = {}
#     for line in f:
#         if line.strip():
#             temp = line.split()[0]
#             if temp not in d:
#                 d[temp] = 1
#             else:
#                 d[temp] += 1
#
# print(d)

# from collections import defaultdict
# with open(f_path) as f:
#     d = defaultdict(int)
#     for line in f:
#         if line.strip():
#             temp = line.split()[0]
#             d[temp] += 1
#
# print(d)

''' create a dict, key as group and value as list of counties belongs to that group '''
football = r"C:\Users\HP\PycharmProjects\project_new\my_reference\files\football.txt"
# with open(football, encoding="UTF-8") as file:
#     d = {}
#     for line_no, line in enumerate(file, start=1):
#         if line_no == 1:
#             continue
#         temp = line.split()[0]
#         country = line.split()[1]
#         if temp not in d:
#             d[temp] = [country]
#         elif country not in d[temp]:
#             d[temp].append(country)
# print(d)

# with open(football, encoding="UTF-8") as file:
#     s = {line.split('\t')[1] for line in file if line.strip()}
#     print(s)

# data = r"C:\Users\HP\PycharmProjects\project_new\my_reference\files\data.txt"
# fast = r"C:\Users\HP\PycharmProjects\project_new\Python_FT\fastrack.txt"
# with open(data) as file1:
#     with open(fast, 'w') as file2:
#         for line in file1:
#             file2.write(line)

import csv
# # csv_path = r"C:\Users\HP\PycharmProjects\project_new\my_reference\files\test.csv"
# # with open(csv_path) as file:
# #     rows = csv.DictReader(file)
# #     for item in rows:
# #         print(item)
#
# with open('fastrack.csv', 'w') as file:
#     csv_obj = csv.writer(file)
#     csv_obj.writerow(['name', 'company', 'salary'])
#     while True:
#         name = input('ENter name: ')
#         company = input('Enter company : ')
#         salary = input('Enter salary : ')
#         csv_obj.writerow([name, company, salary])
#         option = input('Enter 1 to add more data else enter * ')
#         if option != '1':
#             break

# def outer(func):
#     def inner(*args, **kwargs):
#         print('The Output is : ')
#         func(*args, **kwargs)
#     return inner
#
# @outer # add = outer(add)
# def add(a, b):
#     print(a + b)
#
# @outer # rev = outer(rev)
# def rev(s):
#     print(s[::-1])
#
# print(add(2, 4))
# print(rev('hello'))

# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res[::-1]
#     return wrapper
#
# @outer
# def reverse_(s):
#     return s
#
# print(reverse_('hello'))

# def outer(func):
#     def wrapper(m, n):
#         print('inside decorator')
#         return func(m, n)
#     return wrapper
#
# @outer
# def add(a, b):
#     return a + b
#
# @outer
# def sub(a, b):
#     return a - b
#
# print(add(10, 20))
# print(sub(11, 7))

# ''' write a decorator that counts the number of arguments given to the main function '''
# def outer(func):
#     def wrapper(*args, **kwargs):
#         print(len(args) + len(kwargs))
#         return func(*args, **kwargs)
#     return wrapper
#
# @outer
# def sum_(*args):
#     return sum(args)
#
# print(sum_(1, 2, 3, 4, 5))

# def para(n):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return outer
#
# @para(3)
# def welcome(s):
#     print(s)
#
# welcome('namskaara')
#
# @para(2)
# def greet(s):
#     print('Welcome,', s)
#
# greet('Akash')

''' wa dec to calculate the time taken for execution '''
import time
# d = {}
# def outer(func):
#     count = 0
#     def inner(*args, **kwargs):
#         nonlocal count
#         count += 1
#         f_name = func.__name__
#         func(*args, **kwargs)
#         d[f_name] = count
#         return d
#     return inner
#
# @outer
# def spam():
#     print('hello')
#
# print(spam())
# print(spam())
# print(spam())
# # print(count)
#
# @outerdef para(msg='Hello world'):
# #     def outer(func):
# #         def inner(*args, **kwargs):
# #             print(msg)
# #             func(*args, **kwargs)
# #         return inner
# #     return outer
# #
# # @para('Akaash')
# # def display():
# #     print('python')
# #
# # display()
# def add():
#     print(2 + 5)
#
# print(add())

#
























