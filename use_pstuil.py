#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/6/23 17:56 
# @Author : TFrose 
# @Version : V 0.1
# Product : PyCharm
# Project : AutoScript
# @File : use_pstuil.py
# @desc : use pstuil and get data of the linux system

import paramiko

# 建立一个sshclient对象
ssh = paramiko.SSHClient()
# 允许将信任的主机自动加入到host_allow 列表，此方法必须放在connect方法的前面
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 调用connect方法连接服务器
ssh.connect(hostname='114.116.79.140', port=22, username='root', password='Dans12a?')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('df -hl')
# 结果放到stdout中，如果有错误将放到stderr中
print(stdout.read().decode())
# 关闭连接
ssh.close()