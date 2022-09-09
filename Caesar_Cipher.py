'''
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a 
number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the 
case of a rotation by 3, w, x, y and z would map to z, a, b and c.
Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
-> Example: s = There's-a-starman-waiting-in-the-sky  and  k = 3
   The alphabet is rotated by 3, matching the mapping above, The encrypted string is: Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb
-> Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.
-> Function Description: Complete the caesarCipher which has parameter(s): string s: cleartext and int k: the alphabet shift 
factor and Returns string: the encrypted string
-> Input Format: The first line contains the integer, n, the length of the unencrypted string. The second line contains the 
unencrypted string, s. The third line contains k, the number of letters to rotate the alphabet by.
-> Constraints: 1 <= n <= 100,  0 <= k <=100 and s is a valid ASCII string without any spaces.
-> Sample Input:          Sample Output: 
11                          okffng-Qwvb
middle-Outz
2
-> Explanation: Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +2:    cdefghijklmnopqrstuvwxyzab
m -> o
i -> k
d -> f
d -> f
l -> n
e -> g
-    -
O -> Q
u -> w
t -> v
z -> b
'''

import math
import os
import random
import re
import sys

# Complete the 'caesarCipher' function below. The function is expected to return a STRING.
# The function accepts following parameters: 1. STRING s  2. INTEGER k

def caesarCipher(s, k):
    # Write your code here
    res = ''
    for c in s:
        if c.isupper():
            res += chr((ord(s) + k - 65) % 26 + 65)
        elif c.islower():
            res += chr((ord(s) + k - 97) % 26 + 97)
        else: 
            res = res + c
    return res
           
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input().strip())
 
    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    #fptr.write(result + '\n')

    #fptr.close()

    print(result)
