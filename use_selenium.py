#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/6/23 17:27 
# @Author : TFrose 
# @Version : V 0.1
# Product : PyCharm
# Project : AutoScript
# @File : use_selenium.py
# @desc : use selenium to deal web server

from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
options = EdgeOptions()
options.use_chromium = True
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" # 浏览器的位置
driver = Edge(options=options, executable_path=r"D:\Program Files\IDM\Download\edgedriver_win64\msedgedriver.exe") # 相应的浏览器的驱动位置

driver.get("http://www.baidu.com")