# -*- coding: utf-8 -*-
'''
Bain(p6383795)
Q27数据为0的，Q41补0
其中Q27共8列数据，在Excel的1-9列，Q41从第9列开始
Q27的1列对应Q41的9,17,25,33列，以此类推
'''
import os
import xlrd as xr
import xlsxwriter as xw

file_path = os.getcwd() + '/'
file_name = 'CNdata_10.24.xlsx'
out_file = 'BainOutput.xlsx'
data = xr.open_workbook(file_path + file_name) # 读取数据
sheet = data.sheet_by_index(1)
rows = sheet.nrows # 获取数据行数
cols = sheet.ncols # 获取数据列数

qID = [] # 获取题号
for i in range(cols):
    qesID = sheet.cell_value(0, i)
    if qesID.find(':') != -1: # 题号中有冒号的，去掉冒号及后面的内容
        qID.append(qesID[:qesID.index(':')])
    else:
        qID.append(qesID)

out_data = xw.Workbook(file_path + out_file) # 创建新的Excel Workbook
out_data_sheet = out_data.add_worksheet() # 为新的Wrokbook添加Sheet

for row in range(rows):
    for col in range(cols):
        if row == 0: # 写入题号
            out_data_sheet.write(0, col, qID[col])
        else: # 写入数据
            out_data_sheet.write(row, col, sheet.cell_value(row, col))

for q27 in range(1, 9):
    for row in range(1, rows):
        if sheet.cell_value(row, q27) == 0:
            out_data_sheet.write(row, q27 + 8, 0)
            out_data_sheet.write(row, q27 + 16, 0)
            out_data_sheet.write(row, q27 + 24, 0)
            out_data_sheet.write(row, q27 + 32, 0)

out_data.close()