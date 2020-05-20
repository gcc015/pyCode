# -*- coding: utf-8 -*-
# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。

sort_list = []

for i in range(3):
    x = input('integer:')
    sort_list.append(x)

sort_list.sort()
print(sort_list)