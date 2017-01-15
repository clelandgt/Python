# -*- coding: utf-8 -*-
__author__ = 'cleland'


def quick_sort(lists, left, right):
	# 快速排序
	if left >= right:
		return lists
	keys = lists[left]
	low = left
	high = right
	while left < right:
		while left < right and lists[right] >= key:
			right -= 1
		lists[left] = lists[right]
		while left < right and lists[left] <= key:
			left += 1
		lists[right] = lists[left]
	lists[right] = key
	quick_sort(lists, low, left-1)
	quick_sort(lists, left+1, high)
	return lists

if __name__ == '__main__':
	l = [2, 1, 10, 3, 8, 9]
	print l
	print 'after sort \n'
	quick_sort(l, 0, len(l))
	print l
