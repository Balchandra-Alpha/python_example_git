# a = int(input('Enter a number : '))
# if a % 2 == 0:
#     print(f'{a} is even')
# else:
#     print(f'{a} is odd')
# print('code executed')

# a = [10]
# if a:
#     print('a is not empty')
# else:
#     print('a is empty')
#
# a = 10
# b = 10
# c = 10
# if a > b and a > c:
#         print(f'{a} is the greatest num')
# elif b > c:
#         print(f'{b} is the greatest num')
# else:
#     print(f'{c} is the greatest num')

# a = 20
# if a > 10: print('a is greater than 10'),print('hello')
# a = 21
# print('even') if a % 2 == 0 else print('odd')

# num = int(input('Enter a number :'))
# if num > 0:
#     print('positive')
# elif num < 0:
#     print('negative')
# else:
#     print('zero')

''' convert upper case char to lower case char '''
# char = input('Enter any alphabet ')
# if 'a' <= char <= 'z':
#     print(chr(ord(char) - 32))
# elif 'A' <= char <= 'Z':
#     print(chr(ord(char) + 32))
# else:
#     print(f'{char} is not an alphabet')

''' check whether a given char is vowel or not '''
# char = input('Enter any alphabet ')
# if char.upper() in 'AEIOU':
#     print(f'{char} is a vowel')
# else:
#     print(f'{char} is not a vowel')

''' create key as char and value as its ASCII value if char is vowel or numeric'''
# char = input('Enter any alphabet ')
# d = {}
# if char.upper() in 'AEIOU' or '0' <= char <= '9':
#     d[char] = ord(char)
# print(d)

'''check if the key(alphabet) is present in a dictionary, if its present then increment its value by 1 , else 
 initialise to 1'''

# d = {'a':2, 'e':4, 'i':3, 'o': 2, 'u':1}
# char = input('Enter any alphabet ')
# if char.isalpha():
#     if char in d:
#         d[char] += 1
#     else:
#         d[char] = 1
# else:
#     print(f'{char} is not an alphabet')
# print(d)

# value = 10
# if isinstance(value, str):
#     print(len(value), f'is the length of {value}')
# else:
#     print(f'{value} is not a string')

''' check whether a string is palindrome or not '''
# s = 'kannada'
# if s[::-1] == s:
#     print(f'{s} is palindrome')
# else:
#     print(f'{s} is not palindrome')@

''' check whether given char belongs to alphabets, numbers or any spl char'''
# char = input('Enter any alphabet ')
# if char.isalpha():
#     print('alphabet')
# elif char.isdigit():
#     print('number')
# else:
#     print('spl character')

'''check whether a number is perfect square or not '''
# num = 16
# temp = num ** 0.5
# if temp % 1 == 0:
#     print('perfect square')
# else:
#     print('not perfect square')

''' get a marks from user and categorize that to respective class '''
# marks = -100
# if marks <= 100 and marks >= 0:
#     if 85 <= marks:
#         print('distiction')
#     elif 60 <= marks:
#         print('first class')
#     elif 45 <= marks:
#         print('second class')
#     elif 35 <= marks:
#         print('pass')
#     else:
#         print('fail')
# else:
#     print('Enter a valid marks')
# print('code executed')

# ''' remove a random element from a set and create a dict with removed element as key and its length as its value '''
# s = {1, 'hello', 'hai', 3, 'python', False, (1, 2, 3)}
# temp = s.pop()
# d = {}
# if isinstance(temp, (str, tuple)):
#     d[temp] = len(temp)
# elif isinstance(temp,  bool):
#     d[temp] = int(temp)
# else:
#     d[temp] = ord(str(temp))
# print(d)



# count = 0
# if count < 3:
#     print('hello world')
#     count += 1

# ''' -10 to -1'''
# c = -1
# while c > -11:
#     print(c)
#     c -= 1

''' print 50 evens in a list from a given number'''
# l = []
# count = 1
# ref = 0
# while ref < 50:
#     if count % 2 == 0:
#         l.append(count)
#         ref += 1
#     count += 1
# print(l)
# print(len(l))

'''wap if the length of given string is even then print as it is, else reverse it and print'''
# string = input('Enter anything : ')
# if len(string) % 2 == 0:
#     print(string)
# else:
#     print(string[::-1])

