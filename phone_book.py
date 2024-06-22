
def add_contact(phone_book):
    name = input("Enter the contact name: ")
    phone_number = input("Enter the contact phone number: ")
    phone_book[name] = phone_number
    print(f"Contact {name} added successfully.")

def delete_contact(phone_book):
    name = input("Enter the name of the contact you want to delete: ")
    if name in phone_book:
        del phone_book[name]
        print(f"{name} deleted sucessfully.")
    else:
        print(f"{name} not found.")
        
def update_contact(phone_book):
    name = input("Enter the name you want to update: ")
    if name in phone_book:
        new_number = input("Enter the new number: ")
        phone_book[name] = new_number
        print(f"Contact {name} updated succesfully.")
    else:
        print(f"{name} not found.")
        
def display_contact(phone_book):
    print("Showing Contacts...........")
    for name, number in phone_book.items():
        print(f"{name}--->{number}")
    
    
def main():
    phone_book = {}
    while True:
        print("Enter 1 to add contact\nEnter 2 to view contacts\nEnter 3 to update contact\nEnter 4 to delete contact\nEnter 5 to exit")
        choose = int(input("Enter you choice here: " ))
        if choose ==1:
            add_contact(phone_book)
        elif choose == 2:
            display_contact(phone_book)
        elif choose == 3:
            update_contact(phone_book)
        elif choose == 4:
            delete_contact(phone_book)
        elif choose == 5:
            break
    
main()