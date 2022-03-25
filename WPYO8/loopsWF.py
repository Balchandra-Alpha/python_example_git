# a = 10
# if a > 5:
#     print('hello')
#     print('entered if block')
#     print(a)
# print('Execution done')

# num = int(input('Enter a number :'))
# if num % 2 == 0:
#     print('even')

# s = ''
# if s:
#     print(f'{s} is not an empty string')
# print('done')

# a = 10
# if a % 2 == 0: print('even'), print('if block executed')
# print('done')

# a = 11
# if a % 2 == 0:
#     print('even')
# else:
#     print('odd')

# s = input('enter any alphabet')
# if s in 'aeiouAEIOU':
#     print(f'{s} is an vowel')
# else:
#     print(f'{s} is a consonant')


# a = int(input('Enter a number : '))
# print('even') if a % 2 == 0 else print('odd')

# a = 6
# if a % 2 == 0:
#     print('even')
# elif a % 3 == 0:
#     print('odd is divisible by 3')
# elif a % 5 == 0:
#     print('odd is divisible by 5')
# else:
#     print('odd is not divisible by 3 and 5')
# print('done')

# marks = int(input('enter marks'))
# if 0 <= marks <= 100:
#     if marks >= 85:
#         print('distiction')
#     elif marks >= 60:
#         print('first class')
#     elif marks >= 45:
#         print('second class')
#     elif marks >= 35:
#         print('pass')
#     else:
#         print('fail')
# else:
#     print('Enter a vaild marks')
# a = 10
# ''' convert upper case to lower case and lower to upper case'''
# char = input('enter a character : ')
# if char.isalpha():
#     if char.isupper():
#         print(chr(ord(char)+32))
#     else:
#         print(chr(ord(char)-32))
# else:
#     print('Not an alphabet')

##############################
''' check whether a given value is string or not '''
# a = '123'
# if isinstance(a, str):
#     print('string')
# else:
#     print('not a string')

''' check is the entered char is vowel or not, if its an vowel then create a 
dictionary with char and its ascii value pair '''
# a = input("enter a char : ")
# d = {}
# if a.lower() in 'aeiou':
#     d[a] = ord(a)
#     print(d)
# else:
#     print('entered char is not a vowel')

''' check whether a string palindrome or not '''
# word = input('Enter a word : ')
# if word == word[::-1]:
#     print(f'{word} is a palindrome')
# else:
#     print(f'{word} is not a palindrome')

''' check a number is palindrome or not '''
# num = int(input('Enter a number: '))
# b = str(num)
# if b == b[::-1]:
#     print(f'{num} is a palindrome')
# else:
#     print(f'{num} is not a palindrome')

''' find the greatest of three numbers '''
# a = 35
# b = 37
# c = 45
# if a > b and a > c:
#     print(f'{a} greatest')
# elif b > c:
#     print(f'{b} greatest')
# else:
#     print(f'{c} greatest')

''' check if the given char is number or alphabet or special char'''
# char = input('Enter a char : ')
# if char.isalpha():
#     print('alphabet')
# elif char.isdigit():
#     print('Number')
# else:
#     print('special character')
#or
# char = input('Enter a char : ')
# if len(char) == 1:
#     if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
#         print('alphabet')
#     elif '0' <= char <= '9':
#         print('number')
#     else:
#         print('special character')
# else:
#     print('enter a vaild input')

'''check if the given char is key in given dictionary, if it is present 
incriment its value, else initialize to 1'''

# d = {'a': 3, 'e': 3, 'i': 3, 'o': 3, 'u': 3}
# char = input('Enter a char :')
# if char in d:
#     d[char] += 1
# else:
#     d[char] = 1
# print(d)

''' check if the given string is starting with vowel or not '''
# char = input('Enter anything : ')
# if char[0].upper() in 'AEIOU':
#     print('starting with vowel')
# else:
#     print(' Not starting with vowel')

''' check given num is perfect square or not '''
# num = int(input('Enter a number : '))
# temp = num ** 0.5
# if round(temp) ** 2 == num:
#     print(f'{num} is a perfect square')
# else:
#     print(f'{num} is not a perfect square')

