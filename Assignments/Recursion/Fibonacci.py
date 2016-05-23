import timeit
from timeit import Timer

def fibs1(number):
    if number <= 1:
        return number
    else:
        return int(fibs1(number-1))+int(fibs1(number-2))


resultlist = {0:0, 1:1}
def fibs2(number):
    if number in resultlist:
        return resultlist[number]

    result = fibs2(number-1) + fibs2(number-2)
    resultlist[number] = result
    return result


def main():

    t1 = Timer(stmt="fibs1(30)", setup="from __main__ import fibs1")
    print ("fibs1:", t1.timeit(number=1), "milliseconds")
    t2 = Timer(stmt="fibs2(30)", setup="from __main__ import fibs2")
    print ("fibs1:", t2.timeit(number=1), "milliseconds")

if __name__ == '__main__':
    main()