'''•	check whether a entered 2 digit number is prime or not
(hint:if the number is not a prime then it will have a divisor with in (num ** 0.5))
'''
# num = int(input('Enter two digit number :'))
# if 1 < num < 100:
#     if num % 2 == 0:
#         print(f'{num} is not a prime, divisor is 2')
#     elif num % 3 == 0:
#         print(f'{num} is not a prime, 3')
#     elif num % 5 == 0:
#         print(f'{num} is not a prime, 5')
#     elif num % 7 == 0:
#         print(f'{num} is not a prime, 7')
#     else:
#         print(f'{num} is a prime')
# else:
#     print('Enter a valid number')

''' wap to check whether last digit of the number is divisible by 3 or not '''
# num = int(input('Enter a number :'))
# if (num % 10) % 3 == 0:
#     print(f'last digit {num % 10} is divisble by 3')
# else:
#     print(f'last digit {num % 10} is not divisble by 3')

# if int(str(num)[-1]) % 3:
#     print(f'last digit {num % 10} is not divisble by 3')
# else:
#     print(f'last digit {num % 10} is divisble by 3')

''' sum of first n natural numbers '''
# num = int(input('Enter a number :'))
# sum = 0
# while num > 0:
#     sum += num
#     num -= 1
# print(sum)

''' factorial of given number '''
# num = int(input('Enter a number :'))
# factorial = 1
# while num > 0:
#     factorial *= num
#     num -= 1
# print(factorial)

''' sum of all the digits in a given number '''
# num = int(input('Enter a number :'))
# sum = 0
# count = 0
# while num > 0:
#     x, y = divmod(num, 10)
#     sum += y
#     num = x
#     count += 1
# print(sum)
# print(count)

# s = 'hello python'
# index = 0
# while index < len(s):
#     print(s[index])
#     index += 1

'''wap to create even and odd numbers list using digits in the given number '''

# even = []
# odd = []
# num = int(input('Enter a number :'))
# while num > 0:
#     x, y = divmod(num, 10)
#     if y % 2 == 0:
#         even += [y]
#     else:
#         odd += [y]
#     num = x
# print(even)
# print(odd)

'''wap to count no of vowels and consonants in a given string '''
# s = 'Either you die as a hero or live long enough to see yourself as a villainn'
# v_count = 0
# c_count = 0
# index = 0
# while index < len(s):
#     if s[index].isalpha():
#         if s[index] in 'aeiouAEIOU':
#             v_count += 1
#         else:
#             c_count += 1
#     index += 1
#
# print(v_count)
# print(c_count)

''' reverse given string using while loop '''
# s = input('Enter anything : ')
# index = 0
# result = ''
# while index < len(s):
#     result = s[index] + result
#     index += 1
#     print(result)
# print()
# index = len(s)-1
# result = ''
# while index > -1:
#     result += s[index]
#     index -= 1
#     print(result)


''' wap to remove all the odd length string and keep a count of it'''
# company = ['apple', 'google', 'microsoft', 'meta', 'flipkart', 'amazon', 'netflix', 'bharath pe', 'disney', 'tesla']
# index = 0
# no_odd = 0
# while index < len(company):
#     temp = company[index]
#     if len(temp) % 2:
#         no_odd += 1
#         company.remove(temp)
#     else:
#         index += 1
# print(company)
# print(no_odd)

'''wap to calculate the sum of numbers in the given list '''
# l = [20, 11, 19, 'string', [10, 20, 30], True, 'Python', 10.7, 20, (1, 2, 3)]
# sum = 0
# index = 0
# while index < len(l):
#     temp = l[index]
#     if isinstance(temp, (int, float)):
#         sum += temp
#     elif isinstance(temp, (list, tuple)):
#         nes_i = 0
#         while nes_i < len(temp):
#             sum += temp[nes_i]
#             nes_i += 1
#     index += 1
# print(sum)

''' wap to create dict as elements of list as key and its len as value '''
# company = ['apple', 'google', 'microsoft', 'meta', 'flipkart', 'amazon', 'netflix', 'bharath pe', 'disney', 'tesla']
# d = {}
# index = 0
# while index < len(company):
#     temp = company[index]
#     d[temp] = len(temp)
#     index += 1
# print(d)

