
# l = range(1,20)
# i = 0
# while i<=len(l)-1:
#     if i%2 == 0:
#         print(i, l[i], sep="-", end=",")
#     else:
#         print(i, l[i], sep="-", end=",")
#     i = i+1

# n = 16
# if n % 2 == 0:
#     print(n)
# else:
#     print(n)

# l = range(1,20)
# i = 0
# while i<=len(l)-1:
#     print(i, l[i], sep="-", end=",")
#     i = i+1

# l = [(1,2), (3,4), (5,6), (7,8)]
# p = []
# for i in l:
#     p.append(str(i))
# print(p)

# l = ["hi", "we", "fg", "we", "we", "hi", "we"]
# print(max(l))

# names =["python", "php", "java", "perl"]
# # b = [(n,len(n)) for n in names]
# # print(b)
#
# l = names[3:]+names[:3]
# print(l)

# a = [10,12,14,16,18]
# b = [20,22,24,26,28]

# n = [1, 2, 3, 4, 0, 4, 3, 2, 4, 3, 2, 1, 0, 4]
# for i in n:
#     if i==max(n):
#         print(i)


# names =["python", "php", "java", "perl"]
# for i in range(3):
#     for j in range(len(names)-1, 0, -1):
#         names[j] = names[j-1]
# print(names)


num = 20

def my_sum(a, b):
    return a + b