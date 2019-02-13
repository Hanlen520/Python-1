#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/13 15:03
# FileName: D11_13模块xml模块.py
# Description: 
# Question: 
# --------------------------------
import xml.etree.ElementTree as ET

tree = ET.parse("./Xml/country_xml.xml")
root = tree.getroot()
# print(root.tag)
# data

# 修改节点数据
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("updated", 'YES')
tree.write(r"./Xml/country_xml.xml")

# 删除节点数据
for country in root.findall("country"):
    rank = int(country.find('rank').text)
    if rank > 2:
        root.remove(country)
tree.write(r"./Xml/country_remove_xml.xml")

# 创建一个xml文件
create_xml = ET.Element("namelist")
name = ET.SubElement(create_xml, "name", attrib={'enrolled': 'yes'})
age = ET.SubElement(name, "age", attrib={'checked': 'no'})
sex = ET.SubElement(name, 'sex')
sex.text = '24'
name2 = ET.SubElement(create_xml, 'name', attrib={'enrolled': 'no'})
age = ET.SubElement(name2, 'age')
age.text = '23'

# 生成文档对象
et = ET.ElementTree(create_xml)
et.write("./Xml/create_xml.xml", encoding='utf-8', xml_declaration=True)
# 打印生成的格式
ET.dump(create_xml)