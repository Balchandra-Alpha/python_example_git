# def spam():
#     print('python')
#     yield 'hello'
#     print('programming')
#     yield 10
#     yield 20
#
# res = spam()
# print(next(res))
# print(next(res))
# print(next(res))
# # print(next(res))
# print(list(spam()))
#
# print()
#
# # l = [0, 1, 2, 3, 4]
# def num():
#     for i in range(5):
#         yield i
# res1 = num()
# print(next(res1))
# print(next(res1))
# print(list((res1)))

# def nums():
#     for i in range(10, 0, -1):
#         print(i)
#
# nums()

# def nums():
#     for i in range(10, 0, -1):
#         yield i
#
# r = nums()
# for item in r:
#     print(item)

# def nums(n):
#     for i in range(1, n):
#         if i % 2 == 0:
#             yield i
#
# res = nums(20)
# print(next(res))
# print(next(res))
# print(next(res))
# for item in res:
#     print(item, end=' ')

# company = ['amazon', 'flipkart', 'apple', 'google', 'instagram']
# def func(n):
#     for i in n:
#         if i[0].lower() in 'aeiou':
#             yield {i: len(i)}
#
# res = func(company)
# print(res)
# for item in res:
#     print(item)

#generator expression :
# res1 = (item for item in company if item[0].lower() in 'aeiou')
# print(res1)
# for item in res1:
#     print(item)


# f_path = r"C:\Users\HP\PycharmProjects\project_new\batch_113US\files\test.csv"
# import csv
# def share_details():
#     with open(f_path) as file:
#         rows = csv.DictReader(file)
#         for item in rows:
#             yield item
#
# res = share_details()
# for item in res:
#     print(item)

# vaccination_path = r"C:\Users\HP\PycharmProjects\project_new\batch_113US\files\vaccination_data.csv"
# import csv
# def total_vacci():
#     with open(vaccination_path) as f:
#         rows = csv.reader(f)
#         temp = next(rows)
#         for item in rows:
#             yield {temp[0]: item[0], temp[5]: item[5]}
#
# res = total_vacci()
# for i in res:
#     print(i)
import sys

vaccination_path = r"C:\Users\HP\PycharmProjects\project_new\batch_113US\files\vaccination_data.csv"
# import csv
# def total_vacci():
#     with open(vaccination_path) as f:
#         rows = csv.DictReader(f)
#         for item in rows:
#             yield {'COUNTRY': item['COUNTRY'], "TOTAL_VACCINATIONS": item["TOTAL_VACCINATIONS"]}
#
# res = total_vacci()
# for i in res:
#     print(i)

# f_path = r"C:\Users\HP\PycharmProjects\project_new\batch_113US\files\sample.txt"
# res = (line for line in open(f_path))
# for i in res:
#     print(i)

path = r"C:\Users\HP\PycharmProjects\project_new\batch_113US\files\sample.log"
# def func(s):
#     with open(path) as file:
#         count = 0
#         for line in file:
#             if line.strip():
#                 temp = line.split()
#                 if temp[2] == s:
#                     count += 1
#         yield count
#
# res = func("TRACE")
# for i in res:
#     print(i)
# res = func("INFO")
# print(next(res))
# res = func('WARNING')
# print(list(res))

# count = 0
# res = (1 for line in open(path) if line.strip() if line.split()[2] == 'TRACE')
# for i in res:
#     count += i
# print(count)
#
# print(dir(res))
# print(dir(list))

# class Sample:
#     a = 10
#     b = 20
#
#
# obj1 = Sample()
# obj2 = Sample()
#
# print(obj1.a, obj2.a)
# obj1.a = 100
# print(obj1.a, obj2.a)
# print(Sample.a, Sample.b)
# Sample.a = 'hello'
# print(obj1.a, obj2.a)
# print(Sample.a, Sample.b)
# print(obj1.__dict__)
# print(obj2.__dict__)
# print(Sample.__dict__)

# class Calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         print(self.a + self.b)
#
#     def sub(self):
#         print(self.a - self.b)
#
#     def div(self):
#         print(self.a / self.b)
#
#     def mul(self):
#         print(self.a * self.b)
#
# calci1 = Calculator(1, 2, 3, 4)
# calci1.add()
# calci1.mul()
# calci1.div()
# calci1.sub()
# print(calci1.__dict__)

