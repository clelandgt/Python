# -*- coding: utf-8 -*-
__author__ = 'cleland'


def bubble_sort(l):
    """ 冒泡排序
    序列顺序从左到右是从小到大，伪代码：
    for i in [0, n)
        for j in [n-1, i) #逆序 
            if a[j] > a[j-1]
                swap(a[j], a[j-1])
    """
    for i in xrange(len(l)):
        for j in range(i+1, len(l))[::-1]:
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]


def main():
    s
    print 'before sort: ', l1
    bubble_sort(l1)
    print 'after sort: ', l1


if __name__ == '__main__':
    main()
 