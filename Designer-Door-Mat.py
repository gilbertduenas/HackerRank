n, m = map(int, input().split(' '))

for i in range(n):
    haha = '.|.'

    if i < (n-1)/2:
        print((haha * (2*i+1)).center(m, '-'))

    elif i == (n-1)/2:
        print('WELCOME'.center(m, '-'))

    else:
        print((haha * (2*(n-1-i)+1)).center(m, '-'))
