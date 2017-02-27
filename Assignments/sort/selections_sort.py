# -*- coding: utf-8 -*-
__author__ = 'cleland'


def selections_sort(l):
    """ 选择排序
    冒泡算法，每次比较如果发现较小的元素在后面，就交换两个相邻的元素。而选择排序算法的改进在于得到所谓的最小值时再做交换
    序列顺序从左到右是从小到大，伪代码：
	for i in [0, n)
		min = a[i]
		min_index = i
		for j in (i, n-1)
			if a[j+1] < min
				min = a[j+1]
				min_index = j+1
		swap(a[i], a[min_index])
    """
    for i in xrange(0, len(l)):
    	min = l[i]
    	min_index = i
    	for j in xrange(i, len(l)-1):
    		if l[j+1] < min:
    			min = l[j+1]
    			min_index = j+1
    	l[i], l[min_index] = l[min_index], l[i]


def main():
    l1 = [5, 2, 4, 6, 1, 3, 1]
    print 'before sort: ', l1
    selections_sort(l1)
    print 'after sort: ', l1


if __name__ == '__main__':
    main()
