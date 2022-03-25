# print('Hello Python')

# count = 0
# while count < 10:
#     print('Hello Python')
#     print(count)
#     count += 2
# else:
#     print('Loop Successfully executed')

# list_even = []
# list_odd = []
#
# num = 0
# while num <= 20:
#     if num % 2 == 0:
#         list_even.append(num)
#         print(list_even)
#     else:
#         list_odd.append(num)
#         print(list_odd)
#     num += 1
# else:
#     print('Loop Executed')
# print(list_even)
# print(list_odd)

# s = 'hello'
# index = 0
# while index < len(s):
#     print(s[index])
#     index += 1
# else:
#     print('loop executed')

# s = 'hello python'
# index = 0
# count = 0
# while index < len(s):
#     if s[index].lower() in 'aeiou':
#         print(index, s[index])
#     else:
#         print('else block of if ')
#         count += 1
#     index += 1
# else:
#     print('else block of while')
# print(count)

''' calculate the first n number sum '''
# num = int(input('Enter a number :'))
# sum = 0
# start = 1
# while start < num+1:
#     sum += start
#     start += 1
# print(sum)

'''calculate the sum of all the digits present in a num'''
# num = int(input('Enter any number ')) # 12345 ==> int
# temp = str(num)     # '12345' ==> str
# index = 0
# sum = 0
# while index < len(temp):
#     sum += int(temp[index])
#     index += 1
#     print(sum)
# print(sum)

# num = int(input('Enter any number '))
# sum = 0
# while num > 0:
#     num, remainder = divmod(num, 10)
#     sum += remainder
# print(sum)


# print(divmod(12345, 10))
''' to get all the vowels in a proper order '''
# var = input('Enter a word/sentence:')
# index = 0
# count = 0
# result = ''
# while index < len(var):
#     if var[index].lower() in 'aeiou':
#         result += var[index]
#     else:
#         count += 1
#     index += 1
# print(result)
# print(f'{var} has {count} number of other characters')

''' traversing through a list '''
# company = ['apple', 'google', 'yahoo', 'facebook', 'google', 'apple', 'instagram', 'microsoft', 'amazon', 'uber']
# index = 0
# while index < len(company):
#     print(company[index])
#     index += 1

# ''' even length words only'''
# company = ['apple', 'apple', 'google', 'yahoo', 'facebook', 'google', 'apple', 'instagram', 'microsoft', 'amazon', 'uber']
# index = 0
# while index < len(company):
#     temp = company[index]
#     if len(temp) % 2:
#         company.remove(temp)
#     else:
#         index += 1
# print(company)

''' reverse the string if len is even, else keep as it is '''
# company = ['apple', 'apple', 'google', 'yahoo', 'facebook', 'google', 'apple', 'instagram', 'microsoft', 'amazon', 'uber']
# index = 0
# while index < len(company):
#     temp = company[index]
#     if len(temp) % 2 == 0:
#         company[index] = temp[::-1]
#     else:
#         company[index] += '-odd_len'
#     index += 1
# print(company)

# sample = ['hello', 'hai', 'python']
# index = 0
# while index < len(sample):
#     sample[index] = sample[index][::-1]
#     index += 1
# print(sample)

''' sum of all the number in a list '''
# example1 = [20, 35, 19, 17, 30]
# index = 0
# sum = 0
# while index < len(example1):
#     sum += example1[index]
#     index += 1
# print(sum)

# example2 = [20, 35, 19, 'string', [10, 20,30], 10.78, (10, 10), True]
# index = 0
# sum = 0
# while index < len(example2):
#     temp = example2[index]
#     if isinstance(temp, (int, float)):
#         sum += temp
#     elif isinstance(temp, (list, tuple)):
#         var = 0
#         while var < len(temp):
#             sum += temp[var]
#             var += 1
#     else:
#         print(temp)
#     index += 1
# print(sum)

''' check whether a  number is prime or not '''
num = int(input('Enter a number :'))
divisor = 2
while divisor < num:
    if num % divisor == 0:
        print(f'{divisor} is a divisor of {num}, so its not prime')
        break
    divisor += 1
else:
    print(f'{num} is prime')
# print('hi')

''' reversing a string '''
# s = 'Hello Python'
# index = len(s) - 1
# result = ''
# while index >= 0:
#     result += s[index]  # result = result +  s[index]
#     index -= 1
#     print(result)
# print(result)

# s = 'Hello Python'
# index = 0
# result = ''
# while index < len(s):
#     result = s[index] + result
#     index += 1
# print(result)

''' create a dictionary where elements of list will be its key and len of key as value '''
# company = ['apple', 'google', 'yahoo', 'facebook', 'instagram', 'microsoft', 'amazon', 'uber']
# index = 0
# d = {}
# while index < len(company):
#     temp = company[index]
#     d[temp] = len(temp)
#     index += 1
# print(d)

''' create a dictionary where elements of list will be its key and number of vowels  of key as value '''
# company = ['apple', 'google', 'yahoo', 'facebook', 'instagram', 'microsoft', 'amazon', 'uber']
# index = 0
# d = {}
# while index < len(company):
#     temp = company[index]
#     nes_index = 0
#     count = 0
#     while nes_index < len(temp):
#         char = temp[nes_index]
#         if char.lower() in 'aeiou':
#             count += 1
#         nes_index += 1
#     d[temp] = count
#     index += 1
# print(d)

# s = 'hai@hello@how@are@you@gentlemen'
# res = ''
# count = 0
# for index, item in enumerate(s):
#     if item in '@':
#         count += 1
#         if count % 2 == 0:
#             res += item
#     else:
#         res += item
#
# print(count)
# print(res)








