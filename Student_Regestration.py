
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
            
def update_students(id,name = None,age=None,grade=None):
    for student in students:
        if student['id'] == id:
            student['name'] = name
            student['age']   = age 
            student['grade'] = grade
            print("Updated Successfully !!")
            
        if student[id] not in students:
            print("Student not found !")
            
def delete_student(id):
    for student in students:
        if student['id'] == id:
            students.remove(student)
            print(f"Student deleted !!")
    print("student not found !!")
            
            
def main():
    while True:
        print("-------------- Welcome to the ABC College -----------------")
        print("Enter 1 to add student \nEnter 2 to view student \nEnter 3 to update student \nEnter 4 to delete student \nEnter 5 to exit")
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
        elif choice == 3:
            id = int(input("Enter the id: "))
            name = input("Enter the name: ")
            age = int(input("Enter the age: "))
            grade = input("Enter the grade: ")
            update_students(id,name,age,grade)
            
        elif choice == 4:
            id = int(input("Enter id: ")) 
            delete_student(id)
            
        elif choice == 5:
            print("exiting the system")
            break
        else:
            print("invalid input!!")
            
        

if __name__ == "__main__" :
    main()