''' wap to create a dict such that len of element should be key and all the elemnts having same length should
be present in value as list'''
# company = ['apple', 'google', 'microsoft', 'meta', 'flipkart', 'amazon', 'netflix', 'bharathpe', 'disney', 'tesla']
# d = {}
# index = 0
# while index < len(company):
#     temp = company[index]
#     if len(temp) not in d:
#         d[len(temp)] = [temp]
#     else:
#         d[len(temp)].append(temp)
#     index += 1
# print(d)

'''wap to create dictionary such that elements of list as keys and no of vowels in them as values'''
# company = ['apple', 'google', 'microsoft', 'meta', 'flipkart', 'amazon', 'netflix', 'bharathpe', 'disney', 'tesla']
# d = {}
# index = 0
# while index < len(company):
#     temp = company[index]
#     nes_i = 0
#     v_count = 0
#     while nes_i < len(temp):
#         if temp[nes_i] in 'aeiouAEIOU':
#             v_count += 1
#         nes_i += 1
#     d[temp] = v_count
#     index += 1
# print(d)

''' wap to check whether the given number is prime or not'''
# num = int(input('Enter a number : '))
# num = 11
# divisor = 2
# while divisor < num:
#     if num % divisor == 0:
#         print(f'{divisor} is a divisor of {num}')
#         print(f'{num} is not prime')
#         break
#     divisor += 1
# else:
#     print('prime')
# print('hello')

# start = 0
# while start < 9:
#     if start == 9 // 2:
#         start += 1
#         continue
#     else:
#         print(start)
#     start += 1

''' wap to print first 10 prime numbers '''
# count = 0
# num = 2
# while count < 10:
#     divisor = 2
#     while divisor < num:
#         if num % divisor == 0:
#             break
#         divisor += 1
#     else:
#         print(num)
#         count += 1
#     num += 1

# numbers = range(5)
# print(numbers)
# print(len(numbers))
# for num in range(1, 5, 2):
#     print(num)

# n = int(input('Enter a number'))
# sum = 0
# for item in range(1, n+1):
#     sum += item
# print(sum)

''' calculate the sum of all the numeric values in a given string 
and also extract all the alpha characters'''
# msg = input('Enter a number')
# sum = 0
# ref = ''
# for i in msg:
#     if i.isdigit():
#         sum += int(i)
#     elif i.isalpha():
#         ref += i
# print(sum)
# print(ref)


#split()
# s = 'python is a programming language'
# # ['python', 'is', 'a', 'programming', 'language']
# l = []
# ref = ''
# for i in s:
#     if i.isspace():
#         l.append(ref)
#         ref = ''
#     else:
#         ref += i
# else:
#     l.append(ref)
# print(l)

# n = int(input('Enter a number:'))
# for item in range(1, 50):
#     for i in range(2, item):
#         if item % i == 0:
#             break
#     else:
#         print('prime', item)

# l = [10, 34, 56, 23, 11, 65, 70, 43]
# s = ['python', 'is', 'a', 'programming', 'language']
# print(s)
# print(max(s, key=len))
# print(min(s))

# m = ''
# for i in s:
#     if m < i:
#         m = i
# print(m)

# company = ['apple', 'google', 'microsoft', 'meta', 'flipkart', 'amazon', 'netflix', 'bharathpe', 'disney', 'tesla']
# l = []
# for element in company:
#     count = 0
#     for char in range(len(element)):
#         if element[char] in 'aeiouAEIOU':
#             count += 1
#     if count % 2 == 0:
#         l.append(element)
# print(l)

# company = ['apple', 'google', 'microsoft', 'google', 'flipkart', 'amazon', 'netflix', 'apple', 'google']
# d = {}
# for i in enumerate(company):
#     if i[-1] not in d:
#         d[i[-1]] = [i[0]]
#     else:
#         d[i[-1]].append(i[0])
# print(d)

# n = enumerate(company, start=10)
# print(n)
# print(list(n))

# a = str(company)
# print(a, type(a))

# d = {}
# for index, item in enumerate(company):
#     if item not in d:
#         d[item] = [index]
#     else:
#         d[item].append(index)
# print(d)

# from itertools import zip_longest
# l1 = [1, 2, 3, 4, 5]
# l2 = [1, 4, 9, 16]
# l3 = ['hello', 'hai']
# n = zip_longest(l1, l2, l3, fillvalue='Extra')
# print(n)
# print(list(n))

