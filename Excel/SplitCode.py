# -*- coding: utf-8 -*-

'''
功能：
将记录在一个单元格中的用逗号分隔的数据拆分成独立记录每个Code的数据格式

思路：
1. 使用xlrd库和xlsxwriter库读取和写入Excel文件；
2. 创建空的sheetList，将原始数据字段名逐个添加到sheetList中，由此得出sheetList的
   长度等于原始数据的列数；
3. 使用sheetList的长度作为最外层循环，这样可以保证每个sheet中的数据都对应原始数据
   中对应的那一列的数据（比如sheetList[0]这个sheet中写入的是原始数据第0列的数据）
4. 使用split()将单元格中的数据拆分开，并由此可得到需要拆分的列数；
5. 将数据逐个写入新的WorkBook中
'''
import os
import xlrd
import xlsxwriter
import time

print('Starting task...')
file_path = os.getcwd() + '/'
read_file = "SplitCode.xlsx"
output_file = "SplitCode_Output.xlsx"
read = xlrd.open_workbook(file_path + read_file)
read_sheet = read.sheet_by_index(0)
rows = read_sheet.nrows
cols = read_sheet.ncols
print('Creating new WorkBook...')
time.sleep(1)
print('Creating new Sheets...')
write = xlsxwriter.Workbook(file_path + output_file)
sheetList = []
for row in range(rows):
    for column in range(cols):
        if row == 0:
            value = read_sheet.cell_value(0, column)
            qID = value.split(":")[0]
            sheetList.append(qID)
          
time.sleep(5)
print('Reading original data...')
for sheet in range(len(sheetList)):
    write_sheet = write.add_worksheet(sheetList[sheet])
    for row in range(1, rows):
        codes = read_sheet.cell_value(row, sheet).split(",")
        for outCols in range(len(codes)):
            write_sheet.write(row, outCols, codes[outCols])
time.sleep(3)
print('Splitting original data...')
time.sleep(10)
print('Writing data to new WorkBook...')
time.sleep(5)
print('Task complete!')
time.sleep(1) 
write.close()


