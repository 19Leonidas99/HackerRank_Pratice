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
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            #print(i, i% 3, i % 5)
            print('FizzBuzz')
        
        elif i % 3 == 0 and i % 5 != 0:
            #print(i, i % 3, i % 5)
            print('Fizz')
            
        elif i % 3 != 0 and i % 5 == 0:
            #print(i, i % 3, i % 5)
            print('Buzz')
            
        else:
            #print(i, i % 3, i % 5)
            print(i)
        

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