''' check if the last digit of the given number is divisible by 3 or not'''
# num = int(input('Enter a number : '))
# last = num % 10
# if last % 3 == 0:
#     print('last digit is divisible by 3')
# else:
#     print('last digit is not divisible by 3')

''' remove a random element from given set,and if removed element is a string
then create it as key and value as its len, if its a number then create it as 
key and its ASCII value as the value'''
# s = {4, 5, 6, 'hello', 9, 'python', 'hai'}
# removed = s.pop()
# d = {}
# if isinstance(removed, str):
#     d[removed] = len(removed)
# else:
#     d[removed] = ord(str(removed))
# print(d)

''' if the len of given string is even, then print it as it is
else reverse it and print it.'''

# s = input('Enter anything :')
# if len(s) % 2 == 0:
#     print(s)
# else:
#     print(s[::-1])

# print(s) if len(s) % 2 == 0 else print(s[::-1])

''' check whether a number is divisible by 7 and 5 both, only 7
only 5, or niether 7 not 5 '''
# num = int(input('Enter a number : '))
# if num % 5 == 0 and num % 7 == 0:
#     print('both 5 & 7 ')
# elif num % 7 == 0:
#     print('only by 7')
# elif num % 5 == 0:
#     print('only by 5')
# else:
#     print('Neither 7 nor 5')

#############################################################
'''while :'''

# start = 1
# while start <= 5:
#     print('Welcome to the python class')
#     start += 1

# i = 10
# while i > 0:
#     print('hello')
#     print(i)
#     i -= 1

''' print numbers from 0 to 4 '''
# num = 0
# while num <= 4:
#     print(num)
#     num += 1

''' print numbers from 10 to 1 '''
# num = 10
# while num > 0:
#     print(num)
#     num -= 1

''' print numbers from -10 to -1'''
# num = -10
# while num != 0:
#     print(num)
#     num += 1

# num = -10
# while num != 1:
#     print(num)
#     num += 2

''' print evens between 0 and 50 '''
# i = 0
# while i <= 50:
#     if i % 2 == 0:
#         print(i)
#     i += 1

''' create list of evens betweeen 0 and 50 '''
# l = []
# i = 0
# while i <= 50:
#     if i % 2 == 0:
#         l.append(i)
#     i += 1
# print(l)

''' traverse through a string using while loop '''
# s = 'Hello python'
# index = 0
# while index < len(s):
#     print(s[index])
#     index += 1

''' find sum of first n natural numbers '''
# num = int(input('Enter a natural number : ' ))
# sum = 0
# i = 1
# if num > 0:
#     while i <= num:
#         sum += i
#         i += 1
#     print(sum)
# else:
#     print('Enter a valid number')

''' count the number of vowels in a given string '''
# msg = 'Python programming is fun'
# index = 0
# count = 0
# while index < len(msg):
#     if msg[index].lower() in 'aeiou':
#         count += 1
#     index += 1
# print(count)

''' print the vowels along with its index'''
# msg = 'Python programming is fun'
# index = 0
# while index < len(msg):
#     if msg[index].lower() in 'aeiou':
#         print(index, msg[index])
#     index += 1

''' traverse through string in reverse order '''
# s = 'Hello python'
# index = len(s)-1
# while index >= 0:
#     print(s[index])
#     index -= 1

''' reverse a given string '''
# msg = input('Enter a string : ')
# # 'nohtyP olleH'
# result = ''
# index = len(msg) -1
# while index > -1:
#     result += msg[index]
#     index -= 1
# print(result)
#
# res = ''
# index = 0
# while index < len(msg):
#     res = msg[index] + res
#     index += 1
# print(res)

'''break, continue, pass '''
# i = 0
# while i < 5:
#     if i == 2:
#         break
#     print(i)
#     i += 1
# else:
#     print('loop executed succesfully')
# print('end')
# print() ################3
# i = 0
# while i < 5:
#     if i == 2:
#         i += 1
#         continue
#     print(i)
#     i += 1
# else:
#     print('loop executed succesfully')
# print('end')
# print()
# i = 0
# while i < 5:
#     if i == 2:
#         pass
#     print(i)
#     i += 1
# else:
#     print('loop executed succesfully')
# print('end')

