# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

import re

alpha = '[qwrtypsdfghjklzxcvbnm]'

a = re.findall('(?<=' + alpha +')([aeiou]{2,})' + alpha, input(), re.I)

print('\n'.join(a or ['-1']))

