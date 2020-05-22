# -*- coding: utf-8 -*-
# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# 程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....

def countRabbit(n):
    rList = []
    if n == 1:
        rList = [1]
    elif n == 2:
        rList = [1, 1]
    else:
        rList = [1, 1]
        for i in range(2, n):
            rList.append(rList[-1] + rList[-2])
    
    return rList

print(countRabbit(12))