def kangaroo(x1, v1, x2, v2):
    if (x1<x2 and v1<v2) or (x1>x2 and v1>v2):
        return 'NO'
    
    for i in range(5000):
        x1 += v1
        x2 += v2

        if x1 == x2:
            return 'YES'

    return 'NO'
