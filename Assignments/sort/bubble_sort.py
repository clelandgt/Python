# -*- encoding: utf-8 -*-
def bubble_sort(l):
    for i in range(len(l)):
        for j in range(0, len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]


def main():
    l = [5, 2, 4, 6, 1, 3]
    print 'before sort: ', l
    bubble_sort(l)
    print 'after sort: ', l


if __name__ == '__main__':
    main()
