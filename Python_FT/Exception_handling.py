# try:
#     print('hai')
#     a = 10
#     b = 0
#     c = 100
#     print(s.index('m'))
#     print(b.append(10))
#     print('python')
#     print(a / b)
#     print('hello')
# except ZeroDivisionError as msg:
#     print('Denominator is zero')
#     print(msg)
# except AttributeError as msg2:
#     print(msg2)
# except NameError as m:
#     print(m)
# except:
#     print('Good morning')

# try:
#     print('hai')
#     a = 10
#     b = 0
#     # print(a + 'hai')
#     print(a/ b)
#     print(a + 'hai')
# except ZeroDivisionError as msg:
#     print('hai hello')
#     print(msg)
# d = {}
# try:
#     a = d['value']
#     print(1 / 0)
# except KeyError:
#     print("inside KeyError block ")
#     d['value'] = 10
# except ZeroDivisionError:
#     print("inside ZeroDivisionError block ")
# print(d)
# try:
#     a = d['value']
#     print(1 / 0)
# except KeyError:
#     print("inside KeyError block ")
#     d['value'] = 10
# except ZeroDivisionError:
#     print("inside ZeroDivisionError block ")
# print(d)

# try:
#     a =10
#     b = 0
#     print(a / b)
#     set().pop()
# except BaseException as msg:
#     print(msg)

# d = {}
# try:
#     d['value'] = 1
#     set().pop()
#     print(1/2)
# except KeyError as msg:
#     print('In execption block')
#     print(msg)
# finally:
#     print('In finally')
#
# d = {}
# try:
#     d['value'] = 1
#     print(1/2)
# except BaseException as msg:
#     print('In execption block')
#     print(msg)
# else:
#     print('in else block')
#     print(d)

# class InvalidPassword(Exception):
#     pass
#
# class InvalidUsername(Exception):
#     pass
# def validate_username(name):
#     if name != 'Ram':
#         raise InvalidUsername("Username is not matching")
#
# def validate_password(value):
#     if value != 'Ram@123':
#         raise InvalidPassword("Password is not matching")
#
# try:
#     validate_username('Ram')
#     validate_password('Shyam@123')
# except InvalidPassword as msg:
#     print('Invalid Credentials')
#     print(msg)

a = 10
''' wap to handle Keyerror while creating a dictionary of word and its count '''
# company = ['apple', 'google', 'microsoft', 'apple', 'tesla', 'google', 'apple']
# d = {}
# for item in company:
#     try:
#         d[item] += 1
#     except KeyError:
#         d[item] = 1
# print(d)

''' wap to handle zerodivison error in the list of data, print the result of the division
if there is no exception and also the elements '''
# nums = [(1, 0), (3, 4), (4, 5), (0, 1), (2, 0), (-10, 0)]
# for first, second in nums:
#     try:
#         temp = first / second
#     except ZeroDivisionError:
#         print(f"we can not divide {first} by {second}")
#     else:
#         print({temp:(first, second)})
#
# for first, second in nums:
#     try:
#         if second == 0:
#             raise ZeroDivisionError
#     except ZeroDivisionError:
#         print(f"we can not divide {first} by {second}")
#     else:
#         print({first/second:(first, second)})

from math import factorial
def fact(n):
    if not isinstance(n, int):
        raise TypeError('Number is not integer')
    elif n < 0:
        raise ValueError('Given negative integer, expected positive or zero')
    else:
        return factorial(n)


print(fact(-8.5))







