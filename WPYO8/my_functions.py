# l = [1, 2, 3, 4, 5, 6]
# count = 0
# for i in l:
#     count += 1
# print(count)

# s = 'hellooo'
# c_s = 0
# for i in s:
#     c_s += 1
# print(c_s)

# t = (10, 20, 30, 40)
# c_t = 0
# for i in t:
#     c_t += 1
# print(c_t)

# l = [1, 2, 3, 4, 5, 6]
# s = 'hellooo'
# t = (10, 20, 30, 40)
#
# print('before function definition')

# def my_len_func(iter_): # formal arguments/ parameters
#     count = 0
#     for _ in iter_:  # _ - Throw away variable(convention)
#         count += 1
#     return count
#
# new = my_len_func(t)# calling a function/ function call)
# print(len(t))
# print(new)
# print('after function definition ')
# my_len_func(s)
# my_len_func(l)
# # my_len_func()
# my_len_func()

# def add(a, b):  # formal arguments/ parameters
#     return a + b
# print(add(10, 20)) # actual argument / arguments
# value = add(12, 11)
# print(value)
#
# def display(name):
#     print('Inside function')
#     return 'hai', name, 'welcome', 10
#
# print(display('Ironman'))
# var = display('Shakthiman')
# print(var)
# print(var[1])

# def sample(s):
#     if len(s) % 2 == 0:
#         return 1 #True
#     else:
#         return 0 #False
#
#
# string = input('Enter anything : ')
# if sample(string):
#     print(string, 'string is even length')
# else:
#     print(string[::-1], 'string is odd length')

# def is_prime(n):
#     for item in range(2, n):
#         if n % item == 0:
#             return False
#     else:
#         return True
#
#
# print(is_prime(7))
# print(is_prime(11))
# print(is_prime(10))
# print(is_prime(37))
# print(is_prime(39))
''''''

''' wa function to search for a char in a given string and return the corresponding index '''
# s = input('Enter a string : ')
# c = input('Enter a char to search : ' )
#
# # def search(string, char):
# #     for item in string:
# #         if item == char:
# #             return string.index(char)
# #     else:
# #         return 'Char not found in given string'
#
# def search(string, char):
#     temp = string.find(char)
#     if temp == -1:
#         return 'Char not found in given string'
#     else:
#         return temp
#
# print(search(s, c))

''' wa function to check whether given two strings are anagram or not '''
''' 'cat', 'act' '''

# def is_anagram(str1, str2):
#     temp1 = list(str1) # [c, a, t]
#     temp2 = list(str2) # [a, c, t]
#     temp1.sort()    # [a, c, t]
#     temp2.sort()    # [a, c, t]
#     if temp1 == temp2:
#         return 'anagram'
#     else:
#         return 'not anagram'
#
#
# print(is_anagram('cat', 'act'))
# print(is_anagram('caat', 'acct'))
# print(is_anagram('night', 'thing'))


#positional arguments:
# def info(name, company, salary, phno):
#     print(f'{name} is working in {company}')
#     print(f'{salary} is offered for {name}' )
#     print(f"{name}'s contact number is {phno}")
#
#
# info('john', 'google', 45000, 1234)
# print()
# def info(name, company, salary, phno):
#     print(f'{name} is working in {company}')
#     print(f'{salary} is offered for {name}' )
#     print(f"{name}'s contact number is {phno}")
#
#
# info(45000, 1234, 'john', 'google')
# print()
#keyword arguments
# def info(name, company, salary, phno):
#     print(f'{name} is working in {company}')
#     print(f'{salary} is offered for {name}' )
#     print(f"{name}'s contact number is {phno}")
#
#
# info(salary=45000, phno=1234, name='john', company='google')
# print()
# def info(name, company, salary, phno):
#     print(f'{name} is working in {company}')
#     print(f'{salary} is offered for {name}' )
#     print(f"{name}'s contact number is {phno}")
#
#
# info('john', 'google',phno=1234, salary=45000)

# print()
# def info(name, company, /,a,  * , salary, phno):
#     print(f'{name} is working in {company}')
#     print(f'{salary} is offered for {name}' )
#     print(f"{name}'s contact number is {phno}")
#     print(a)
#
#
# info('john', 'google',10, salary=45000, phno=1234)

# def add(a, /, *,  b):
#     return a + b


# print(add(2, 3))
# print(add(b=3, a=2))
# print(add(2, b=3))

# DEFAULT ARGUMENT
def add(a, b=0, c=0):
    print(a, b, c)
    return a + b + c


# print(add(2, 3, 4)) #2 3 4 ==> 9
# print(add(a=2, c=3)) # 2 0 3 ==> 5
# print(add(5)) # 5 0 0 ==> 5

# def add(a, b, c=0, d=0):
#     return a + b + c + d
#
#
# print(add(1, 2, 3, 4))

# def add(*args):
#     print(args)
#     sum = 0
#     for i in args:
#         sum += i
#     return sum


# print(add(1, 2, 3, 4, 5, 6))
# print(add(10, 20, 30))


def add(**kwargs):
    print(kwargs)
    sum = 0
    for i in kwargs:
        sum += kwargs[i]
    return sum

#
# print(add(f=1, s=2, t=3, f4=4, f5=5))
# print(add(a=10, b=20, c=25))

def add(*args, **kwargs):
    print(args)
    print(kwargs)


# print(add(1, 2, 3, 4, 5, s=6)) # (1, 2, 3, 4, 5) {'s': 6}
# print(add(1, 2, 3, 4, f=5, s=6)) # (1, 2, 3, 4) {'f': 5, 's': 6}


# def add(a, b):
#     print(a)
#     print(b)
#     return a, b
#
# l = [10, 20]
# print(add(*l))
# ''' while unpacking list/tuple , the number of elements in list/tuple
# should be same as formal arguments.'''
# d = {'a':11, 'b': 22}
# print(add(**d))
# ''' while unpacking dictionary, along with number, even the keys in dictionary
# should be same as formal arguments in function definiton.'''

# def add(a, b):
#     print(a)
#     print(b)
#
# d = {'a':11, 'b': 22}
# print(add(**d))

# def add_(a:int, b:int) -> int:
#     print(a)
#     print(b)
#     return a + b
#
# print(add_(3, 4))
# print(add_('hello', 'hai'))

''' wa function to print msg "hello world" if the user input is not present'''

# def func(msg='hello world'):
#     print(msg)
#
#
# func()
# func('hello python')
# func('@')

# def f1(*args, **kwargs):
#     count = 0
#     for _ in args:
#         count += 1
#     for _ in kwargs:
#         count += 1
#     return count
#
#
# print(f1(1, 2, 3, 4, a=10, b=20))
# print(f1(4, 8, m=23, n=21))












































