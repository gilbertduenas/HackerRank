# https://www.hackerrank.com/challenges/validate-a-roman-number/problem

ones = '(?:(V?(I){0,3})|(IX)|(IV))?'
tens = '(?:(L?(X){0,3})|(XC)|(XL))?'
hundreds = '(?:(D?(C){0,3})|(CM)|(CD))?'

regex_pattern = r'^' + thousands + hundreds + tens + ones + '$'

import re
print(str(bool(re.match(regex_pattern, input()))))
