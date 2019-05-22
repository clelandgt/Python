# -*- coding:utf-8 -*-
from random import randint

__author__ = 'cleland'


# def merger(left, right):
#     i, j = 0, 0
#     result = []
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result += left[i:]
#     result += right[j:]
#     return result

def merger(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left[0])
            del left[0]
        else:
            result.append(right[0])
            del right[0]
    result.extend(left)
    result.extend(right)
    return result


def merger_sort(lists):
    """ 归并算法
    该算法是采用分治的一种非常典型的应用。
    1. 将已有序的子序列合并，并得到完全有序的序列；
    2. 先使命每个子序列有序，再使子序列段间有序。若将两个有序表合成一个有序表，称为二路合并。
    """
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
