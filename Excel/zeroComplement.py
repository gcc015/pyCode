# -*- coding: utf-8 -*-

'''
使用pandas库写入Excel的方法，na_rep参数设为0
若不需要pandas读取数据时自动生成的index，则将
index参数设为False
'''
import os
import pandas as pd
file_path = os.getcwd()
read_file = ""
output_file = ""
data = pd.read_excel(file_path + "/" + read_file)
data.to_excel(file_path + "/" + output_file, sheet_name="Sheet1", na_rep=0, index=False)
