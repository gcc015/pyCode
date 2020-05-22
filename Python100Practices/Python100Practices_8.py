# -*- coding: utf-8 -*-
# 输出 9*9 乘法口诀表。

for row in range(1,10):
    print()
    for col in range(1, row+1):
        print(f'{row}*{col}={row*col}', end=' ') 
