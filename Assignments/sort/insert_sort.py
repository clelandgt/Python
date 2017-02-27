# -*- coding:utf-8 -*-
__author__ = 'cleland'


def insert_sort(l):
    """ 插入排序
    从左到右是从小到大
    伪代码：
        for i in [1, n)
            for j in [0, i):
                if a[i] <= a[j]:
                    swap(a[i], a[j])
    """
    for i in xrange(1, len(l)):
        for j in xrange(0, i):
            if l[i] <= l[j]:
                l[i], l[j] = l[j], l[i]


def main():
    l1 = [5, 2, 4, 6, 1, 3]
    print 'before sort: ', l1
    insert_sort(l1)
    print 'after sort: ', l1


if __name__ == '__main__':
    main()
