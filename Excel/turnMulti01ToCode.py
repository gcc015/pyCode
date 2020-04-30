# -*- coding: utf-8 -*-

'''
1. 使用xlrd库和xlsxwriter库读取和写入Excel文件；
2. 使用字符串对象的split()方法将题号中下划线后的code码分离出来，写入对应数据为1的单元格里；
3. 将每条数据选到的code码存储在list中；
4. 使用字符串对象的join()方法将list中的元素以逗号分隔的形式相连，并将其写入最后一列的单元格中
5. 将list清空，重复步骤2-4
'''
import os
import xlrd
import xlsxwriter

file_path = os.getcwd() + '/'
read_file = ""
output_file = ""
read = xlrd.open_workbook(file_path + read_file)
read_sheet = read.sheet_by_index(0)
rows = read_sheet.nrows
cols = read_sheet.ncols
write = xlsxwriter.Workbook(file_path + output_file)
write_sheet = write.add_worksheet()
code = []
cstr = ","

for row in range(rows):
    for column in range(cols):
        if row == 0 or column == 0:
            write_sheet.write(row, column, read_sheet.cell_value(row, column))
        elif read_sheet.cell_value(row,column) == '1':
            value = str(read_sheet.cell_value(0,column)).split("_")[1]
            write_sheet.write(row, column, value)
            code.append(value)
    if row != 0:
        code = cstr.join(code)
        write_sheet.write(row, cols, code)
        code = []    

write.close()
