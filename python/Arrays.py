# https://www.hackerrank.com/challenges/np-arrays/problemimport numpy

# Create a simple array of floats and reverse it.

def arrays(arr):
    n = numpy.array(arr, float)
    return n[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)