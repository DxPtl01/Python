'''
Given an array of n integers, where all elements but one occur twice, find the unique element.
-> Example: a[1,2,3,4,3,2,1] , The unique element is 4.
-> Function Description: Complete the lonelyinteger function which has the following parameter(s):int a[n]: an array of integers
   Returns int: the element that occurs only once
-> Input Format: The first line contains a single integer, n , the number of integers in the array. The second line contains  space-separated 
   integers that describe the values in .
-> Constraints: 1 <= n <100
                It is guaranteed that  is an odd number and that there is one unique element.
                0 <= a[i] <= 100, where 0 <= i < n.
-> Time complexity is O(N);
-> space complexity is O(1)
-> Execution: XORing two equal numbers cancels them out. XOR all numbers together.
'''
import math
import os
import random
import re
import sys

def lonelyinteger(a):
    # Write your code here
    ans = a[0]
    for i in range(1, n): # time complexity O(n)
        ans ^= a[i]  
    return ans

def lonelyinteger1(a): # time complexity O(n)
    fArry = [0] * n
    for i in a:
        fArry [i] = fArry [i] + 1
    for i in range(n):
        if fArry[i] == 1:
            return i
    
if __name__ == '__main__':
    
    print("Enter lenght of elemnet: ")
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger1(a)
    print("The Loniest Integer of list is: ", result)
