import re

n = int(input())

for i in range(n):
  for color in re.findall('(?<=.)#{1}[0-9A-Fa-f]{3,6}', input()):
    print(color)
