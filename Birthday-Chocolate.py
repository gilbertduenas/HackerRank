def birthday(s, d, m, n):
    i = j = 0
    total = 0

    if m > n:
        return 0

    while j < m:
        total += s[j]
        j += 1

    if total == d:
      count = 1 

    else:
      count = 0

    while j < n:
        total -= s[i]
        total += s[j]

        if total == d:
            count += 1

        i += 1
        j += 1
        
    return count
