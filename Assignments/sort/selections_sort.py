# -*- encoding: utf-8 -*-
__author__ = 'cleland'


def selections_sort(l):
	''' 选择排序
	1. 从左到右遍历找到最大/最小的元素与第一个元素交换
	2. 从剩余的元素继续遍历找到最大/最小的元素与第二个元素交换
	3. 依次类推，直到所有元素排序完毕
	'''
	for i in range(len(l)):
		min_index = i
		for j in range(i+1, len(l)):
			min_num = l[min_index]
			if l[j] < min_num:
				min_index = j
		l[i], l[min_index] = l[min_index], l[i]


if __name__ == '__main__':
	l = [3, 2, 1, 6, 5, 9, 4]
	print 'Before sort: ', l
	selections_sort(l)
	print 'after sort: ', l