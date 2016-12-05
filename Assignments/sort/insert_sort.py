# -*- coding:utf-8 -*-


def insert_sort(l):
    for i in range(1, len(l)):
        curr = l[i]
        j = i - 1
        while j >= 0 and l[j] > curr:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = curr
    return l


def main():
    l = [5, 2, 4, 6, 1, 3]
    print 'before sort: ', l
    insert_sort(l)
    print 'after sort: ', l


if __name__ == '__main__':
    main()