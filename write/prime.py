
n = int(input("ENter the number: "))
k = 0
if n == 1:
    print('not prime')
    
elif n > 1:
    for i in range ( 2, n):
        if n % i == 0:
            k = 1
            
    if k == 1: 
        print('not prime')
    else:
        print('prime')
    