# # from itertools import zip_longest
# l1 = [1, 2, 3, 4, 5]
# l2 = [1, 4, 9, 16]
# # l3 = ['hello', 'hai']
# n = zip(l1, l2)
# print(n)
# print(list(n))

# from itertools import zip_longest
# company = ['apple', 'google', 'microsoft', 'google', 'flipkart', 'amazon', 'netflix', 'apple', 'google']
# l = []
# for item in zip_longest(company, list(), fillvalue='pdf'):
#     temp = item[0] + '.' + item[1]
#     l.append(temp)
# print(l)

# files = ['apple.pdf', 'google.pdf', 'microsoft.txt', 'google.pdf', 'flipkart.txt', 'amazon.txt', 'netflix.txt', 'apple.pdf']
# for item in files:
#     temp = item.split('.')
#     print(temp[0])

''' create a dict such that extension as key and file names wrt that extension as values '''
# files = ['apple.pdf', 'google.pdf', 'microsoft.txt', 'google.pdf', 'flipkart.txt', 'amazon.txt', 'netflix.txt', 'apple.pdf']
# d = {}
# for item in files:
#     temp = item.split('.')
#     if temp[1] not in d:
#         d[temp[1]] = [temp[0]]
#     elif temp[0] in d[temp[1]]:
#             continue
#     else:
#         d[temp[1]] += [temp[0]]
# print(d)

''' '''
# company = ['apple', 'google', 'microsoft', 'google', 'apple', 'amazon', 'netflix', 'apple', 'google']
# d = {}
# for item in company:
#     if item not in d:
#         d[item] = 1
#     else:
#         d[item] += 1
# print(d)
#
# from collections import defaultdict
# d = defaultdict(int)
# for item in company:
#     d[item] += 1
# print(d)

''' create a dict such that starting char of each word as key and the word in the value as list'''
# s = 'python is a programming language programs are always interesting'
# d = {}
# for item in s.split():
#     if item[0] not in d:
#         d[item[0]] = [item]
#     else:
#         d[item[0]] += [item]
# print(d)
#
# from collections import defaultdict
# d = defaultdict(list)
# for item in s.split():
#     d[item[0]] += [item]
# print(d)

'''
*
* *
* * *
* * * *
'''
# for i in range(1, 5):
#     print("* " * i)

'''
      *
    * *
  * * *
* * * *
'''
# for i in range(1, 5):
#     print(f"{'* ' * i:>8}")

# print('hello'.center(20, '@'))

'''
   *    
  * *   
 * * *  
* * * * 
'''

# for i in range(1, 5):
#     print(f"{'* ' * i:^12}")

'''
1 
1 2
1 2 3
1 2 3 4
'''
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()

# res = ''
# for i in range(1, 5):
#     res += str(i) + ' '
#     print(f'{res:^10}')

'''
a 
a b 
a b c 
a b c d 
'''
# res = ''
# for i in range(ord('a'), ord('e')):
#     res += chr(i) + ' '
#     print(res)

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
# res = ''
# for i in range(ord('A'), ord('E')):
#     res += chr(i) + ' '
#     print('A')
#     print(res)


# for i in range(4, 0, -1):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()

# a = 'Iron'
# b = 'Man'
# # print(a, b)
# print(f'{a:<10},{b:<10}')
# print(f'{a:>10},{b:>10}')
# print(f'{a:<10},{b:>10}')
# print(f'{a:^10},{b:^10}')


# company = ['apple', 'google', 'microsoft', 'google', 'apple', 'amazon', 'netflix', 'apple', 'google']
# from collections import defaultdict
# d = defaultdict(int)
# for item in company:
#     if item not in d:
#         for i in item:
#             if i in 'aeiouAEIOU':
#                 d[item] += 1
# print(d)

# a = 'apple'
# b = 'orange'
#
# print(f'{a:^25},{b:^15}')

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

# for i in range(4, 0, -1):
#     print(f'{"* "*i:<8}')

'''
1 
1 2
1 2 3
1 2 3 4 
'''
# ref = ''
# for i in range(1, 5):
#     ref += str(i) + ' '
#     print(ref)
#
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
#
# '''
# A
# A
# A
# A B
# A
# A B C
# A
# A B C D
# '''
# ref = ''
# for i in range(ord('A'), ord('E')):
#     print('A')
#     ref += chr(i) + ' '
#     print(ref)





















