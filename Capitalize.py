# https://www.hackerrank.com/challenges/capitalize/problem

# Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

def solve(s):
    return string.capwords(s, ' ')
