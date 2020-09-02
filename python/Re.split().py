# https://www.hackerrank.com/challenges/re-split/problem

regex_pattern = r"[.,]+"	# Just added [.,]+

import re
print("\n".join(re.split(regex_pattern, input())))