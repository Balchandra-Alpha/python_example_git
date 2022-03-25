''' count the no of times the function being called/executed'''

# count = 0
# def display():
#     global count
#     count += 1
#     c_inside = 0
#     def inside():
#         nonlocal c_inside
#         c_inside += 1
#     inside()
#     inside()
#     inside()
#     return c_inside
# print(display())
# print(display())
# print(count)
#
#
# b = 20
# a = 10
# def spam():
#     global c
#     c = 15
#     c += 1
#     print(a, b, c, "inside function")
#
# # print(a, "outside function, before")
# spam()
# print(a, c, "outside function, after")

# a = 10
# def func():
#     print(a)
#     c = 20
#     def nested():
#         nonlocal c
#         print(c)
#         c += 1
#     nested()
#     print(c)
#
#
# func()

# def spam(func):
#     def inner(*args, **kwargs):
#         print('(in spam) The output is :')
#         func(*args, **kwargs)
#     return inner

# @spam # rev_str = spam(rev_str) [inner]
# def rev_str(s):
#     print(s[::-1])
#
# @spam # add= spam(add) [inner]
# def add(a, b):
#     print(a + b)
#
# @spam
# def display(msg):
#     print(msg)
#
# add = spam(add)
# rev_str = spam(rev_str)
# add(4, 5)
# #
# rev_str('hello')
# print(rev_str)
# print(add)
# print(display)
# display('Good morning')

''' create a decorator to give a msg welcome '''
# def note(func):
#     def wrapper(*args, **kwargs):
#         print(func(*args, **kwargs))
#         print('you are welcome')
#         return 10
#     return wrapper
#
# @note #greet =  note(greet)
# def greet(name):
#     return f"hi {name}"
#
# print(greet('Akaaash'))
#
# @note #greet2 =  note(greet2)
# def greet2(name, age):
#     print(name, age)
#     return 20
#
# print(greet2(age=19, name='aaa'))

''' create a decorator which will execute the main function 3 times '''

# def para(n):
#     def outer(func):
#         def inner(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#             return 'Execution Done(inside inner)'
#         return inner
#     return outer
#
# @para(3)
# def display(msg):
#     print(msg)
#
# print(display('Welcome'))
#
# @para(2)
# def some(msg):
#     print(msg)
#
# print(some('python'))

''' write a decorator to reverse a string '''

''' write a decorator to count the number of arguments given to the main function'''

''' delay the execution for n seconds using decorator (use time.sleep() from time module)'''
# import time
# def delay(n):
#     def outer(func):
#         def inner(*args, **kwargs):
#             start = time.time()
#             print('Before')
#             print(func.__name__)       #to print the main function name.
#             time.sleep(n)       # delay the execution
#             func(*args, **kwargs)
#             print('after')
#             end = time.time()
#             return end - start      #time taken to execute
#         return inner
#     return outer
#
# @delay(2)
# def my_func(name):
#     print(name[::-1])
#
# @delay(3) #==> @outer #==> new_func = outer(new_func) #==> new_func ==> inner
# def new_func():
#     print('hello everyone')
#
# print('execution time is : ', my_func('Hello'))
#
# print(new_func())
#
# @delay(1)
# def add(a, b):
#     print(a + b)
#
# print(add(10, 20))