# class Employee:
#     company = 'microsoft'
#
#     def __init__(self, ename, eid):
#         self.ename = ename
#         self.eid = eid
#
#     def display(self):
#         print(self.ename, self.eid, self.company)
#
#     def email(self):
#         return f"{self.ename}_{self.eid}@{self.company}.com"
#
# person1 = Employee('Akash', 'ms123')
# person1.display()
# print(person1.email())
# print(person1.__dict__)
# person1.company = 'google'
# person1.display()
# print(person1.email())
# print(Employee.__dict__)
# print(person1.__dict__)

# class Sample:
#     a = 10
#     b = 20
#
#     def __init__(self, m, n):
#         self.c = m
#         self.a = n
#
#     @classmethod
#     def display(self, value):
#         print(self)
#         self.b = value
#         print(self.a, self.b)
#
#
# obj1 = Sample(50, 100)
# obj2 = Sample(1, 2)
# print(Sample.__dict__)
# obj1.display(200)
# print(Sample.__dict__)
# print(obj1.b)
# print(obj1.__dict__)
# print(obj2.__dict__)
# print(Sample.b)

# class ChiefMinister:
#     current_cm = 'Bommai'
#
#     def dispaly(self):
#         print(self.current_cm)
#
#     @classmethod
#     def replacement(cls, votes):
#         if votes > 50:
#             cls.current_cm = 'kejriwal'
#
# bjp = ChiefMinister()
# com_ppl = ChiefMinister()
# opposition = ChiefMinister()
#
# bjp.dispaly()
# com_ppl.dispaly()
# opposition.dispaly()
# bjp.replacement(51)
# bjp.dispaly()
# com_ppl.dispaly()
# opposition.dispaly()

# class Employee:
#     company = 'microsoft'
#
#     @staticmethod
#     def greet():
#         print('Hello How are you')
#
#     def __init__(self, ename, eid):
#         self.ename = ename
#         self.eid = eid
#         self.greet()
#
#     def display(self):
#         print(self.ename, self.eid, self.company)
#
#     def email(self):
#         return f"{self.ename}_{self.eid}@{self.company}.com"
#
# person1 = Employee('Akaash', 'ms123')
# person1.greet()

# class Records:
#     def __init__(self):
#         self.records = []
#
#     def __call__(self):
#         print('In call method')
#
# r = Records()
# print(callable(r))

''' create a class the prints msg = 'hello world' on 
calling the objects '''

# class Sample:
#
#     def __call__(self, *args, **kwargs):
#         print('hello world')
#
# s = Sample()
# s('hai', 'hello')

# class Greet:
#
#     def __init__(self, n):
#         self.name = n
#
#     def __call__(self):
#         print(self)
#         print(f'welcome {self.name}')
#
#
# ms123 = Greet('Akaash')
# ms123()
# ms321 = Greet('Rahul')
# ms321()

# class List_:
#
#     def __init__(self):
#         self.count = 0
#
#     def __call__(self, i):
#         self.a = []
#         self.temp = i
#         if isinstance(self.temp, (list, tuple, set)):
#             for item in self.temp:
#                 self.a.append(item ** 2)
#                 self.count += 1
#             return self.a
#         else:
#             return 'Non iterable'
#
# obj1 = List_()
# print(obj1([1, 2, 3, 4, 5]))
# print(obj1([10, 20, 30]))
# print(obj1.count)
# print(obj1.temp)

# def outer(func):
#     def wrapper(*args, **kwargs):
#         print('The output is : ')
#         func(*args, **kwargs)
#     return wrapper
#
# @outer
# def spam(name):
#     print(name)
#
# spam('Microsoft')

# class Decor:
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print('The output is : ')
#             func(*args, **kwargs)
#         return wrapper
#
#
# obj = Decor()
# @obj  # spam = obj(spam)
# def spam(name):
#     print(name)
#
# spam('Microsoft')

# class Decor:
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print('The output is : ')
#         self.func(*args, **kwargs)
#
# @Decor # spam = decor(spam)
# def spam(name):
#     print(name)
#
# spam('Ironman')
import time

# class Delay:
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         self.func(*args, **kwargs)
#         time.sleep(3)
#         self.func(*args, **kwargs)
#
# @Delay
# def display(msg):
#     print(msg)
#
# display('hello everyone')
#
# class Delay:
#
#     def __init__(self, n):
#         self.n = n
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             func(*args, **kwargs)
#             time.sleep(self.n)
#             func(*args, **kwargs)
#         return wrapper
#
# @Delay(1) # display = obj(display)
# def display(msg):
#     print(msg)
#
# display('hello everyone')

