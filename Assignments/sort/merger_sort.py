# -*- coding:utf-8 -*-
from random import randint

__author__ = 'cleland'


def merger(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merger_sort(lists):
    # 归并排序
    if len(lists) <= 1:
        return lists
    num = len(lists) / 2
    left = merger_sort(lists[:num])
    right = merger_sort(lists[num:])
    return merger(left, right)


def main():
    lists = [randint(1, 10) for i in xrange(10)]
    print lists
    print 'after sort\n'
    lists = merger_sort(lists)
    print lists


if __name__ == '__main__':
    main()
