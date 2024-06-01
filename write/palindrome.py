 
number = int(input("Enter the number you want: "))
original_number = number
reverse = 0

while number > 0:
    
    last_digitnum = number % 10
    reverse = reverse * 10 + last_digitnum
    number = number // 10 
    
if original_number == reverse:
    print("number is palindrome ")
    
else:
    print("not palindrome")



