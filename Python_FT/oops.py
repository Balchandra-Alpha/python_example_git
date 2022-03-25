'''
is a relationship - inheritance
has a relationship - composition
'''

# class Parent:
#     name = 'Ironman'
#     a = 'hai'
#
#     def display(self):
#         print('Nano Tech')
#
# class Child(Parent):
#     a = 10
#     b = 20
#
# print(Child.name)
# c = Child()
# c.display()
# print(Child.__dict__)
# print(Parent.__dict__)
#
# p = Parent()
# print(p.a)
# print(c.a)

# class Company:
#     c_name = 'microsoft'
#
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#
#
# class Employee(Company):
#     eid = '3478'
#
#     def display(self):
#         print(self.fname + self.lname)
#
# e = Employee('Sundar', 'Sharma')
# c = Company('Shyam', 'Sharma')
# print(e.eid, e.fname, e.lname)
# print(c.fname, c.lname)
# e.display()
#
# class Benefits(Employee):
#     bonus = 3000

# class Parent:
#     a = 10
#     b = 20
#
# class child2(Parent):
#     c = 130
#     b = 125
#
# class child3(Parent):
#     a = 80
#     d = 64
#
# c3 = child3()
# c2 = child2()
# print(c2.a, c2.b, c2.c)
# print(c3.a, c3.b, c3.d)

# class Parent:
#     a = 13
#
#     def spam(self):
#         print('In parent class')
#
#     def display(self):
#         print('In parent display')
#
#
# class Child(Parent):
#     a = 100
#
#     def spam(self):
#         print('In child class')
#         # Parent().spam()
#         super().spam()
#
# b = Child()
# print(b.a)
# b.spam()
# b.display()


# class Sample:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         print('The values are : ', self.a, self.b)
#         print(self.a + self.b)
#
#     def display(self):
#         print("The values in parent class are ", self.a, self.b)
#
#
# class Sample2(Sample):
#     def __init__(self, x, y, s1, s2):
#         self.x = x
#         self.y = y
#         super().__init__(s1, s2)
#
#
#     def display(self):
#         print("The values in child class are ", self.x, self.y)
#         super().display()
#
# s = Sample2(10, 20, 11, 15)
# s.add()
# s.display()
#
# class Company:
#
#     def __init__(self, c_name):
#         self.c_name = c_name
#
# class Employee(Company):
#
#     def __init__(self, name, company):
#         self.e_name = name
#         super().__init__(company)
#
# a = Employee('John', 'microsoft')
# print(a.__dict__)


# Polymorphism
# '''Poly - many , morphs - forms '''
# ''' +, * '''
#
# ''' len --> str - No of char
#             list, tuple - No of elements
#             dict, set - No of keys '''
#
# class Sample:
#     def display(self):
#         print('In Sample ')
#
# class Demo:
#     def display(self):
#         print('In Demo ')
#
# s = Sample()
# d = Demo()
# s.display()
# d.display()

# class Sample:
#     def display(self):
#         print('In Sample ')
#
# class Demo(Sample):
#     def display(self):
#         print('In Demo ')
#         super().display()
#
# s = Sample()
# d = Demo()
# # s.display()
# d.display()

# public
# class BankAccount:
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
# b = BankAccount('John', 50000)
# print(b.name)
# print(b.balance)

#proteccted
# class BankAccount:
#
#     def __init__(self, name, balance):
#         self.name = name
#         self._balance = balance
#
# b = BankAccount('John', 50000)
# print(b.name)
# print(b.balance) #Error
# print(b._balance) # we should not do this

#private
# class BankAccount:
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#
# b = BankAccount('John', 50000)
# print(b.name)
# print(b.balance) #Error
# print(b._balance) #Error
# print(b.__balance) #Error
# print(b.__dict__) #{'name': 'John', '_BankAccount__balance': 50000}

