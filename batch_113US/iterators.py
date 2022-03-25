# def spam():
#     print('inside function')
#     yield 'hello'
#     print('2nd yield value')
#     yield 10
#     yield 4.5
#
# res1 = spam()
# # res2 = spam()
# # print(dir(res1))
# # print(dir(list))
# print(next(res1))
# print(next(res1))
# # for item in res2:
# #     print('in for loop ')
# #     print(item)
# print(next(res1))
import time

_ = ""
''' to get numbers from 10 to 1 '''
# func
# def nums():
#     l = []
#     for i in range(10, 0, -1):
#         l.append(i)
#     return l
#
# print(nums())
#
# #generator func
# def nums():
#     for i in range(10, 0, -1):
#         yield i
#
# numbers = nums()
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print()
# print(list(numbers))

''' write a gen func that produces even numbers from 1 to n '''
# n = int(input('Enter a number : '))

# def normal(n):
#     for i in range(1, n+1):
#         if i % 2 == 0:
#             print(i)
#
# normal(n)


# def gen_even(num):
#     for i in range(1, num):
#         if i % 2 == 0:
#             yield i
#
#
# obj = gen_even(n)
# for item in obj:
#     print(item)

# f_path = r"C:\Users\HP\PycharmProjects\project_new\batch_113US\files\sample.txt"
# def line():
#     with open(f_path) as file:
#         for i in file:
#             if i.strip():
#                 yield i
#
# obj = line()
# print(obj)
# for element in obj:
#     print(element, end="")
#
# obj1 = (item for item in open(f_path) if item.strip())
# print(obj1)
# print(next(obj1))
# print(next(obj1))
# for item in obj1:
#     print(item, end="")

# l = ['apple', 'amazon', 'google', 'netfilx', 'microsoft', 'facebook']
# odd length word - not include them, even - reverse them and include.

# def rev_even(n):
#     for item in n:
#         if len(item) % 2 == 0:
#             yield item[::-1]

# obj = rev_even(l)
# print(obj)
# for i in obj:
#     print(i)

# exp = (item[::-1] for item in l if len(item) % 2 == 0)
# print(exp)
# for x in exp:
#     print(x)

# new = (item[::-1] if len(item) % 2 == 0 else item for item in l)
# print(new)
# for y in new:
#     print(y)

# new = (item[::-1] if len(item) > 6 else item for item in l if len(item) % 2 == 0)
# print(new)
# for y in new:
#     print(y)


''' create a gen obj which wll be having dictionary of keys country and 
its total vaccination details from vaccination.csv '''
# path = r"C:\Users\HP\PycharmProjects\project_new\batch_113US\files\vaccination_data.csv"
#
# import csv
# import time
# def func():
#     with open(path) as file:
#         start = time.time()
#         csv_obj = csv.reader(file)
#         temp = next(csv_obj) # to get the first line element
#         for item in csv_obj:
#             time.sleep(0.1)
#             yield {temp[0]: item[0], temp[5]: item[5]}
#         end = time.time()
#         yield end - start
#
#
# gen = func()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# for i in gen:
#     print(i)

path = r"C:\Users\HP\PycharmProjects\project_new\batch_113US\files\vaccination_data.csv"

# import csv
# import time
# def func():
#     with open(path) as file:
#         sum = 0
#         start = time.time()
#         csv_obj = csv.reader(file)
#         temp = next(csv_obj) # to get the first line element
#         for item in csv_obj:
#             if item[5].strip():
#                 sum += int(item[5])
#         yield sum
#         end = time.time()
#         yield end - start
#
# obj = func()
# print(next(obj))
# print(next(obj))

''' get all the details of the employees who will be getting more 50000 pay in employee.csv'''
# emp_path = r"C:\Users\HP\PycharmProjects\project_new\batch_113US\files\employees.csv"
# import csv
# def details():
#     with open(emp_path) as file:
#         obj = csv.DictReader(file)
#         for item in obj:
#             if int(item['pay']) > 75000:
#                 yield item
#
# d = details()
# for i in d:
#     print(i)



















