# -*- coding: utf-8 -*-
# 斐波那契数列。
# 程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，
# 指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

# 返回斐波那契数列的第n个数
def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a + b
    return a

print(fib(10))

# 返回n个数的斐波那契数列
def fibSeq(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    
    return fibs


print(fibSeq(10))