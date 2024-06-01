# def is_leap(year):
#     leap = False
    
#     if year % 400 == 0 and year % 100 == 0:
#         leap = True
#         return leap
#     elif year % 4 == 0 and year % 100 != 0:
        
#         leap = True
#         return leap
    
#     else:
#         leap = False
#         return leap

# year = int(input())
# print(is_leap(year))
#Hello Ross Taylor! You just delved into python.
def print_full_name(first, last):
    # Write your code here
    
    print(f'Hello {first} {last}! You just delved into python.')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)