''' check a number is prime of not '''
# num = int(input('Enter a number :' ))
# divisor = 2
# while divisor < num:
#     if num % divisor == 0:
#         print(f"{num} is not a prime, {divisor}")
#         break
#     divisor += 1
# else:
#     print(f"{num} is prime ")
# print('done')

''' print first ten prime numbers '''
# count = 0
# num = 2
# while count < 10:
#     divisor = 2
#     while divisor < num:
#         if num % divisor == 0:
#             break
#         divisor += 1
#     else:
#         print(f"{num} is prime ")
#         count += 1
#     num += 1

''' create a dictionary as elements of given list as keys and its length as values '''
# company = ['amazon', 'apple', 'netflix', 'amazon','google', 'microsoft', 'instagram']
# d = {}
# index = 0
# while index < len(company):
#     temp = company[index]
#     d[temp] = len(temp)
#     index += 1
# print(d)

''' create a dictionary as elements of given list as keys and 
number of vowels in them as values '''
# company = ['amazon', 'apple', 'netflix','google', 'microsoft', 'instagram']
# d = {}
# index = 0
# while index < len(company):
#     temp = company[index]
#     count = 0
#     i = 0
#     while i < len(temp):
#         char = temp[i]
#         if char.lower() in 'aeiou':
#             count += 1
#         i += 1
#     d[temp] = count
#     index += 1
# print(d)

''' sum of all the digits in a given number '''
# num = int(input('Enter a number : '))
# temp = str(num)
# index = 0
# sum = 0
# while index < len(temp):
#     sum += int(temp[index])
#     index += 1
# print(sum)

# sum = 0
# while num > 0:
#     quotient, remainder = divmod(num, 10)
#     sum += remainder
#     num = quotient
#
# print(sum)

# s = 'hello'
# for char in s:
#     print(char)

# l = [10, 29, [32, 15], 67]
# for num in l:
#     print(num)
#
# se = {10, 29, 32, 15, 67}
# for ele in se:
#     print(ele)
#
# d = {'one': 1, 'two': 2, 'three': 3}
# for item in d:
#     print(item, d[item])
#
# for item in d.items():
#     print(item)
#
# for key, value in d.items():
#     print(key, value, sep=" : ")

# for item in range(1, 11):
#     print(item, end=' ')
# print()
# for item in range(10, 0, -1):
#     print(item, end=' ')
# print()
# for item in range(-10, 0):
#     print(item, end=' ')
# print()
# for item in range(-1, -11, -1):
#     print(item, end=' ')
# print()
''' numbers which are divisible by 3 between given range'''
# for item in range(1, 30):
#     if item % 3 == 0:
#         print(item)

''' print all the numbers between 100 to 200 
whose last digit is divisible by 3'''

# l = []
# for i in range(100, 201):
#     last = i % 10
#     if last % 3 == 0:
#         l.append(i)
# print(l)

''' print all the numbers between 100 to 200 
whoes last two digit is divisible by 3'''

# l1 = []
# for i in range(100, 201):
#     last = i % 100
#     if last % 3 == 0:
#         l1.append(i)
# print(l1)

''' traverse through sequences(str, list, tuple), using range '''
# s = 'hello python'
# for index in range(len(s)):
#     print(s[index], index)
# print()
# l = [10, 12, 'hello', 54, 10, 76, 'python', 32]
# for i in range(len(l)):
#     print(l[i], i)
''' printing odd index char in a given string '''
# s = 'hello python'
# result = ''
# for index in range(len(s)):
#     if index % 2 != 0:
#         result += s[index]
# print(result)

''' get the sum of all the numerical(int, float) in a given list '''
# l = [10, 12, 'hello', 54.76, 10, 76.0, 'python', 32, ['a', 'b', 'c']]
# sum_ = 0
# rest = []
# for item in l:
#     if isinstance(item, (int, float)):
#         sum_ += item
#     else:
#         rest.append(item)
# print(sum_)
# print(rest)

# company = ['apple', 'google', 'amazon', 'netflix', 'instagram', 'meta', 'facebook']
# for item in range(len(company)):
#     temp = company[item]
#     if len(temp) % 2 != 0:
#         company[item] = temp[::-1]
# print(company)

''' reversing a string '''
# s = 'hello python'
# res = ''
# for i in s:
#     res = i + res
# print(res)

