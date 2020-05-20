# -*- coding: utf-8 -*-
# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，
# 特殊情况，闰年且输入月份大于2时需考虑多加一天

year = int(input('Year:'))
month = int(input('Month:'))
day = int(input('Day:'))
dayth = day
days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
        11: 30, 12: 31
        }

for key in range(1, month):
    dayth += days[key]

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    if month > 2:
        dayth += 1

print(f'It is the {dayth}th day.')