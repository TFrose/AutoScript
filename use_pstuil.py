#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/6/23 17:56 
# @Author : TFrose 
# @Version : V 0.1
# Product : PyCharm
# Project : AutoScript
# @File : use_pstuil.py
# @desc : use pstuil and get data of the linux system to deal

import paramiko

def conssh():
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

def consftp():
    import paramiko
    # 获取Transport实例
    tran = paramiko.Transport("114.116.79.140", 22)
    # 连接SSH服务端
    tran.connect(username="root", password="Dans12a?")
    # 获取SFTP实例
    sftp = paramiko.SFTPClient.from_transport(tran)
    # 设置上传的本地/远程文件路径
    localpath = "D:\Program Files\IDM\Download\mysql-5.7.38-linux-glibc2.12-x86_64.tar.gz"  ##本地文件路径
    remotepath = "/root"  ##上传对象保存的文件路径
    # 执行上传动作
    sftp.put(localpath, remotepath)

    tran.close()

if __name__ == '__main__':
    consftp()