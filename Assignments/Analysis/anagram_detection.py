import time


# Soluton 1: Check Off
def anagramSolution1(s1, s2):
    alist = list(s2)
    still_ok = True
    pos1 = 0

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(s2) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            still_ok = False
        pos1 = pos1 + 1

    return still_ok


# Solution 2: Sort and compare
# First Sort two list
# Then compare two list whether be equaled.
def anagramSolution2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches


#Solution 3: Brute Force
def anagramSolution3(s1, s2):
    still_ok = True
    pos1 = 0

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(s2) and not found:
            if s1[pos1] == s2[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            pass
        else:
            still_ok = False
        pos1 = pos1 + 1

    return still_ok


#Solution 4: Count and Compare
def anagramSolution4(s1, s2):

    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i])  - ord('a')
        c1[pos] = c1[pos] +1

    for i in range(len(s2)):
        pos = ord(s2[i])  - ord('a')
        c2[pos] = c2[pos] +1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok =  False

    return still_ok


def main():

    s1 = "abcd" * 2000
    s2 = "dcba" * 2000
    start_time = time.time()
    print "anagramSolution1 function execute time:"
    print(anagramSolution1(s1, s2))
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    print "anagramSolution2 function execute time:"
    print(anagramSolution2(s1, s2))
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    print "anagramSolution3 function execute time:"
    print(anagramSolution3(s1, s2))
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    print "anagramSolution4 function execute time:"
    print(anagramSolution4(s1, s2))
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
