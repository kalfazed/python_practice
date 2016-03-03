import re
import sys

__author__ = 'monkey'

def countWords():
    # open file
    inputFile = sys.argv[1]
    with open(inputFile, 'r') as file:
        data = file.read()

    words = re.compile(r'([a-zA-Z]+)')

    # calculate the appear times of each words
    dic = {}
    for i in words.findall(data):
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    # save the items of dic to numlist
    numlist = []
    for k,value in dic.items():
        numlist.append((k, value))

    # sort
    numlist.sort(key = lambda  t:t[0])

    # output
    for i in numlist:
        print(i[0], i[1])

if __name__ == '__main__':
    countWords()
