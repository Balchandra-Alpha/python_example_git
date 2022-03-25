# class Sample:
#     a = 10
#     b = 20
#
#     def display(self):
#         print('In display')
#
#
# obj = Sample()
# obj.a = 'hello'
# # print(obj.a)
# # Sample.a = 'hai'
# # print(Sample.a, obj.a)
# print(Sample.__dict__)
# print(obj.__dict__)


# class Calculator:
#     a = 'hello'
#     b = 'hai'
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         print(self.a + self.b)
#
#     def sub(self):
#         print(self.a - self.b)
#
#     def div(self):
#         print(self.a / self.b)
#
#     def mul(self):
#         print(self.a * self.b)
#
# calci1 = Calculator()
# calci1.add()
# calci1.sub()
# calci1.mul()
# calci1.div()
# print(Calculator.__dict__)
# print(calci1.__dict__)

# class Sample:
#     a = 10
#     b = 'hello'
#     x = 15
#
#     @staticmethod
#     def display():
#         print('in display')
#
#
#
# m = Sample()
# m.display()
# print(Sample.__dict__)
# print(m.__dict__)

# class CheifMinister:
#     current_cm = 'Bommai'
#
#     def display(self):
#         print(f'current cm is :{self.current_cm}')
#
#     @classmethod
#     def replacement(cls, votes):
#         if votes > 51:
#             cls.current_cm = 'Balchandra'
#
# people = CheifMinister()
# bjp = CheifMinister()
# opp = CheifMinister()
#
# bjp.display()
# bjp.replacement(55)
# bjp.display()
# opp.display()
# people.display()

# class spam():
#
#     def display(self):
#         print('in display')
#
#     def __init__(self, func):
#         self.f = func
#
#     def __call__(self, *args, **kwargs):
#         print('In call ')
#         self.f(*args, **kwargs)
#
#
# @spam # add = spam(add)
# def add(a, b):
#     print('In add')
#     print(a + b)
#
# add(10, 20)

class spam():

    def display(self):
        print('in display')

    def __init__(self, n):
        self.n = n

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('In call ')
            for i in range(self.n):
                func(*args, **kwargs)
        return wrapper

# obj = spam()
@spam(3) # add = obj(add)
def add(a, b):
    print('In add')
    print(a + b)

add(10, 20)













