# -*- coding: utf-8 -*-
import os
path = input('Please enter the file path(end with /):')
path += os.sep
source = '' # 需要统一加入文件名中的内容
# 获取该目录下所有文件，存入列表中
fileList = os.listdir(path)

# 批量修改文件名
for fileName in fileList:
    oldName = path + fileName
    # 去除掉文件名中'_hd_'以及后面的内容
    if fileName.find('_hd_') != -1:
        extension = fileName[fileName.find('.'):] # 获取文件扩展名
        newName = path + source + fileName[:fileName.find('_hd_')] + \
                  extension
    else:
        newName = path + source + fileName
    os.rename(oldName, newName)
    print(newName)
    