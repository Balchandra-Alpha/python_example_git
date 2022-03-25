# a = 10
# b = 'apple'
# print(bool(b))
# if 11 > a:
#     print('hello')
#     print('hai')
#     print('Entered if block')

# if 11 > a: print('Entered if block'), print(a), print(b), print('hello')

# if 10 > a:
#     print('hello')
#     print('hai')
#     print('Entered if block')
# else:
#     print('Entered else block')

# print('entered if block') if a > 5 else print('Entered else block')

# print('entered if block') if a > 11 else print('Entered else block')

# print('statement'), print('entered if block') if a > 11 else print('Entered else block')

# print('statement'), print('entered if block') if a > 5 else print('Entered else block')

# a = 13
# b = 'h'
# if a > 11 or b:
#     if a == 12:
#         print('nested if executed')
#     print('entered if block')
# elif a > 5:
#     print('entered elif block')
# elif a == 0:
#     print('entered 2nd elif block')
# else:
#     print('entered else block')

# z = float(input('Enter a number  :'))
# if z > 0:
#     print(f'{z} is a positive number')
# elif z < 0:
#     print(f'{z} is a negative number')
# else:
#     print(f'{z} is zero')

# z = float(input('Enter a number  :'))
# if z > 0:
#     print(f'{z} is a positive number')
# elif z <= 0:
#     if z < 0:
#         print(f'{z} is a negative number')
#     else:
#         print(f'{z} is zero')

# var = 10
# if isinstance(var, str):
#     print(var[2], f'is the 2nd indexed element of {var}')
# else:
#     print(f'{var} is not a string but its a {type(var)}')


# var = input('Enter anything')
# index = abs(int(input('Enter a index to find character')))
# if isinstance(var, str):
#     if len(var) > index:
#         print(var[index], f'is the {index}th indexed element of {var}')
#     else:
#         print(f'{index} num is out of range for {var} given')
# else:
#     print(f'{var} is not a string but its a {type(var)}')

''' greatest of three numbers '''
# a = 30
# b = 25
# c = 20
#
# if a > b and a > c:
#     print(a, 'is the largest ')
# elif b > c:
#     print(b, 'is largest')
# else:
#     print(c, 'is the largest')

############################
# char = input('Enter a character', )
# d = {}
# if char.upper() in 'AEIOU':
#     print(f'The given char "{char}" is a vowel')
#     d[char] = ord(char)
# else:
#     print(f'The given char "{char}" is not a vowel')
# print(d)
##########################

# hour = int(input('Enter a number '))
# print(type(hour))
# print(f'{hour} hours have {hour * 60} minutes')

#############################

# char = input('Enter a character ', )
# if char.isupper():
#     print(char.lower())
# else:
#     print(char.upper())

##############################

'''remove a random ele from set and create a dict with removed element as a key and its length as value'''

# s = {1, 'hello', 3, 'hai', 10, 'python'}
# removed = s.pop()
# d = {}
# if isinstance(removed, str):
#     d[removed] = len(removed)
# else:
#     d[removed] = ord(str(removed))
# print(d)

###########################

# num = int(input('Enter a number ', ))
# if num % 7 and num % 5:
#     print(f'{num} is divisible by both 7 and 5')
# else:
#     print(f'{num} is not divisible by both 7 and 5')


###################################
# num2 = int(input('Enter a number ', ))
# if num2 % 2:
#     print(num2, 'is odd')
# else:
#     print(num2, 'is even')

# s = input('Enter a word')
# if s.lower() == s.lower()[::-1]:
#     print(f'{s} is a palindrome')
# else:
#     print(f'{s} is not a palindrome')

# num = int(input('Enter a number '))
# print(type(num))
# temp = str(num)[-1]
# if int(temp) % 3:
#     print(f'last digit {temp} is not divisible by 3')
# else:
#     print(f'last digit {temp} is divisible by 3')
''' or '''
# temp = num % 10
# if temp % 3:
#     print(f'last digit {temp} is not divisible by 3')
# else:
#     print(f'last digit {temp} is divisible by 3')

''' check given str is even length or odd '''
# string = input('Enter a  word ')
# if len(string) % 2:
#     print(f'given string {string} is of odd length')
# elif len(string) == 0:
#     print('given an empty string')
# else:
#     print(f'given string {string} is of even length')

''' wap such that if the user input key is in dictionary then incriment it, else initiate it to value 1'''
# d = {'apple': 3, 'microsoft': 4, 'google': 7, 'facebook': 3, 'youtube': 10, 'Tesla': 1}
# name = input('Enter a company name ')
# if name in d:
#     d[name] += 1
# else:
#     d[name] = 1
# print(d)

''' wap to check whether the given number is perfect square or not '''
# num = int(input("Enter a number "))
# temp = num ** 0.5
# print(temp)
# print(round(temp))
# if round(temp) ** 2 == num:
#     print(f'the given number {num} is a perfect square')
# else:
#     print(f'the given number {num} is not a perfect square')

'''wap if the len of given str in even then print as it is, else reverse it and print'''
# string = input('Enter a string :')
# temp = len(string)
# if temp % 2:
#     print(string[::-1])
# else:
#     print(string)

# n = int(input('Enter a number with maximum 2 digit'))
# if len(str(n)) < 3:
#     if n % 2 == 0:
#         print(f'{n} is divisible by 2')
#     elif n % 3 == 0:
#         print(f'{n} is divisible by 3')
#     elif n % 5 == 0:
#         print(f'{n} is divisible by 5')
#     elif n % 7 == 0:
#         print(f'{n} is divisible by 7')
#     else:
#         print('given number is prime')
# else:
#     print('Given number is more than 2 digit, enter a valid number')








