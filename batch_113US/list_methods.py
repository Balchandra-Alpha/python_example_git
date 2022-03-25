# company = ['apple', 'microsoft', 'tesla']
# print(company, len(company))
# company.extend(['hello', 'hai'])
# print(company, len(company))
# company.append('flipkart')
# print(company, len(company))
# company.insert(4, 'amazon')
# print(company, len(company))

# company = ['apple', 'microsoft','hello', 'tesla', 'hello', 'amazon', 'hai', 'flipkart']
# var = company.pop()
# print(company, var)

# num = [1, 2, 4, 5, 6, 7]
# num.append(8)
# print(num)
# num.insert(2, 3)
# print(num)
# a = {9, 10, 11}
# num.extend(a)
# print(num)

# num = [1, 2, 3, 4, 3, 4, 2, 3, 2, 1]
# print(num.count(2))
# num.remove(4)
# print(num)
# num.pop()
# print(num)
# a = num.pop(-3)
# print(num, a)
# b = num.pop(2)
# print(num, b)

# num = [1, 2, 3, 4, 3, 4, 2, 3, 2, 1]
# company = ['apple', 'microsoft','hello', 1, 4, 5.66, [10, 20], {2, 3, 4}, '99']
# company.pop()
# print(company)
# company.remove('hello')
# print(company)
# num.clear()
# print(company.clear())
# print(num, bool(num), company, bool(company))

# del company[2: 5]
# print(company)

# company = ['apple', 'microsoft','hello', 1, 4, 5.66, [10, 20], {2, 3, 4}, '99']
# print(company.reverse())
# print(company)
# print(company[2:5])

# a = [1, 2, 3, 4]
# b = a.copy()
# print(id(a), id(b))
# a.append(5)
# print(id(a), id(b))

# a = [1, 2, 3,[10, 20, 30], 4]
# b = a.copy()
# print(id(a), id(b))
# a[3].append(5)
# b[3].insert(2, 'hai')
# print(a, b)

# from copy import deepcopy
# a = [1, 2, 3,[10, 20, 30], 4]
# b = a.copy()
# c = deepcopy(a)
# print(id(a), id(b))
# a[3].append(5)
# a.append(5)
# b[3].insert(2, 'hai')
# c[3].extend([40, 50])
# print(a, b, c, sep='\n')

# num = [1, 2, 3, 4, 3, 4, 2, 3, 2, 1]
# company = ['apple', 'microsoft','hello', 1, 4, 5.66, [10, 20], {2, 3, 4}, '99']
# cars = ['toyota', 'Tesla', 'BmW', 'Benz', 'audi', '1', '2']
# print(num.sort(reverse=True))
# print(num)
# print(ord('A'), ord('Z'), ord('a'), ord('z'))
# cars.sort(key=len, reverse=True)
# print(cars)
# company.sort()
# print(company)
# cars.sort(reverse=True)
# print(cars)
#   0   1  2      3        4        5     6        7
# t = (1, 2, 4, 'hai', [1, 2, 3], 3, 'hai',{1, 2, 3})
# print(type(t))
# # t[3] = 'hello'
# print(t[2:5])
# a, b, c = (1, 2, 3)  #unpacking
# print(a, b, c)
# m = 'hai', 5, 8.9, True  #packing
# print(m, type(m), len(m))
# print(t.index(3))
# print(t.count('Hai'))