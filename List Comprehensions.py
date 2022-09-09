
'''
Let's learn about list comprehensions! You are given three integers X,Y and N representing the dimensions of a cuboid along
with an integer N. You have to print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is
not equal to N.
'''

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    print [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if((i+j+k)!=n)]
