# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
def average(array):
  a_set = set(array)
  n = len(a_set)
  
  return sum(a_set)/n
