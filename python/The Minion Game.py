# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(s):
    v = 'AEIOU'
    kev = 0
    stu = 0

    for i in range(len(s)):
        if s[i] in v:
            kev += (len(s)-i)
        else:
            stu += (len(s)-i)

    if kev > stu:
        print('Kevin', kev)
    elif kev < stu:
        print('Stuart', stu)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
    