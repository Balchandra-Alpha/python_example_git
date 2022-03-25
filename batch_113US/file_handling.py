# f_path = r"C:\Users\HP\PycharmProjects\project_new\Python_FT\abc"
# with open('new_file.txt') as file_obj:
#     print(file_obj)
#     print('inside with block :' , file_obj.closed)
#     print('mode is : ', file_obj.mode)
#     print('file name , :', file_obj.name)
#     print('readable:', file_obj.readable())
#     print('writeble :', file_obj.writable())
# print(file_obj.closed)

# with open('sample.txt', 'r') as f:
#     print(f.readline(30))
#     print()
#     f.seek(0)
#     print(f.read(30))
#     print()
#     f.seek(0)
#     print(f.readlines(125))

''' to count the number of lines in file and printing specified numbe r of lines'''
# with open('sample.txt') as file:
#     count = 0
#     for line in file:
#         if count <= 3:
#             print(line, end='')
#         count += 1
#
#     print(count)
import csv

''' printing each line along with its line number'''
# with open('sample.txt') as file:
#     line_no = 1
#     for line in file:
#         print(line_no, line, end='')
#         line_no += 1

# using enumerate:
# with open('sample.txt') as file:
#     for line_no, line in enumerate(file, start=1):
#         print(line_no, line, sep='- ', end='')


''' count the actual number of lines with valid data in a file'''
# with open('sample.txt') as file:
#     count = 0
#     for line in file:
#         if line.strip():
#             print(line, end='')
#             count += 1
#     print(count)

''' calculate the number of words in a line and print it'''
# with open('sample.txt') as file:
#     total = 0
#     for line in file:
#         count = 0
#         for word in line.split():
#             count += 1
#         print(count , line, end='')
#         total += count
#     print(total)

''' extract ip address from access-log.txt '''
# f_path = r"C:\Users\HP\PycharmProjects\project_new\batch_113US\files\access-log.txt"
# with open(f_path) as file:
#     l = []
#     count = 0
#     no_lines = 0
#     for line in file:
#         if line.strip(): # to remove empty lines
#             temp = line.split()
#             if temp[0] not in l: #to not get duplicate values
#                 l.append(temp[0])
#         else:
#             count += 1
#         no_lines += 1
# print(l)
# print(count, len(l))
# print(no_lines)

''' create a dictionary with ip adress and its count from access-log.txt '''
# with open(f_path) as file:
#     ip = []
#     for line in file:
#         if line.strip():
#             temp = line.split()
#             ip.append(temp[0])
#     d = {}
#     for item in ip:
#         d[item] = ip.count(item)
# print(d)

# with open(f_path) as file:
#     ip = []
#     for line in file:
#         if line.strip():
#             temp = line.split()
#             ip.append(temp[0])
#     d = {}
#     for item in ip:
#         if item not in d:
#             d[item] = 1
#         else:
#             d[item] += 1
# print(d)

# f_path = r"C:\Users\HP\PycharmProjects\project_new\batch_113US\files\football.txt"
# with open(f_path, encoding="UTF-8") as file:
#     d = {}
#     for line_no, line in enumerate(file, start=1):
#         if line_no == 1:
#             continue
#         elif line.strip():
#             temp = line.split()
#             if temp[0] not in d:
#                 d[temp[0]] = [temp[1]]
#             elif temp[1] not in d[temp[0]]:
#                 d[temp[0]].append(temp[1])
# print(d)

# f_path = r"C:\Users\HP\PycharmProjects\project_new\batch_113US\sample.txt"
# with open(f_path) as file:
#     print(file.readline())
#     temp = file.tell()
#     print(file.readline())
#     temp2 = file.tell()
#     print(file.readline())
#     file.seek(temp)
#     print(file.readline())
#     file.seek(0)
#     print(file.readline())
#     file.seek(temp2)
#     print(file.readline())

# f_path = r"C:\Users\HP\PycharmProjects\project_new\batch_113US\sample.txt"
# with open('Example.txt', "a") as file:
#     file.writelines(['This is not morning', '\n\n\nthis is evening(to 2nd line)', '\npython class'])

''' copying a file to another file'''
# f_path = r"C:\Users\HP\PycharmProjects\project_new\batch_113US\sample.txt"
# with open(f_path, 'r') as r_file:
#     with open('Example.txt', 'w') as w_file:
#         for line in r_file:
#             w_file.write(line)

# import csv
#
# f_path = r"C:\Users\HP\PycharmProjects\project_new\batch_113US\files\sample.csv"
#
# with open(f_path, 'r') as file:
#     f = csv.reader(file)
#     for line in f:
#         print(line[0], line[1])
#
# with open(f_path, 'r') as file:
#     f = csv.DictReader(file)
#     for line in f:
#         print(line)


''' print all the details if quantity of shares is more than 50 '''
# f_path = r"C:\Users\HP\PycharmProjects\project_new\batch_113US\files\test.csv"
# with open(f_path , 'r') as file:
#     rows = csv.reader(file)
#     for line_no, line in enumerate(rows, 1):
#         if line_no > 1:
#             if int(line[1]) > 50:
#                 print(line)

# import csv
# with open('n_file.csv', 'w') as file:
#     obj = csv.writer(file)
#     obj.writerow(['name', 'company', 'salary'])
#     obj.writerows([('jack', 'apple', '70000'), ('john', 'apple', '70000'), ('jill', 'microsoft', '80000')])
#     while True:
#         name = input('Enter name :')
#         company = input('Enter company: ')
#         salary = input('Enter salary : ')
#         obj.writerow([name, company, salary])
#         value = input('Enter 1 to add more data and 2 to exit : ')
#         if value == '2':
#             break

# import csv
# with open('n_file.csv', 'w') as file:
#     obj = csv.DictWriter(file, ['name', 'salary', 'company'])
#     obj.writeheader()
#     obj.writerow({'name': 'john', 'salary': '70000', 'company':'facebook'})
#     obj.writerows([{'salary': '75000','name': 'jack', 'company':'facebook'}, {'name': 'mike', 'salary': '70000', 'company':'facebook'}])


# from practice import num, my_sum
# print(num)
# print(my_sum(10, 20))
#
# from my_reference.file1 import var, square
# print(var)
# print(square(4))

# from csv import reader
# with open('n_file.csv') as file:
#     f = reader(file)
#     for line in f:
#         print(line)










