# -*- coding: utf-8
'''
功能：
将Excel中的汉字转为拼音
如 北京 --> BEIJING
'''
import os
import xlrd
import xlsxwriter
from pypinyin import lazy_pinyin as lp
file_path = os.getcwd() + "/"
read_file = "CityName.xlsx"
out_file = "outCityName.xlsx"
read = xlrd.open_workbook(file_path + read_file)
read_sheet = read.sheet_by_index(0)
rows = read_sheet.nrows
cols = read_sheet.ncols
write = xlsxwriter.Workbook(file_path + out_file)
write_sheet = write.add_worksheet("sheet1")

for row in range(rows):
    name = lp(read_sheet.cell_value(row, 0))
    length = len(name)
    cityName = ''
    for num in range(length):
        cityName += str(name[num])
    write_sheet.write(row, 0, cityName.upper())

write.close()