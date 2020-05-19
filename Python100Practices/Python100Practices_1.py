# -*- Coding: utf-8
# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件
# 的排列。

count = 0
for hundred in range(1, 5):
    for decade in range(1, 5):
        for unit in range(1, 5):
            if (hundred != decade and hundred != unit and
                decade != unit):
                count += 1
                print(hundred * 100 + decade * 10 + unit)

print(f'1、2、3、4四个数字能组成{count}个互不相同且无重复数字的三位数')