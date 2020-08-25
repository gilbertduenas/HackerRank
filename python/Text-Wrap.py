# https://www.hackerrank.com/challenges/text-wrap/problem

def wrap(s, m):
  all = []
  chunk =[]
  count = 0
  length = m
  nl = '\n'
  
  for i in range(len(s)):
    chunk.append(s[i])

    if count==length-1:
      all.append(''.join(chunk))
      chunk = []
      count = -1
    elif i==len(s)-1:
      all.append(''.join(chunk))

    count+=1

  return f'{nl.join(all)}'
