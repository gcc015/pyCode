# -*- coding: utf-8 -*-
# 暂停1秒输出

import time

myDog = {
    'Name': 'Gouzi',
    'Age': '3'
}

for key, value in myDog.items():
    print(key, value)
    time.sleep(1)