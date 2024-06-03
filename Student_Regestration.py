print("-------------- Welcome to the ABC College -----------------")

Name = []
Age = []
Phone_Number = []
Plus2_faculty = []

nam = input("Enter your name: ")
ag = int(input("Enter your age: "))
ph = int(input("Enter your phone number: "))
faculty = input("Enter your plus 2 faculty: ")


def add():   
    Name.append(nam)
    Age.append(ag)
    Phone_Number.append(ph)
    Plus2_faculty.append(faculty)
 
def display():
    
    for i in range(len(Name)):
        print("-------------- Details ----------")
        print("Name | Age | Phone Number | Faculty ")
        print(Name[i],  "|", Age[i], "|", Phone_Number[i],"|" ,Plus2_faculty[i])
        
add()
display()