# class n_times:
#
#     def __init__(self, n):
#         self.n = n
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             for i in range(self.n):
#                 func(*args, **kwargs)
#         return wrapper
#
# @n_times(5)
# def display(name):
#     print(f'welcome {name}')
#
# display('Arjun')

# class Greet:
#     def __init__(self, msg='Good Morning'):
#         self.msg = msg
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print(self.msg)
#             func(*args, **kwargs)
#         return wrapper
#
# @Greet('welcome')
# def display():
#     print('Congratulations')
# display()
#
# @Greet()
# def spam():
#     print('Why so serious')
# spam()

''' calculate total number of functions decorated by a specified class decorator '''

# iterators :

# l = [1, 2, 3]
# temp = iter(l)
# print(temp)
# v = l.__iter__()
# print(v)
# print(l.__len__())
# a = 10
# m = a.__str__()
# print(type(m))

# l = [1, 2, 3, 4]
# for item in l:
#     print(item)

# obj = iter(l)
# while True:
#     try:
#         item = next(obj)
#     except StopIteration:
#         break
#     else:
#         print(item)

# obj = l.__iter__()
# while True:
#     try:
#         item = obj.__next__()
#     except StopIteration:
#         break
#     else:
#         print(item)

''' create a custom iterator class to print the numbers from 1 to 5 '''
# class Sample:
#
#     def __init__(self):
#         self.a = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.a > 5:
#             raise StopIteration
#         else:
#             x = self.a
#             self.a += 1
#             return x
#
# s = Sample()
# m = Sample()
# n = Sample()
# for item in s:
#     print(item)
#
# for i in m:
#     print(i)

# def sample():
#     a = 1
#     while a <= 5:
#         yield a
#         a += 1
#
# x = sample()
# print(x)
# for item in x:
#     print(item)

''' 10 to 1'''
# def sample():
#     a = 10
#     while a > 0:
#         yield a
#         a -= 1
#
# x = sample()
# print(x)
# for item in x:
#     print(item)

# class Sample:
#
#     def __init__(self):
#         self.a = 10
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.a == 0:
#             raise StopIteration
#         else:
#             x = self.a
#             self.a -= 1
#             return x
#
# s = Sample()
# m = Sample()
# n = Sample()
# for item in s:
#     print(item)
#
# for i in m:
#     print(i)

''' user defined range class '''
# class Sample:
#
#     def __init__(self, start, end, stepvalue):
#         self.s = start
#         self.e = end
#         self.sv = stepvalue
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.sv > 0:
#             if self.s >= self.e:
#                 raise StopIteration
#             else:
#                 num = self.s
#                 self.s += self.sv
#                 return num
#         elif self.sv < 0:
#             if self.s <= self.e:
#                 raise StopIteration
#             else:
#                 num = self.s
#                 self.s += self.sv
#                 return num
#         else:
#             raise ValueError('Step Value can not be zero ')
#
# s = Sample(10, -2, -1)
# for i in s:
#     print(i)

'''create custom iterator class to print squares of range of numbers'''
# class Square:
#
#     def __init__(self, start, end):
#         self.s = start
#         self.e = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.s >= self.e:
#             raise StopIteration
#         else:
#             x = self.s
#             self.s += 1
#             return x ** 2
#
# s = Square(2, 6)
# for i in s:
#     print(i)
#
# class SquareN:
#
#     def __init__(self,end):
#         self.s = 1
#         self.e = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.s >= self.e:
#             raise StopIteration
#         else:
#             x = self.s
#             self.s += 1
#             return x ** 2
#
# s = SquareN(6)
# for i in s:
#     print(i)

# class Reverse:
#
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.index = len(iterable)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index <= 0:
#             raise StopIteration
#         else:
#             self.index -= 1
#             return self.iterable[self.index]
#
# r = Reverse(['hello', 'hai', 10, 15, 'python'])
# for i in r:
#     print(i)

''' create a custom iterator to give prime number in the given range '''
# class Prime:
#
#     def __init__(self, s, e):
#         self.s = s
#         self.e = e
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.s == self.e:
#             raise StopIteration
#         else:
#             for i in range(2, self.s):
#                 if self.s % i == 0:
#                     break
#             else:
#                 x = self.s
#                 self.s += 1
#                 return x
#             self.s += 1
#
#
# s = Prime(1, 30)
# for i in s:
#     if i != None:
#         print(i)

























