# https://www.hackerrank.com/challenges/validate-a-roman-number/problem

import re

ones = '(?:(V?(I){0,3})|(IX)|(IV))?'
tens = '(?:(L?(X){0,3})|(XC)|(XL))?'
hundreds = '(?:(D?(C){0,3})|(CM)|(CD))?'

numeral = r'^' + thousands + hundreds + tens + ones + '$'

print(str(bool(re.match(numeral, input()))))
