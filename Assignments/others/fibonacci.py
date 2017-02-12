# -*- coding=utf-8 -*-
""" 斐波那契数列数列
    f(n) = f(n - 1) + f(n - 2)
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...
"""
__author__ = 'cleland'
known = {0: 0, 1: 1}


def fibonacci(n):
    if n <= 1:
        return n
    result = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = result
    return result


def main():
    fibonacci(5)
    print known


if __name__ == '__main__':
    main()