# company = ['apple','google', 'amazon', 'apple', 'netflix',
# 'instagram', 'google', 'apple', 'meta', 'amazon', 'facebook']
# res = []
# for item in company:
#     if len(item) % 2 == 0:
#         res.insert(0, item)
# print(res)

#['facebook', 'amazon', 'meta', 'google', 'amazon', 'google']
#['facebook', 'amazon', 'meta', 'google', 'amazon', 'google']
#
# company = ['apple','google', 'amazon', 'apple', 'netflix',
# 'instagram', 'google', 'apple', 'meta', 'amazon', 'facebook']
# res = []
# for item in company:
#     if len(item) % 2 == 0:
#         if item not in res: # avoid repetitions
#             res.insert(0, item)
# print(res)

''' check whether a number is prime or not '''
# num = int(input('ENter a number : '))
# for i in range(2, num):
#     if num % i == 0:
#         print(f"{num} not prime")
#         break
# else:
#     print(f"{num} is a prime")

''' print all the prime numbers between 10 to 30 '''
# for num in range(10, 31):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(f"{num} is a prime")
#
# '''add first 10 prime number to a list '''
# num = 2
# count = 0
# l = []
# while count < 10:
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         l.append(num)
#         count += 1
#     num += 1
# print(l)

# l1 = [1, 2, 3, 4, 5]
# l2 = [10, 20, 30, 40]
# # l3 = [100, 200, 300, 400, 500]
# for x, y in zip(l1, l2):
#     print(x, y, sep=' : ')
# for item in zip(l1, l2):
#     print(item)
#
# # print(list(zip(l1, l2)))
# from itertools import zip_longest
# for item in zip_longest(l1, l2, fillvalue='Hello'):
#     print(item)

# s = 'hello'
# a = enumerate(s)
# print(list(a))
# for x, y in enumerate(s):
#     print(x, y, sep="  ")

''' print the actual index of the vowels in a given
 string '''
# string = 'hai hello how are you how are you doing'
# for index, char in enumerate(string):
#     if char.lower() in 'aeiou':
#         print(index, char, sep= '>>')

''' extend all the elements with a file extention pdf '''
# company = ['apple','google', 'amazon', 'apple', 'netflix',
# 'instagram', 'google', 'apple', 'meta', 'amazon', 'facebook']
# l = []
# from itertools import zip_longest
# for item in zip_longest(company, list(), fillvalue='pdf'):
#     # print(item)
#     res = item[0] + '.' + item[1]
#     l.append(res)
# #
# print(l)
# print(dir(zip_longest))

# files = ['apple.pdf', 'google.pdf', 'amazon.pdf', 'apple.pdf', 'netflix.pdf',
# 'instagram.pdf', 'google.pdf', 'apple.pdf', 'meta.pdf', 'amazon.pdf', 'facebook.pdf']


''' create a dictionary char as key and its count as its value'''
# s = 'abrakadabraaa'
# d = {}
# for char in s:
#     d[char] = s.count(char)
# print(d)

# for char in s:
#     if char not in d:
#         d[char] = 1  #initialization
#     else:
#         d[char] += 1 #incrementation
# print(d)

# from collections import defaultdict
# s = 'abrakadabraaa'
# dd = defaultdict(int)
# print(dd)
# for char in s:
#     dd[char] += 1
# print(dd)
# print(type(dd))

# company = ['apple','google', 'amazon', 'apple', 'netflix',
# 'instagram', 'google', 'apple', 'meta', 'amazon', 'facebook']
# d = {}
# for index, element in enumerate(company):
#     if element not in d:
#         d[element] = [index]
#     else:
#         d[element].append(index)  #d[element] += [index]
# print(d)

# from collections import defaultdict
# dd = defaultdict(list)
# for index, element in enumerate(company):
#     dd[element] += [index]
# print(dd)

files = ['apple.txt', 'google.pdf', 'amazon.txt', 'netflix.pdf',
'instagram.pdf', 'apple.pdf', 'meta.txt', 'facebook.txt']
# d = {}
# for item in files:
#     temp = item.split('.')
#     if temp[-1] not in d:
#         d[temp[-1]] = {temp[0]}
#     else:
#         d[temp[-1]].add(temp[0])
# print(d)
#
# from collections import defaultdict
# dd = defaultdict(set)
# for item in files:
#     temp = item.split('.')
#     dd[temp[-1]].add(temp[0])
# print(dd)

