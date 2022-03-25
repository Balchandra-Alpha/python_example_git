# from copy import deepcopy
# a = [1, 2, [2, 3, 4], 5]
# b = deepcopy(a)
# c = a.copy()
# print(id(a[2]), id(c[2]), id(b[2]), sep="\t")

###########################

# s = {1, 2, 3, 4, 3}
# print(s)
# print(set([1, 2, 3, 2, 1, 4, 6, 4, 4 , 4]))
# a = set([1, 1, 2, 2, ['a', 'b', 'c']])
# print(type(a), a, bool(a), len(a), sep='\t')
# s = 'hello'
# l = [1, 2, 3, 4]
# random = {'a', 'b', 'hello', {1, 2, 3}, (1, 2, 3), 90, 78.98}
# print(random)

# s1 = {1, 2, 3, 4, 5}
# s2 = {1, 2, 4, 6, 8}
# s3 = {1, 3, 5, 7, 9}

# print(s1.union(s2, s3, {10, 20, 30}))
# print(s1, s2, s3)

# print(s1.union(s2))
# print(s1.update(s2))
# print(s1, s2, s3)

# m = s1.intersection(s2, s3, {1, 2, 3})
# print(s1, s2, m, sep='\t')
# # print(id(s1), id(m))


# m = s1.intersection_update(s2, s3, {1, 2, 3})
# print(s1, m, sep='\t')
# # print(id(s1), id(m))
# print(s1)
#
# s1 = {1, 2, 3, 4, 5}
# s2 = {1, 2, 4, 6, 8}
# s3 = {1, 3, 5, 7, 9}
#
# m = s1.difference(s2, s3)
# n = s2.difference(s1, s3)
# print(m, n, s1, s2, sep='\t')

# m = s1.difference_update(s2) #s1 = {3, 5}
# n = s2.difference_update(s1, s3)
# print( s1, s2, sep='\t')

# s = {'hi',2,'hello',2.0}
# print(s.pop())
# print(s)

# a = 10
# s = {10, 20, 30}
# d = {"hi": 10, "hello" :20 , 30: "world"}
# print(d["hi"]) # 10
# print(d[40])  # key error
# print(d.get("hi", "key not found")) # 10
# print(d.get("python", "key not found")) # key not found
# print(d.get("python"))  # none



































