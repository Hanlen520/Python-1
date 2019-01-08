#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/8 20:21
# FileName: D6_05三级菜单优化.py
# Description: 
# Question: 
# --------------------------------
menu = {
    '北京': {
        '朝阳': {
            '国贸': {
                '中金': {},
                'CCTV': {},
                '渣打银行': {}
            },
            '望京': {
                '陌陌': {},
                '奔驰': {},
                '360': {}
            },
            '三里屯': {
                'Apple': {},
                '优衣库': {},
                '加拿大鹅': {}
            }
        },
        '海淀': {
            '后厂村': {
                '百度': {},
                '网易': {},
                '新浪': {}
            },
            '中关村': {
                '爱奇艺': {},
                '优酷': {},
                '优信二手车': {}
            },
            '五道口': {
                '北京大学': {},
                '清华大学': {},
                '中国人民大学': {}
            }
        },
        '昌平': {
            '沙河': {
                '沙河地铁站': {},
                '沙河公交站': {},
                '沙河大桥': {}
            },
            '回龙观': {
                '回龙观地铁站': {},
                '回龙观公交站': {},
                '回龙观街道办事处': {}
            },
            '天通苑': {
                '链家': {},
                '我爱我家': {},
                '绿地': {}
            }
        }
    },
    '上海': {
        '浦东区': {
            '陆家嘴': {
                "CICC": {},
                "高盛": {},
                "摩根士丹利": {}
            },
            '外滩': {
                "上海滩": {}
            }
        },
        '闵行区': {

        },
        '静安区': {

        }
    },
    '陕西省': {
        '西安': {
            '长安区': {
                '西安外国语大学': {},
                '西北政法大学': {},
                '西北大学': {}
            },
            '雁塔区': {
                '大雁塔': {},
                '小雁塔': {},
                '小寨': {}
            }
        },
        '渭南': {
            '临渭区': {}
        }
    }
}

current_layer = menu
parent_layers = []

while True:
    # 遍历字典打印第一层的菜单
    for key in current_layer:
        print("菜单：", key)
    choice = input("请输入：").strip()
    # 如果输入长度为0，则继续输入
    if len(choice) == 0:
        continue
    if choice in current_layer:
        # 进入子项之前，记录父层是那一层
        parent_layers.append(current_layer)
        # 根据选择进入菜单的子项
        current_layer = current_layer[choice]
    elif choice == 'b':
        # 返回父层
        if parent_layers:
            current_layer = parent_layers.pop()
    elif choice == 'q':
        print("感谢您的使用")
        break
    else:
        print("查无此项，请检查您的输入。")






