import timeit
from timeit import Timer

x = list(range(2000000))

def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


def main():

    # Listing 3
    t1 = Timer(stmt="test1()", setup="from __main__ import test1")
    print ("concat ", t1.timeit(number=1000), "milliseconds")

    t2 = Timer(stmt="test2()", setup="from __main__ import test2")
    print ("concat ", t2.timeit(number=1000), "milliseconds")

    t3 = Timer(stmt="test3()", setup="from __main__ import test3")
    print ("concat ", t3.timeit(number=1000), "milliseconds")

    t4 = Timer(stmt="test4()", setup="from __main__ import test4")
    print ("concat ", t4.timeit(number=1000), "milliseconds")

    # Listing 4
    popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
    popend = timeit.Timer("x.pop()", "from __main__ import x")

    print "popzero ", popzero.timeit(number=1000)
    x = list(range(2000000))
    print "popend ", popend.timeit(number=1000)


    # Listing 5
    print ("pop(0) pop()")
    for i in range(1000000,10000001,1000000):
        x = list(range(i))
        pt = popend.timeit(number=1000)
        x = list(range(i))
        pz = popzero.timeit(number=1000)
        print ("%15.5f, %15.5f" %(pz, pt))


if __name__ == "__main__":
    main()


