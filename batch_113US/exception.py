# a = 10
# b = 0
# c = a / b
# print(c)
# print('hello')

# try and default except block:

# try:
#     print('in try block')
#     a = 10
#     b = 0
#     a.index(b)
#     c = a / b
#     print(c)
#     print('hello in try block')
# except:
#     print('hello in except block')

#specific except block #multiple execpt block
# try:
#     print('in try block')
#     a = 10
#     b = 0
#     c = a / b
#     a.index(b)
#     print(c)
#     print('hello in try block')
# except ZeroDivisionError as msg:
#     print('hello in except block')
#     print(msg)
# except AttributeError as msg2:
#     print('In attribute except block')
#     print(msg2)
# except NameError as msg3:
#     print('In Name except block')
#     print(msg3)

#generic exception block
# try:
#     print('in try block')
#     a = 10
#     b = 0
#     # set().pop()
#     # a.index(b)
#     # c = a / b
#     # print(c)
#     print('hello in try block')
# except BaseException as msg:
#     print('hello in except block')
#     print(msg)
# else:
#     print('in else block')

# finally block
# try:
#     print('in try block')
#     a = 10
#     b = 0
#     set().pop()
#     # a.index(b)
#     # c = a / b
#     # print(c)
#     print('hello in try block')
# except ZeroDivisionError as msg:
#     print('hello in except block')
#     print(msg)
# else:
#     print('in else block')
# finally:
#     print('hello in finally block')

#raise error
# num = int(input('Enter a positive number : '))
# try:
#     if num < 0:
#         raise ValueError('Expected positive number , but negative given')
#     else:
#         print(num)
# except ValueError as msg:
#     print(msg)

company = ['apple', 'google', 'microsoft', 'apple', 'infosys', 'apple', 'google']
d = {}
# for item in company:
#     if item not in d:
#         d[item] = 1
#     else:
#         d[item] += 1
# print(d)

# for item in company:
#     try:
#         d[item] += 1
#         print(d, 'in try block')
#     except KeyError:
#         d[item] = 1
#         print(d, 'in except block')
#     else:
#         print(item)
# print(d)

''' wap to handle zero division error in the list of data'''
# l = [(1, 0), (2, 4), (3, 0), (4, 3), (7, 0), (5, 0)]
# res = []
# for item in l:
#     try:
#         temp = item[0] / item[1]
#     except ZeroDivisionError as msg:
#         print(item, msg)
#     else:
#         res.append(item)
# print(res)

#custom exception
# class MyException(Exception):
#     pass
#
# a = 10
# if a > 0:
#     raise MyException

# class InvaildCredentials(BaseException):
#     pass
#
# def validate_username(username):
#     if username != 'John':
#         raise InvaildCredentials('invalid username')
#
# def validate_password(password):
#     if password != 'John1234':
#         raise InvaildCredentials('invalid password')
#
# try:
#     validate_username('John')
#     validate_password('john1234')
# except BaseException as msg:
#     print('Invalid credetials :', msg)
# else:
#     print('No exception')


# iterator :
# def spam(n):
#     for i in range(n):
#         yield i
#
# res = spam(5)
# # print(dir(res))
# # print(dir(list))
# for i in res:
#     print(i)

''' working of for loop '''
l = [1, 2, 3, 4]
# m = []
# for i in l:
#     print(i)
print()
# protocol of for loop.
# iterator_obj = l.__iter__() # iter(l)
# while True:
#     try:
#         i = next(iterator_obj)
#     except StopIteration:
#         break
#     else:
#         print(i)

# class Sample:
#
#     def __init__(self):
#         self.start = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start < 5:
#             self.start += 1
#             return self.start
#         else:
#             raise StopIteration
#
#
# s = Sample()
# m = Sample()
# for i in s:
#     print(i)
# print()
# for i in m:
#     print(i)

# class Sample:
#
#     def __init__(self, num):
#         self.start = 0
#         self.end = num
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start == self.end:
#             raise StopIteration
#         else:
#             x = self.start
#             self.start += 1
#             return x
#
# s = Sample(5)
# m = Sample(7)
# for i in s:
#     print(i)
# for i in m:
#     print(i)

# import time
#
# class Sample:
#
#     def __init__(self, num):
#         self.start = num
#         self.end = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start == self.end:
#             raise StopIteration
#         else:
#             x = self.start
#             time.sleep(0.5)
#             self.start -= 1
#             return x
#
# s = Sample(5)
# m = Sample(7)
# for i in s:
#     print(i)
# for i in m:
#     print(i)

# custom range class.

# class MyRange:
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
#                 x = self.s
#                 self.s += self.sv
#                 return x
#         elif self.sv < 0:
#             if self.s <= self.e:
#                 raise StopIteration
#             else:
#                 x = self.s
#                 self.s += self.sv
#                 return x
#         else:
#             raise ValueError('Step Value can not be zero')
#
# s = MyRange(-10, -1, -1)
# for i in s:
#     print(i)

''' creating a reverse iterator obj for sequences  '''
# class Reverse:
#
#     def __init__(self, sequence):
#         self.s = sequence
#         self.end = len(sequence)
#         self.start = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start == self.end:
#             raise StopIteration
#         else:
#             self.end -= 1
#             return self.s[self.end]
#
# new = Reverse([1, 2, 3, 4, 5])
# for i in new:
#     print(i)
# a = Reverse('Hello')
# for i in a:
#     print(i)

# class Primes:
#
#     def __init__(self, start, end):
#         self.s = start
#         self.e = end
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
#                     y = self.s
#                     self.s += 1
#                     return                         #f"{y} is not prime"
#             else:
#                 x = self.s
#                 self.s += 1
#                 return x
#
#
# num = Primes(12, 100)
# for i in num:
#     if i:
#         print(i)


