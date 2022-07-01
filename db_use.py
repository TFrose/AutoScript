#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2023/1/5 15:40 
# @Author : TFrose 
# @Version : V 0.1
# Product : PyCharm
# Project : AutoScript
# @File : db_use.py
# @desc :


import pymssql

conn = pymssql.connect(host='127.0.0.1',user = 'root' # 用户名
,password='Dans12a?' # 密码
,port= 3306 # 端口，默认为3306
,database='testdb' # 数据库名称
,charset='utf8' # 字符编码
)

print(conn)