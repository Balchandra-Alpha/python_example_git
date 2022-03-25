# z = "zuperman"
# a = "zuperman"
# # print(s.index(s))
# print(a.index(z))
# def joinn(string,joining_char = "-"):
#     op = ""
#    for i in string:
#        op += i
#     return op
# print(joinn("hello"))
# a = 10
# print(a)
# to comment ctrl+/
# print("##############",end = "\t")
# print("****welcome to python***")
# print("end")
# a = 10
# b = 20
# c = 30
# print(a,b,c,sep = "    ")
# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# print("a contains" ,a)
# print("b contains",b)
# print("addition of your 2 numbers is = ",a+b)


# s  = "how"
# a = "hi hello how are you "
# print(a.index(s))
# print(a.index("how"))
# print(type(s))
# print(type("how"))

# o/p:
# 9
# 9
# <class 'str'>
# <class 'str'>

# operations on strings
# concatination
# s = "hai"
# s1 = "hello"
# a = s+s1
# print(a)
# print(s)
# print(s1)
# string multiplication
# print(s*s1) #TypeError: can't multiply sequence by non-int of type 'str'
# print(s*8) #haihaihaihaihaihaihaihai

# string formatting
# * infusing data dynamically into string at the time of execution is called
# formatting
# there are three ways to format strings:
# 1 ) formatting with place  holders
# 2) formatting with .format() method
# 3) formatting with string literals i,e fstrings

# 1 ) formatting with place holders
# * it is the oldest method for string formatting
# * % is used  to hold the place
# * this is also called as string formatting operator
# -> "%s" for injecting strings
#     "%d" for injecting integers
#     "%f" for injecting floats

# name = input("enter your name : ")
# age = int(input("enter your age : "))
# percent = float(input("enter your percent : "))
#
# print(" hello %s , your  age is %d  your percentage %f" % (name, age,percent))


# 2) formatting with .format() method

# *formatting  by calling .format()  method
# * here we'll be using {} as placeholders

# example :
# print(" hello {} , your  age is {}  your percentage {}".format("shivin",22,99.0))
# print(" hello {1} , your  age is {0}  your percentage {2}".format(22,"shivin",99.0))
# print(" hello {name} , your  age is {age}  your percentage {percent}".format( age = 22, percent = 99.0,name = "shivin"))

# 3) formatting with string literals i,e fstrings

# *here we can pass variables from outside directly into the string instead of passing them as
# arguments
# * here we'll be using {var_name} as placeholders

# example:
# name = input("enter your name : ")
# age = int(input("enter your age : "))
# percent = float(input("enter your percent : "))
# print(f"hello {name}, your age is {age}, your percentage is {percent}")

# s = "malayalam"
# print(id(s), "memory location of s")
# for _ in s :
#     print(id(_), "                 " ,"is memory locaion of ",_)












