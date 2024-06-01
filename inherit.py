# class Vehicle:
#     def general_usage(self):
#         print("general use: transportaion")
        

# class Car(Vehicle):
#     def __init__(self):
#         print('I am car')
#         self.wheels = 4
#         self.roof = True
       
#     def specific_usage(self):
#         print("specific use: vacation wid family")

# class Motorcycle(Vehicle):
    
#      def __init__(self):
#         print('I am motorcycle')
#         self.wheels = 4
#         self.roof = True
        
#      def specific_usage(self):
#         print("specific use:to ride")
        
        
# c = Car()
# c.general_usage()
# c.specific_usage()

# m = Motorcycle()
# m.general_usage()
# m.specific_usage()

class Animal:
    
    def __init__(self, habitat):
        self.habitat = habitat
        
    def phabitat(self):
        print(self.habitat)
        
    def sound(self):
        print("some animal my sound")
        
class Dog(Animal):
    
    def __init__(self):
        super().__init__("kennel")
        
    def sound(self):
        print("woof woof")
        
        
dog = Dog()
dog.phabitat()
dog.sound()