# class Spam:
#     a = 10
#     b = 'hello'
#
# obj1 = Spam()
# m = Spam()
# n = Spam()
#
# print(obj1)
#
# print(obj1.a, obj1.b)
# print(m.a, m.b)
# print(n.a, n.b)
# obj1.a = 100
# print(obj1.a, obj1.b)
# Spam.a = 15.5
# print(m.a, m.b)
# print(n.a, n.b)
# print(Spam.__dict__)
# print(m.__dict__)
# print(obj1.__dict__)
# print(obj1.a)
# print(dir(Spam))
# print(dir(obj1))
# print(dir(m))

# class Calculator:
#     value = 10
#
#     def sum(self, a, b):
#         print(self)
#         print(self.value)
#         print(a + b)
#
#     def sub(self, a, b):
#         print(self)
#         print(a - b)
#
#     def div(self, a, b):
#         print(a / b)
#
#     def mul(self, a, b):
#         print(a * b)
#
# calci1 = Calculator()
# calci1.value = 100
# calci2 = Calculator()
# calci1.sum(2, 3)
# # calci1.sub(22.5, 15.8)
# calci2.sum(10, 20)

# class Calculator:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def sum(self):
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
# calci1 = Calculator(2, 3)
# print(calci1.__dict__)
# calci2 = Calculator(10, 20)
# calci1.sum()
# calci1.div()
# calci1.mul()
# calci1.sub()
# print(calci2.__dict__)
# calci2.sum()
# calci2.div()
# calci2.mul()
# calci2.sub()
# print(dir(Calculator))

# class Spam:
#
#     def display(self):
#         pass
#         # print(Spam.__dict__)
#         # print(self.__dict__, 'Obj attributes')
#
#     @classmethod
#     def random(cls, name):
#         print(cls)
#         cls.n = name
#
# obj1 = Spam()
# obj2 = Spam()
# obj1.display()
# obj1.random('Thor')
# obj1.display()
# obj2.display()

# class President:
#     current_president = 'Biden'
#
#     def display(self):
#         print(self.current_president)
#
#     @classmethod # This method takes the class adress implicitely and do changes wrt class not wrt object, its doone by @classmethod
#     def replacement(cls, votes):
#         print(cls)
#         if votes > 50:
#             cls.current_president = 'Trump'
#
# demo_party = President()
# rep_party = President()
# people = President()
# people.replacement(55)
# people.display()
# demo_party.display()
# rep_party.display()

# class Message:
#
#     @staticmethod
#     def greet():
#         print('Hello everyone')
#
#     def __init__(self, name):
#         self.name = name
#
#
# person1 = Message('Thor')
# person2 = Message('Ironman')
# print(person1.__dict__, person2.__dict__)
# person1.greet()
# person2.greet()

# class Sample:
#
#     def display(self):
#         print(self)
#         print('Hello Everyone')
#
#     def __call__(self):
#         print('In call method')
#
#
# a = Sample()
# b = Sample()
# c = Sample()
# b()
# c()
# a()
# print(Sample.__dict__)
# print(dir(a))
_ = ''
''' create class that prints "hello everyone" on calling is object '''

# class Sample:
#
#     def __call__(self):
#         print('Hello Everyone')
#
# a = Sample()
# b = Sample()
# a()
# b()

''' create class that greets the person when its object is being called '''
# class Spam:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self, msg):
#         print(f'Hello {self.name}, {msg}')
#
# p1 = Spam('Arjun')
# p2 = Spam('Rahul')
# p1('Good Morning')
# p2('Good Evening')

#########################################################

''' creating decorator using class '''
# class Sample:
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print('The output is : ')
#         self.func(*args, **kwargs)
#
# @Sample   #add = Sample(add)
# def add(a, b):
#     print(a + b)
#
# add(4, 5)
#
# @Sample
# def sub(s):
#     print(s - 10)
#
# sub(25)

''' creating decorator using objects of a class '''

# class Sample:
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print('The output is : ')
#             func(*args, **kwargs)
#         return wrapper
#
# obj = Sample()
# @obj  # add = obj(add)
# def add(a, b):
#     print(a + b)
#
# add(10, 20)
#
# @Sample()
# def sub(s):
#     print(s -100)
#
# sub(55)

##########################################

''' create a class decorator as parameterized decorator '''

# class Sample:
#
#     def __init__(self, n, m, l):
#         self.n = n
#         self.m = m
#         self.l = l
#
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print('The output is : ')
#             print(self.m, self.l)
#             for _ in range(self.n):
#                 func(*args, **kwargs)
#         return wrapper
#
# obj = Sample(3, 10, 'hello')
# @obj  # add = obj(add)
# def add(a, b):
#     print(a + b)
#
# add(10, 20)
#
# @Sample(2, 11, 'ahai')
# def sub(s):
#     print(s -100)
#
# sub(55)


''' create a decorator which delays the execution of function '''
# import time
# class Delay:
#     def __init__(self, d):
#         self.d = d
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print('before func execution')
#             time.sleep(self.d)
#             func(*args, **kwargs)
#             print('After func execution')
#         return wrapper
#
# @Delay(2)
# def msg():
#     print('Good Morning')
#
# @Delay(3)
# def rev(s):
#     print(s[::-1])
#
# msg()
# print()
# rev('hello')

''' count the number execution of decorative functions '''
# count = 0
# class Spam:
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             global count
#             count += 1
#             func(*args, **kwargs)
#         return wrapper
#
#
# @Spam()
# def add(a, b):
#     print(a + b)
#
# @Spam()
# def reverse(s):
#     print(s[::-1])
#
# add(10, 15)
# add(12, 11)
# reverse('Python')
# print(count)
# add(10, 15)
# add(12, 11)
# reverse('Python')
# print(count)

