# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    max_height = 0

    for i in range(len(word)):
        if(h[ord(word[i])-97] > max_height):
            max_height = h[ord(word[i])-97]

    return len(word) * max_height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
