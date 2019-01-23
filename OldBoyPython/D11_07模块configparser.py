#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/23 23:01
# FileName: D11_07模块configparser.py
# Description: 用于生成和修改常见配置文档，当前模块的名称在python3.x 版本中变更为configparser
# Question:
# --------------------------------------

import configparser

config = configparser.ConfigParser()

# 1. 写生成配置文件
config["DEFAULT"] = {
    "Server": "WeChat",
    "Host": "118.23.4.5",
    "Port": "22"
}

config["Project"] = {}
config["Project"]["Name"] = "ConfigProject"
config["Project"]["Size"] = "456"

config["Content"] = {
    "Age": "23",
    "high": "175",
    "weight": "65",
    "remove": "Yes"
}

config["Remove"] = {
    "remove": "YES"
}


# with open("C:\\MySpace\\Python\\OldBoyPython\\Config\\config.ini", 'w') as configWrite:
#     config.write(configWrite)

# 2. 读取配置文件
config.read("C:\\MySpace\\Python\\OldBoyPython\\Config\\config.ini")
print(config.sections())  # 打印配置文件中配置项的第一次，除了默认项
print(config.defaults())  # 获取配置文件中配置默认项
print("Content" in config)
print("age" in config)
print(config["Content"]["age"])  # 获取配置文件配置项下一层的具体的值
# 获取配置文件中配置项
for i in config:
    print(i)
# 获取配置文件中配置项和默认项的值
for i in config["Content"]:
    print(i)

# 3. 删除文件中某一项
config.remove_section("Remove")
print(config.has_section("Remove"))
config.remove_option("Content", "remove")
print(config.has_option("Content", "remove"))

# 4. 更改某一项的值
config.set("Content", "Age", "24")
print(config["Content"]["Age"])
