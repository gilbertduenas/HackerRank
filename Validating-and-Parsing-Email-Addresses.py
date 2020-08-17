import re

n = int(input())
valid = '<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>'

for i in range(n):
    name, email = input().split(' ')

    if re.match(valid, email):
        print(f'{name} {email}')
