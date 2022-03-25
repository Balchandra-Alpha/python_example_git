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

# msg = "hi my name is {} and I'm {} years old"
# print(msg.format('Arjun', 25))
# o/p ==> hi my name is Arjun and I'm 25 years old

# msg = "hi my name is {1} and I'm {0} years old"
# details = input('Enter your name')
# print(msg.format(25, details))
# o/p ==> hi my name is salman and I'm 25 years old

# msg = "hi my name is {name} and I'm {age} years old"
# details = input('Enter your name')
# print(msg.format(age=25, name=details))
#o/p ==> hi my name is Arjun and I'm 25 years old

# greet = ("hi, welcome {}")
# name = input('enter ur name')
# print(greet.format(name))

# name = input('enter your name: ')
# age = input('enter your age ')
# text = f"hi my name is {name} and i'm {age} years old"
# print(text)
# a = int(input('enter value:'))
# b = int(input('enter value '))
# msg = f"there are {a * b} hours in {b} day"
# print(msg)
# msg2 = f"{b} day have {a * b * 60} minutes"
# print(msg2)

# name = input('enter name:')
# print(F'Hi hello {name}')

# msg = "hi my name is \nithin, i'm from \tamilnadu"
# print(msg)
# o/p ==> hi my name is
#         ithin, i'm from 	amilnadu

# msg = "hi my name is \\nithin, i'm from \\tamilnadu"
# print(msg)
# o/p ==> hi my name is \nithin, i'm from \tamilnadu

# msg = R"hi my name is \rithin, i'm from \tamilnadu"
# print(msg)

# s = 'hello world'
# new = s.upper()
# print(s, new, sep=new)

# a = 24
# b = 1
# msg = "There are {a}  hours in {b}".format(a=24, b=1)
# print(msg)

# s = 'hello'
# print(s.upper())

# s2 = 'python'
# print(s2.swapcase())

# s = 'balchandra.alpha@GMAIL.c0M'
# a = s.capitalize()
# print(a)

# msg = 'hello python welcome to programming language'
# print(msg.index('programming', -35, 35))

# s = lambda a, b,/,*, c, d: a + b + c + d
# print(s(10, 20, c=30, d=40))

# my_list = ['hi', 'hello']
# for item in my_list:
#     print('hi')
#     my_list.append(item.upper())
# print(my_list)

# l = [1, 2, 3, 4, 5]
# m = l
# n = m
# c = map(lambda x, y, z:x + y + z, l, m, n)
# print(list(c))

new = 'hi hello how are you how are you doing'
var = new.split()
print(var, len(var), sep='\n')
