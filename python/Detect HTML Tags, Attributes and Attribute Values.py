# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem

# Almost the same as this one....
# https://www.hackerrank.com/challenges/html-parser-part-1/problem

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for ele in attrs:
            print('->',ele[0],'>',ele[1])

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for ele in attrs:
            print('->',ele[0],'>',ele[1])

n = int(input())

parse = ''.join([input().strip() for i in range(n)])

parser = MyHTMLParser()
parser.feed(parse)