# -*- coding: utf-8 -*-
import inspect
import time

def foo(tom):
    fred = 0
    for bill in range(1, tom+1):
        barney = bill
        fred  = fred + barney
    return fred


def sumOfN(n):
    theSum = 0
    for i in range(1, n+1):
        theSum = theSum + i
    return theSum


def sumOfN2(n):
    theSum = 0
    for i in range(1, n+1):
        theSum = theSum + i

    return theSum


def sumOfN3(n):
    return (n*(n+1)/2)


def main():
    start_time = time.time()

    print "sumOfN function execute time:"
    print(sumOfN(10))
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    print "foo function execute time:"
    print(foo(10))
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    print "sumOfN2 function execute time："
    print sumOfN2(100)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    print "sumOfN3 function execute time："
    print sumOfN3(100)
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
