'''
We define super digit of an integer x using the following rules:
Given an integer, we need to find the super digit of the integer. If x has only 1 digit, then its super digit is x. Otherwise, 
the super digit of x is equal to the super digit of the sum of the digits of x.
For example, the super digit of 9875 will be calculated as:
	super_digit(9875)   	9+8+7+5 = 29 
	super_digit(29) 	    2 + 9 = 11
	super_digit(11)		    1 + 1 = 2
	super_digit(2)		    = 2  
-> Example : n = 9875  and k = 4
   The number p is created by concatenating the string nk times so the initial p = 9875987598759875.
    superDigit(p) = superDigit(9875987598759875)
                  9+8+7+5+9+8+7+5+9+8+7+5+9+8+7+5 = 116
    superDigit(p) = superDigit(116)
                  1+1+6 = 8
    superDigit(p) = superDigit(8)
All of the digits of p sum to 116. The digits of 116 sum to 8. 8 is only one digit, so it is the super digit.
-> Function Description: Complete the function superDigit which has parameter(s): string n: a string representation of an integer
   and int k: the times to concatenate n to make p. And function must return the calculated super digit as an integer.
-> Input Format:  The first line contains two space separated integers, n and k.
-> Constraints: 1 <= n < 10 ^ 100000  and  1 <= k <= 10 ^ 5
'''
import math
import os
import random
import re
import sys

# Complete the 'superDigit' function below. The function is expected to return an INTEGER. The function accepts following parameters:
#  1. STRING n  2. INTEGER k
'''
# this will have time out for the long numer and larger k.
def superDigit(n, k):
    s = 0
    num = str(n) * k
    if len(num) == 1:
            return int(num)
    else:
        for i in num:
            s += int(i)
        return superDigit(s, 1)
'''

'''
What is called super digit here, is practically the digital root of a number, which can be implemented recursively, 
or easier using modulo. We derived the digital root function alreay:
dr(n) = 1 + (n - 1 mod 9 ))
This has time complexity of O(log n) and is optimize slution of the problem. 
'''
def superDigit(n, k):
    # Write your code here
    return 1 + (k * sum(int(x) for x in n) - 1) % 9
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