# class BankAccount:
#
#     def __init__(self, name , balance):
#         self.name = name
#         self.__balance = balance
#
#     def get_balance(self):  # getter method
#         return self.__balance
#
#     def set_balance(self, value): # setter method
#         self.__balance += value
#
#     def delete_balance(self): #deleter method
#         del self.__balance
#
# b = BankAccount('John', 20000)
# print(b.get_balance())
# b.set_balance(10000)
# print(b.get_balance())
# b.delete_balance()
# print(b.get_balance())
###############################
# class BankAccount:
#
#     def __init__(self, name , balance):
#         self.name = name
#         self.__balance = balance
#
#     def get_balance(self):  # getter method
#         return self.__balance
#
#     def set_balance(self, value): # setter method
#         self.__balance += value
#
#     def delete_balance(self): #deleter method
#         del self.__balance
#
#     balance = property(get_balance, set_balance, delete_balance)
#
# b = BankAccount('John', 20000)
# print(b.balance)
# b.balance = 10000
# print(b.balance)
# del b.balance
# print(b.balance)

# class BankAccount:
#
#     def __init__(self, name , balance):
#         self.name = name
#         self.__balance = balance
#
#     @property
#     def balance(self):
#         pass
#
#     @balance.getter # @property
#     def balance(self):  # getter method
#         return self.__balance
#
#     @balance.setter
#     def balance(self, value): # setter method
#         self.__balance += value
#
#     @balance.deleter
#     def balance(self): #deleter method
#         del self.__balance
#
# # b = BankAccount('John', 20000)
# # print(b.balance)
# b = BankAccount('John', 20000)
# print(b.balance)
# b.balance = 10000
# print(b.balance)
# del b.balance
# print(b.balance)

''' JSON - Java Script Object Notation '''

import json

# d = {'name': 'John', 'company': 'apple', 'salary': 250000}
#
# # x = json.dumps(d)
# # print(x, type(x))
# #
# # y = json.loads(x)
# # print(y, type(y))
#
# with open('Sample.json', 'w') as file:
#     obj = json.dump(d, file)
#     # obj = json.dump('\nhello', file)
#
# with open('Sample.json') as file:
#     x = json.load(file)
# print(x, type(x))

##################

# import pickle
#
# d = {'name': 'John', 'company': 'apple', 'salary': 250000}

# x = pickle.dumps(d)
# print(x, type(x))
#
# y = pickle.loads(x)
# print(y, type(y))

# with open('Sample.pkl', 'wb') as file:
#     pickle.dump(d, file)
#     pickle.dump('\nhello', file)
#
# with open('Sample.pkl', 'rb') as file:
#     x = pickle.load(file)
#     y = pickle.load(file)
# print(x, type(x))
# print(y, type(y))

from abc import ABC, abstractmethod

# class ATM(ABC):
#
#     @abstractmethod
#     def withdraw(self, amount):
#         pass
#
#     @abstractmethod
#     def deposit(self, amount):
#         pass
#
#     @abstractmethod
#     def balance(self):
#         pass
#
# class SBI(ATM):
#
#     def withdraw(self, amount):
#         print('In withdraw', amount)
#
#     def deposit(self, amount):
#         print('In deposit', amount)
#
#     def balance(self):
#         print('In balance')
#
# s = SBI()
# s.deposit(20000)
# s.withdraw(40000)
# s.balance()
# print(s.amount)

# class Polygon(ABC):
#     def __init__(self, side):
#         self.side = side
#
#     @abstractmethod
#     def sides(self):
#         pass
#
#
# class Rectangle(Polygon):
#
#     def sides(self):
#         print(f"Polygon has {self.side} sides")
#
# p = Rectangle(4)
# p.sides()


''' create a class SimCard, 1. number, 2. network provider. 
2 can be changed by user, 1 can not be changed. '''

# class SimCard:
#
#     def __init__(self, network, number):
#         self.__network = network
#         self.__number = number
#
#     @property
#     def network(self):
#         return F'The network is : {self.__network}'
#
#     @network.setter
#     def network(self, new_network):
#         self.__network = new_network
#
#     @property
#     def number(self):
#         return F'The number is : {self.__number}'
#
# s = SimCard('Airtel', '9786342153')
# print(s.network)
# print(s.number)
# s.network = 'Jio'
# print(s.network)

