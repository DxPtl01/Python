'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly (n-1) of the n integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
-> Example: arr[1,2,3,4,5].The minimum sum is 1+2+3+4 and the maximum sum is 2+3+4+5. The function prints: 16 24
-> Function Description: Complete the miniMaxSum function in the editor below. miniMaxSum has parameter arr: an array of n integers.
-> Print: Print two space-separated integers on one line: the minimum sum and the maximum sum of (n-1) of n elements.
-> Input Format: A single line of n space-separated integers. 
-> Constraints: 1 <= arr[i] <= 10^9
-> Output Format: Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly n-1 of the n integers. (The output can be greater than a 32 bit integer.)
    Sample Input      Sample Output
    1 2 3 4 5          10 14
-> Explanation: The numbers are 1,2 ,3 ,4 and 5. Calculate the following sums using four of the five integers:
Sum everything except 1, the sum is 14.
Sum everything except 2, the sum is 13.
Sum everything except 3, the sum is 12.
Sum everything except 4, the sum is 11.
Sum everything except 5, the sum is 10.
Hints: Beware of integer overflow! Use 64-bit Integer.
'''
import math
import os
import random
import re
import sys
from functools import reduce


# Complete the 'miniMaxSum' function below.
# The function accepts INTEGER_ARRAY arr as parameter.


def miniMaxSum(arr):
    # Write your code here
    print(arr)
    n = len(arr)
    ans = []
    for i in range(n):
        nArr = arr[:]
        nArr.pop(i)
        ans.append(reduce(lambda x, y: x + y, nArr))
    print(min(ans), end=" ")
    print(max(ans)) 
        
if __name__ == '__main__':
    print("enter element for list: ")
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr) 

