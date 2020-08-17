# it is no wonder that future AI will be able to program better than humans in the future if all we do is google answers
import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    l = []

    for i in range(size):
        s = '-'.join(alpha[i:size])
        l.append((s[::-1]+s[1:]).center(4*size-3, '-'))

    print('\n'.join(l[:0:-1]+l))
    
