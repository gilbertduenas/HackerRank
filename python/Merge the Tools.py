# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(s, k):
    t = []
    count = 0

    for i in s:
        count += 1
        if i not in t:
            t.append(i)
        if count == k:
            print(''.join(t))
            t = []
            count = 0

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    