# something = 'python is a programming language programs are interesting'
# from collections import defaultdict
# dd = defaultdict(tuple)
# temp = something.split()
# for item in temp:
#     dd[item[0]] += (item,)
# print(dd)
''' create a dictioary with words as keys and number of vowels in them as values'''

#pattern printing, Indentation using formatting strings
# a = 'Ironman'
# b = 'Thanos'

# print(a, b) #Ironman Thanos
# print(f'{a:<10}, {b:<10}') #"Ironman   , Thanos   "
# print(f'{a:<10}, {b:>10}') # "Ironman   ,     Thanos"
# print(f'{a:^12}, {b:^10}') # "  Ironman   ,   Thanos  "

'''
* 
* * 
* * * 
* * * *
'''
# for i in range(1, 5):
#     for j in range(1, i+1):
#         print('* ', end='')
#     print()

# for i in range(1, 5):
#     print(f"{'* '* i:<8}")
#
# for i in range(1, 5):
#     print(f"{'* '* i:>8}")
#
# for i in range(1, 5):
#     print(f"{'* '* i:^8}")
# print()
# for i in range(4, 0, -1):
#     print(f"{'* ' * i:<8}")
#
# for i in range(4, 0, -1):
#     print(f"{'* ' * i:>8}")
#
# for i in range(4, 0, -1):
#     print(f"{'* ' * i:^8}")
# '''
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# '''
# ref = ''
# for i in range(1, 5):
#     ref += str(i) + ' '
#     print(f'{ref:<8}')
# '''
# A
# A B
# A B C
# A B C D
# '''
# ref = ''
# for i in range(ord('A'), ord('E')):
#     ref += chr(i) + ' '
#     print(ref)

'''
A 
A 
A 
A B
A 
A B C 
A 
A B C D
'''
# ref = ''
# for i in range(ord('A'), ord('E')):
#     ref += chr(i) + ' '
#     print('A')
#     print(ref)

# l = []
# for i in range(1, 6):
#     l.append(i)
# print(l)
#
# l = [1, 2, 3, 4, 5]
# l2 = []
# for i in l:
#     if i % 2 != 0:
#         temp = i ** 2
#         l2.append(temp)
# print(l2)
#
# l = [1, 2, 3, 4, 5]
# l2 = [i ** 2 for i in l if i % 2 != 0]
# print(l2)

''' get all the char with even index in a string '''
# s = 'hello python'
# l = [s[i] for i in range(len(s)) if i % 2 == 0]
# print(''.join(l))

# '''get all the vowels in a string '''
# s = 'hello python'
# l = [i for i in s if i.lower() in 'aeiou']
# print(''.join(l))
#
# ''' create list from elemnts of below list which are staring from vowels'''
# company = ['apple','google', 'amazon', 'apple', 'netflix',
# 'instagram', 'google', 'apple', 'meta', 'amazon', 'facebook']
# l = [i for i in company if i[0].lower() in 'aeiou']
# print(l)
#
# ''' create list from elemnts of below list which are having length more than 5'''
# l1 = [i for i in company if len(i) > 5]
# print(l1)
#
# ''' create list by reversing the elemnts of below list which are staring from vowels'''
# l = [i[::-1] for i in company if i[0].lower() in 'aeiou']
# print(l)

# s = 'apple'
# if len(s) % 2 == 0:
#     print(s)
# else:
#     print(s[::-1])
# True statement if cond else False statement

# print(s) if len(s) % 2 == 0 else print(s[::-1])

# company = ['apple','google', 'amazon', 'apple', 'netflix',
# 'instagram', 'google', 'apple', 'meta', 'amazon', 'facebook']
# l = []
# for item in company:
#     if len(item) % 2 == 0:
#         l.append(item)
#     else:
#         l.append(item[::-1])
# print(l)

''' add elements not starting with vowel as it is if its length is even , else reverse it'''
# l = [item if len(item) % 2 == 0 else item[::-1] for item in company if item[0].lower() not in 'aeiou']
# print(l)

