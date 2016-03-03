import re

__author__ = 'kalfazed'

def getFac(var):
    fac = 1
    for i in range(1,var+1):
        fac*= i
    return fac


def printList():
    factorial = {}
    for i in range(1,10):
        #        factorial[i] = getFac(i);
        print "Factorial of %d is %7d"%(i, getFac(i))


if __name__ == '__main__':
    printList()
