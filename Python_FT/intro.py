# s = 'hello'
# a = 10
# b = 20
# print(s, a, b, sep='@', end='%')
# print(s, 'hai', sep='&') # o/p ==> hello@10@20%hello&hai
#
# print('first statement', end='==')
# print('second statement') # o/p ==> first statement==second statement
#
# print('first value', 'second value', 'third value', sep='--')
# # o/p ==> first value--second value--third value

# name = input('Enter your name ', )
# print(type(name))
# print('hello', name)

# greet = 'Hi hello {}, Welcome to my store'
# name = input('Enter your name ')
# print(greet.format(name))
#
# msg = "hi my name is {} and I'm {} years old"
# print(msg.format('Arjun', 25))
# # o/p ==> hi my name is Arjun and I'm 25 years old
#
# msg = "hi my name is {1} and I'm {0} years old"
# details = input('Enter your name')
# print(msg.format(25, details))
# # o/p ==> hi my name is salman and I'm 25 years old
#
# msg = "hi my name is {name} and I'm {age} years old"
# details = input('Enter your name')
# print(msg.format(age=25, name=details))
#o/p ==> hi my name is Arjun and I'm 25 years old

# from copy import deepcopy
# l = [1, 2, 3, [100, 200], 4]
# m = deepcopy(l)
# print(id(l), id(m))
# print(id(l[3]), id(m[3]))
# l[3].append(10)
# print(l, m)
# m[3].append(20)
# print(l, m)

# l = [10, 40, 20, 50, 30, 70]
# print(l)
# print(l.sort())
# print(l)

# l = ['apple', 'google', 'IBM', 'wipro', '10']
# l.sort()
# print(l) #['10', 'IBM', 'apple', 'google', 'wipro']
# l.sort(key=len)
# print(l) #['10', 'IBM', 'apple', 'wipro', 'google']

# list_ = [10, 20, 'hello', 'python', 3, 2, 1]
# m = list_[::-1]
# print(m, list_, sep="\n")
# list_.reverse()
# print(list_)

# s = {1, 2, 3, 'hello', (10, 20), 20}
# print(s)
#
# import lambdaFT
# print(lambdaFT.a)
# print(lambdaFT.company)
#
# from my_reference.new import a as a1, b
# print(a1)
# print(b)

# a = 100
# def outer(n):
#     n += 20
#     print(n, 'inside outer')
#
# print(a)
# outer(a)
# print(a)
# count = 0
# def add(a, b):
#     global count
#     count += 1
#     a = 10
#
#     def inner():
#         global count
#         count += 1
#         nonlocal a
#         a += 1
#         print(count, 'inside inner')
#         print(a, 'inside inner')
#
#
#     inner()
#     print(a, 'inside add')
#     return a + b


# print(add(1, 2))
# print(add(10, 2))
# print(add(1, 2))
# print(add(1, 20))
# print(add(1, 21))
# print(count)
# print(v)

# print(inner())

# a = 10
# def spam():
#     b = 10
#     def inner():
#         nonlocal b
#         print(b)
#         b += 2
#     inner()
#     print(b)
# spam()



