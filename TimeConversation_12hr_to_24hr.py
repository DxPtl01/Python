'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time. Note: - 12:00:00AM on a 12-hour clock is 00:00:00 
on a 24-hour clock. - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
-> Example: s = "12:01:00PM" then Return '12:01:00'. s = "12:01:00AM" then Return '00:01:00'.
-> Function Description: Complete the timeConversion function in the editor below. It should return a new string representing the
   input time in 24 hour format. timeConversion has parameter string s: a time in 12-hr format which Returns string: in 24-hr format
-> Input Format: A single string  that represents a time in 12-hr clock format (i.e.:hh:mm:ss(A/P)M ).
-> Constraints: All input times are valid
Sample Input      Sample Output
07:05:45PM          19:05:45
'''

import math
import os
import random
import re
import sys
from datetime import datetime

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[:2] == '12' and s[-2] == 'A':
        return "00" + s[2:-2]
    if s[:2] != '12' and s[-2] == 'P':
        h = str(int(s[:2])+12)
        return h + s[2:-2]
    else:
        return s[0:-2]
if __name__ == '__main__':
    s = 0
    while s != 'y':
        print("Enter string time in 12-hr format hh:mm:ss(A/P)M and y to exit: ")
        s = input()
        if s == 'y':
            break
        else:
            ans = timeConversion(s)
            print("string in time 24-hr format: ", ans)

