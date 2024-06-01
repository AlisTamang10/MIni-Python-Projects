
def fibonacci(n):
    
    sequence = [0,1]
    if n <= 0:
        print("Please Enter Positive Value")
    elif n == 1:
        print(sequence[0])
    else:
        for i in range(2,n):
            
            next_sum = sequence[-1] + sequence[-2]
            sequence.append(next_sum)
            
        return sequence


n_term = int(input("Enter the number: "))
fibonac_n = fibonacci(n_term)
print("fibonacci of {}".format(n_term),fibonac_n)

