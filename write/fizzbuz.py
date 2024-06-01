#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    result = []
    for i in range(1,n+1):
        
        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')
            
        elif i % 3 == 0:
            result.append('Fizz')
            
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(i))
    
    for i in result:
        print(i)
        
    

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)