'''create a list which have remainders when elements of specified list 
is divisible by 3 '''
# l = [3, 9, 11, 16, 19, 23]
# l1 = [i for i in l if i % 3 == 0] #[3, 9]
# l2 = [i % 3 for i in l] # [0, 0, 2, 1, 1, 2]
# print(l1, l2)

'''create a list with elements whose last digit is divisible by 3 '''
# nums = [1234, 3421, 1423, 1756, 7869, 4576]
# res = [item for item in nums if (item % 10) % 3 == 0]
# res2 = [item for item in nums if int(str(item)[-1]) % 3 == 0]
# print(res)
# print(res2)
# l = []
# for item in nums:
#     temp = str(item)
#     if int(temp[-1]) % 3 == 0:
#         l.append(item)
# print(l)

# l = [(i, j) for i in range(1, 5) for j in range(1, 5) if i < j]
# print(l)

''' create a list with elements such that if ending with vowels add as 
it is, if ending with consonants then add 'hello' '''
# comp = ['apple', 'google', 'microsoft@', 'google0', 'apple',
# 'amazon', 'netflix', 'apple2', 'google']
# l = [item if item[-1].lower() in 'aeiou' else 'hello' for item in comp if item[-1].isalpha()]
# print(l)


# new = ['hello', 'guys', 24.5, 'welcome', 'to', 87, 'my', 19, 'youtube', 'chanel']
# l = [item if len(item) % 2 == 0 else item[::-1] for item in new if isinstance(item, str)]
# print(l)

# company = ['apple','google', 'amazon', 'apple', 'netflix',
# 'instagram', 'google', 'apple', 'meta', 'amazon', 'facebook']

# l = [item for item in company if company.count(item) == 1]
# print(l)
# s = {item for item in company}
# print(s)

# l = [{x, y} for x, y in enumerate(company)]
# print(l)
# print(dict(l))
# new = [item for item in zip(range(len(company)), company)]
# print(dict(new))

company = ['apple','google', 'instagram', 'netflix','meta', 'amazon', 'facebook']
# d = {item[0]: item[-1] for item in enumerate(company)}
# print(d)
# d = {x: y for x, y in enumerate(company)}
# print(d)

''' create dict for repeated char in string as key and its count as value'''
# s = 'hai hello how are you gentlemen'
# d1 = {}
# for char in s:
#     if s.count(char) > 1:
#         d1[char] = s.count(char)
# print(d1)
#
# d = {char: s.count(char) for char in s if s.count(char) > 1}
# print(d)

'''create dictionary of words as keys and its len as value'''
s = 'hai hello how are you gentlemen how come you are here'
# res = {item: len(item) for item in s.split()}
# print(res)

''' flip the keys and values'''
# d = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
# d1 = {}
# for x, y in d.items():
#     d1[y] = x
# print(d1)
#
# d2 = {y: x for x, y in d.items()}
# print(d2)

''' create a dict such that element should be key and value should be its len if element
is a string, else value should be 'not string' '''
new = ['hello', 'guys', 24.5, 'welcome', 'to', 87, 'my', 19, 'youtube', 'chanel']
# d = {item: len(item) if isinstance(item, str) else 'Not String' for item in new}
# print(d)

'''create a dictionary such that index as key and element as it is if len of string is even , else reverse it for value'''
# d = {index: item if len(item) % 2 == 0 else item[::-1] for index, item in enumerate(new) if isinstance(item, str)}
# print(d)

''' Creating Dictionary of city and population pairs using Dict Comprehension '''
cities = ['Tokyo',
          'Delhi',
          'Shanghai',
          'Sao Paulo',
          'Mumbai'
          ]
population = ['38,001,000',
              '25,703,168',
              '23,740,778',
              '21,066,245',
              '21,042,538'
              ]
# d = {x: y for x, y in zip(cities, population)}
# print(d)
# d = {cities[i]: population[i] for i in range(len(cities))}
# print(d)
''' Create a dictionary of dialcode and country from the following list '''
dial_codes = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan')
    ]
# d = {item[0]: item[1] for item in dial_codes}
# d = dict(dial_codes)
# print(d)
''' Building a dictionary whose price value is more than 200'''
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# d = {item : prices[item] for item in prices if prices[item] > 200}
# d1 = {key: value for key, value in prices.items() if value > 200}
# print(d)
# print(d1)










