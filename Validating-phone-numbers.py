import re

n = int(input())
valid_start = '^[789]'

for i in range(n):
    number = input()
    valid_length = len(number)
    if valid_length == 10:
        check = re.findall(valid_start, number)
        if check and number.isdigit():
            print('YES')

        else:
            print('NO')

    else:
        print('NO')
