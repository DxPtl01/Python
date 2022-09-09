'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.For example a square matrix is shown below:
1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = 1+5+9 = 15. The right to left diagonal = 3+5+9 = 17. Their absolute difference |15-17| is 2.
-> Function description: Complete the function diagonalDifference(arr) which takes parameter: int arr[n][m]: an array of integers
-> Return int: the absolute diagonal difference
-> Input Format: The first line contains a single integer, n, the number of rows and columns in the square matrix . 
-> Each of the next n lines describes a row, arr[i], and consists of n space-separated integers a[i][j].
-> Constraints: -100 <= a[i][j] <= 100
-> Output Format:Return the absolute difference between the sums of the matrix's two diagonals as a single integer.
-> Sample Input:     Sample Output:
3                       15
11 2 4
4 5 6
10 8 -12

-> Explanation: 
The primary diagonal is: Sum across the primary diagonal: 11 + 5 - 12 = 4
11
   5
     -12

The secondary diagonal is:  Sum across the secondary diagonal: 4 + 5 + 10 = 19 
     4
   5
10

Difference: |4 - 19| = 15
Time Complexity O(n)
'''

import math
import os
import random
import re
import sys

# Complete the 'diagonalDifference' function below.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.

def diagonalDifference(arr):
    Suml = Sumr = 0
    
    for i in range(n):
        Suml = Suml + arr[i][i]
        Sumr = Sumr + arr[i][n-1-i]
        print(arr[i][i], arr[i][n-1-i])
    
    return abs(Suml - Sumr)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
