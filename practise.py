# # # # lis = list(('a','b','c',1))

# # # # # for i in lis:
# # # # #     print(lis[-3:-1]) # access 

# # # # #membership operator 

# # # # # if 'e' not in lis:
# # # # #     print("No")

# # # # #change b to 

# # # # lis.insert(1,'f')
# # # # lis.append(2)
# # # # # lis.clear()

# # # # # for i in range(len(lis)):
# # # # #     print(lis[i])
# # # # lis.reverse()

# # # # i = 0
# # # # while i < len(lis):
# # # #     print(i,lis[i])
    
# # # #     i = i+1

# # # tup = tuple(("apple",'banana','abc'))

# # # add = ("afaf",)
# # # # x = list(tup)
# # # # x.insert(2,"aoda")
# # # # tup = tuple(x)
# # # tup = tup + add
# # # i = 0

# # # while i < len(tup):
# # #     print(i,tup[i])
# # #     i +=1

# # # sets = {'a','b','dc','e'}
# # # sets.add('ef')
# # # x = [1,2,3]
# # # sets.update(x)
# # # sets.remove('ef')
# # # print(sets)

# # dicti = {
# #     'name':'Alis',
# #     'age': 18,
# #     'job':'Devloper'    
# # }
# # # print(dicti.keys())
# # # print(dicti.values())
# # # print(dicti.items())

# # dicti['height'] = 5.6

# # # print(dicti.keys())
# # # print(dicti.values())
# # # print(dicti.items())

# # for i in dicti.values():
# #     print(i)


# child1 = {
#     'name': 1,
#     'year': 1
# }
# child2 = {
#     'name': 2,
#     'year': 2
# }
# child3 = {
#     'name': 3,
#     'year': 3
# }

# myfamily = {
#     'child1':child1,
#     'child2' :child2,
#     'child3': child3
# }
# print(myfamily.items())
# Write a program in Python to check if a number is prime.

# is_prime = False
# n = int(input("enter the number: "))
# if n == 1:
#     print(n, "is not prime")
    
# elif n > 1:
#     for i in range(2, n):
#         if (n % i )== 0:
#             is_prime = True
#             break
        
        
#     if is_prime:
#         print(n, "is not prime")
#     else:
#         print(n, "is prime")
# class Dog:

# 	# class attribute
# 	attr1 = "mammal"

# 	# Instance attribute
# 	def __init__(self, name):
# 		self.name = name

# Driver code
# Object instantiation
# Rodger = Dog("Rodger")
# Tommy = Dog("Tommy")

# # Accessing class attributes
# print("Rodger is a {}".format(Rodger.attr1))
# print("Tommy is also a {}".format(Tommy.attr1))

# # Accessing instance attributes
# print("My name is {}".format(Rodger.name))
# print("My name is {}".format(Tommy.name))

# Python code to demonstrate how parent constructors
# are called.

# parent class
# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"


# 
# class A:
# 	def __init__(self, n):
# 		self.name = n

# class B(A):
#     def __init__(self, n, roll):
#         self.roll = roll
#         A.__init__ (self, n)
     
# object1 = A('n')
# object = B('n',23)
# print(object1.name)

# parent class
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
	    print(self.name, self.age)

# child class
class Student(Person):
    def __init__(self, name, age):
        self.sName = name
        self.sAge = age
        super().__init__("Rahul", age)

    def displayInfo(self):
	    print(self.sName, self.sAge)

obj = Student("Mayank", 23)
obj.display()
obj.displayInfo()

#jobsnepal.com #scrap #regex #urllib
