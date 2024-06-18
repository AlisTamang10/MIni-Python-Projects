
students =[]

def add_student(id,name,age,grade):
    student = {
        
        'id': id,
        'name': name,
        'age' : age,
        'grade' : grade
    }
    students.append(student)
    print('Student added successfully!!')
    
def view_student():
    if not students:
        print("Students not found !!")
    else:
        for student in students:
            print(f"ID:{student['id']}\nName:{student['name']}\nAge:{student['age']}\nGrade:{student['grade']}")
            
def update_students():
    pass 
    

def main():
    while True:
        print("-------------- Welcome to the ABC College -----------------")
        print("Enter 1 to add student \nEnter 2 to view student")
        choice = int(input("Enter your choice here: "))
        if choice == 1:
            id = int(input("Enter id: "))
            name = input("Enter Name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            add_student(id, name, age, grade)
        elif choice == 2:
            print("----Here is the details of the student -----")
            view_student()
            
        

if __name__ == "__main__" :
    main()