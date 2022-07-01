#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/11/14 16:43 
# @Author : TFrose 
# @Version : V 0.1
# Product : PyCharm
# Project : AutoScript
# @File : test.py
# @desc :

import os
import glob

print("Output #145:")
inputPath = r'C:\Users\yongc\Desktop'
for input_file in glob.glob(os.path.join(inputPath, '*.txt')):
    with open(input_file, 'r', newline='', errors='ignore') as filereader:
        for row in filereader:
            print("Output: %s" %(row.split('\n')))