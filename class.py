# class Human:
#     def __init__(self,name,occupation):
#         self.name = name 
#         self.occupation = occupation
        
#     def do_work(self):
#         if self.occupation == 'tennis':
#             print(self.name, 'play tennis')
#         elif self.occupation == 'actors':
#             print(self.name, 'shoots movie')
            
#     def speak(self):
#         print(self.name, "says how are you")
    
        
# tom = Human('Tom ','actors')
# tom.do_work()
# tom.speak()

# marie = Human('Maria','tennis')
# marie.do_work()
# marie.speak()

#Create a simple class and demonstrate encapsulation, inheritance, and polymorphism.

class Person:
    
    def __init__(self,name, age):
        self.name = name 
        self.age = age 
        
    def display(self):
        print("Every person has thier own occupation: ")
        
class Teacher(Person):
    def __init__(self,name,age,salary):
        self.__salary = salary 
        super().__init__(name,age)
        
    def get_salary(self):
        print(f'My salary is{self.__salary}') 
    
    def display(self):
        print("My name is",self.name,'and Im',self.age,'old')
        
        
teach = Teacher(name ='Alis',age = 21,salary= 20000)
teach.display()
teach.get_salary()

person = Person('Alis',20)
person.display()